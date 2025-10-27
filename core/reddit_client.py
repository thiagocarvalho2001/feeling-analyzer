import os
import praw

def get_reddit_instance():
    """
    Create and return a Reddit instance using PRAW.
    Returns None if the connection fails.
    """
    try:
        reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT"),
        )
        reddit.user.me() 
        print("Connection with Reddit successful.")
        return reddit
    except Exception as e:
        print(f"ERRO: It was not possible to connect to Reddit. Check your REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, and REDDIT_USER_AGENT in .env")
        print(f"Error detail {e}")
        return None
