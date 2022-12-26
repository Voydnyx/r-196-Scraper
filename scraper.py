import praw
import tweepy

# Replace these with your own Reddit and Twitter API credentials
reddit = praw.Reddit(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET", user_agent="YOUR_USER_AGENT")
subreddit = reddit.subreddit("196")

auth = tweepy.OAuth1UserHandler(consumer_key="YOUR_CONSUMER_KEY", consumer_secret="YOUR_CONSUMER_SECRET", access_token="YOUR_ACCESS_TOKEN", access_token_secret="YOUR_ACCESS_TOKEN_SECRET")
api = tweepy.API(auth)

for submission in subreddit.hot(limit=10):
  if submission.url.endswith(".jpg"):
    api.update_with_media(status=submission.title, filename=submission.url)
