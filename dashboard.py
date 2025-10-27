import streamlit as st
import pandas as pd
import plotly.express as px
import os

DATA_FILE = "feelings.csv"

st.set_page_config(page_title="Feeling Analyzer", layout="wide")
st.title(f"Feeling Dashboard 📊")

@st.cache_data(ttl=60) 
def reload_file(file):
    if not os.path.exists(file):
        return pd.DataFrame(columns=["id", "timestamp", "text", "feeling"])
    try:
        df = pd.read_csv(file)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["id", "timestamp", "text", "feeling"])
    except Exception as e:
        st.error(f"Error to reload data: {e}")
        return pd.DataFrame(columns=["id", "timestamp", "text", "feeling"])

df = reload_file(DATA_FILE)

if st.button('Force Update 🔄'):
    st.cache_data.clear()
    df = reload_file(DATA_FILE)

if df.empty:
    st.warning(f"Any data colected in '{DATA_FILE}'. Run the script `collector.py` first.")
else:
    st.subheader("General Metrics")
    total_comments = len(df)
    
    feeling_counting = df['feeling'].value_counts()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total of comments", total_comments)
    col2.metric("Positive 👍", feeling_counting.get("Positive", 0))
    col3.metric("Negative 👎", feeling_counting.get("Negative", 0))
    col4.metric("Neutal 😐", feeling_counting.get("Neutral", 0))

    st.subheader("Time Series of Feelings")
    
    df_grouped = df.set_index('timestamp').resample('H')['feeling'].value_counts().unstack(fill_value=0)
    df_grouped = df_grouped.reset_index()
    
    for col in ["Positive", "Negative", "Neutral"]:
        if col not in df_grouped.columns:
            df_grouped[col] = 0
            
    fig = px.line(df_grouped, 
                  x='timestamp', 
                  y=["Positive", "Negative", "Neutral"], 
                  title="Count of Feelings Over Time",
                  color_discrete_map={
                      "Positive": "green",
                      "Negative": "red",
                      "Neutral": "blue"
                  })
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Recent Comments Analyzed")
    st.dataframe(df.sort_values('timestamp', ascending=False).head(20))