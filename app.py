from flask import Flask,jsonify,request
from flask_restful import Resource,Api,reqparse
import tweepy
from textblob import TextBlob
import re

app=Flask(__name__)
api=Api(app)

consumer_key = "WdcIxzy3ovIOfT0Qpt8KR6x8F"
consumer_secret= "TWrMtfz4EZePznAzvjmt3bt0Z1suNCc8xmPVkogcltAQvEQFXV"

access_token= "960546971818889216-HsjgFIOjN1Bi4Fat935VhSxup8aHnmx"
access_token_secret = "BtmG38zWaE6DxAbGp5XdHFCEUnNROjVGaFVp6SFGAmG7p"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api2=tweepy.API(auth)

class sentiment(Resource):
   
    
    def get(self,topic):
        
        polarity=getPolarity(topic)
        result={ "polarity": polarity }
        return result ,200



def getPolarity(topic):
    public_tweet=api2.search(q=topic,count=100)
    max=len(public_tweet)
    
    sum=0
    polarity="Positive"

    for tweet in public_tweet:
        text=tweet.text
        textWords=text.split()
        #print (textWords)
        Tweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
        #print(Tweet)
        analysis=TextBlob(Tweet)
        sum=sum+analysis.polarity

    avg_polarity=sum/max

    if avg_polarity<0:
        polarity="Negative"

    if (0<=avg_polarity<=0.2):
        polarity="Neutral"

    return polarity


api.add_resource(sentiment,"/<string:topic>")

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True) 