Twitter Like Bot

A Python script to authenticate with the Twitter API v2 and like a tweet using its ID.
Features

- OAuth 2.0 Bearer Token authentication
- Handles rate limits and common API errors
- Logs execution status and errors
- Uses `.env` for secure credential storage

Setup

Clone the repo 
   ```bash 
   git clone https://github.com/yourusername/twitter-like-bot.git
   cd twitter-like-bot

Install Dependencies
pip install -r requirements.txt
Setup .env:

Rename .env.example to .env

Fill in your credentials:

ini
Copy
Edit
BEARER_TOKEN=your_real_token
USER_ID=your_user_id
Run the script:

bash
Copy
Edit
python like_tweet.py

