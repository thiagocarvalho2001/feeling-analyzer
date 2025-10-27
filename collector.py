import os
import pandas as pd
from dotenv import load_dotenv

from core.reddit_client import get_reddit_instance
from core.feeling_analyzer import feeling_analyer

load_dotenv() 

SEARCH_TERM = "Nubank"
SUBREDDIT = "farialimabets"
OUTPUT_FILE = "feelings.csv"


def reload_processed_ids(file):
    """Read the CSV file and return a set of processed comment IDs."""
    try:
        df_existence = pd.read_csv(file)
        return set(df_existence['id'])
    except FileNotFoundError:
        return set()

def save_data(data_list, file):
    """Save the list of data to the CSV file."""
    if not data_list:
        return
        
    df_news = pd.DataFrame(data_list)
    
    mode = 'a' if os.path.exists(file) else 'w'
    header = not os.path.exists(file)
    
    df_news.to_csv(file, mode=mode, header=header, index=False)
    print(f"--- Save {len(data_list)} new comments on {file} ---")


def main():
    print("Starting the Reddit comment collector...")
    
    reddit = get_reddit_instance()
    if reddit is None:
        print("It was not possible to connect to Reddit. Exiting.")
        return

    processed_ids = reload_processed_ids(OUTPUT_FILE)
    print(f"Loaded {len(processed_ids)} already processed comment IDs.")

    data_to_save = []
    subreddit_target = reddit.subreddit(SUBREDDIT)
    
    print(f"--- Monitoring '{SEARCH_TERM}' on r/{SUBREDDIT} in real time ---")

    try:
        for comment in subreddit_target.stream.comments(skip_existing=True):
            
            if comment.id in processed_ids:
                continue

            if SEARCH_TERM.lower() in comment.body.lower():
                comment_text = comment.body
                print(f"\n[New comment] ID: {comment.id}")
                print(f"Text: {comment_text[:100].replace('\n', ' ')}...")
                
                feeling = feeling_analyer(comment_text)
                print(f"Feeling: {feeling}")
                
                if feeling in ["Positive", "Negative", "Neutral"]:
                    data_to_save.append({
                        "id": comment.id,
                        "timestamp": pd.to_datetime(comment.created_utc, unit='s'),
                        "text": comment_text,
                        "feeling": feeling
                    })
                    processed_ids.add(comment.id)

                if len(data_to_save) >= 5:
                    save_data(data_to_save, OUTPUT_FILE)
                    data_to_save = []

    except KeyboardInterrupt:
        print("\n--- Manual interruption received. Exiting... ---")
    finally:
        save_data(data_to_save, OUTPUT_FILE)
        print("--- Finished. ---")

if __name__ == "__main__":
    main()