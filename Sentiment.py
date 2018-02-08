import tweepy
from textblob import TextBlob
import re

consumer_key = "YOUR CONSUMER KEY"
consumer_secret= "YOUR CONSUMER SECRET KEY"

access_token= "YOUR ACCESS TOKEN"
access_token_secret = "YOUR ACCESS SECRET TOKEN"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

topic=input("Enter topic: ");
public_tweet=api.search(q=topic,count=100)
max=len(public_tweet)

sum=0
polarity="Positive"

for tweet in public_tweet:
    text=tweet.text
    textWords=text.split()
    #print (textWords)
    cleanedTweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
    print(cleanedTweet)
    analysis=TextBlob(cleanedTweet)
    sum=sum+analysis.polarity

avg_polarity=sum/max

if avg_polarity<0:
    polarity="Negative"

if (0<=avg_polarity<=0.2):
    polarity="Neutral"

print("Polarity: "+polarity)