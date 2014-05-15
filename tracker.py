import tweepy
import sys
from textwrap import TextWrapper
from textblob import TextBlob
from datetime import datetime
from elasticsearch import Elasticsearch


consumer_key="05WXdIClEQleZESrtYBQw"
consumer_secret="fRShUMDyfgHFdoe4kp3vpqxeGDYg5g6B8vyZiw0OU"

access_token="2205093792-nnx06lR2jZ64WCDIA68XxLuPwhP7HwnsytIRh0L"
access_token_secret="3E2JojFK3QCtEuWFm8FTNlSbUR8DU1JXh37DQ0p7Ic82E"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

es = Elasticsearch()

class StreamListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')

    def on_status(self, status):
        try:
            print '\n%s %s' % (status.author.screen_name, status.created_at)
            print status.text

            tweet = TextBlob(status.text)

            es.create(index="my-index", 
                      doc_type="test-type", 
                      body={ "author": status.author.screen_name,
                             "date": status.created_at,
                             "message": status.text,
                             "polarity": tweet.sentiment.polarity,
                             "subjectivity": tweet.sentiment.subjectivity }
                     )


        except Exception, e:
            pass

streamer = tweepy.Stream(auth=auth, listener=StreamListener(), timeout=3000000000 )
terms = ['intel','#edison', '#galileo']

streamer.filter(None,terms)

