import os
from openai import OpenAI

try:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
    print(f"ERRO: It was not possible to create OpenAI client. Check your OPENAI_API_KEY in .env")
    client = None

def feeling_analyer(text):
    """
    Use the API to classify the text.
    """
    if client is None:
        return "ERRO_IA_CLIENTE"

    system_prompt = """
    You're a financial markets assistant.
    Assess the sentiment of the given text about stocks or financial markets.
    Please answer using one of the following labels only: Positive, negative or neutral.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0,
            max_tokens=10
        )
        return response.choices[0].message.content.strip().upper()
    except Exception as e:
        print(f"Erro na API da OpenAI: {e}")
        return "ERRO_IA_ANALISE"