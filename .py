import os
import time
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
USER_ID = os.getenv("USER_ID")
TWEET_ID = os.getenv("TWEET_ID")

def like_tweet(user_id, tweet_id):
    url = f"https://api.twitter.com/2/users/{user_id}/likes"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "tweet_id": tweet_id
    }

    print(f"👉 Attempting to like tweet {tweet_id} for user {user_id}...")

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code in [200, 201]:
            print("✅ Tweet liked successfully!")
            print(response.json())
        elif response.status_code == 429:
            print("⏳ Rate limit hit. Waiting to retry...")
            reset_time = int(response.headers.get("x-rate-limit-reset", time.time() + 60))
            wait_time = reset_time - int(time.time())
            print(f"⏱ Sleeping for {wait_time} seconds...")
            time.sleep(wait_time)
            return like_tweet(user_id, tweet_id)
        elif response.status_code == 401:
            print("❌ Authentication failed. Check your Bearer Token.")
        else:
            print(f"❗ Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("⚠️ Request failed:", e)

if __name__ == "__main__":
    if not all([BEARER_TOKEN, USER_ID, TWEET_ID]):
        print("❌ Please set BEARER_TOKEN, USER_ID, and TWEET_ID in your .env file.")
    else:
        like_tweet(USER_ID, TWEET_ID)
