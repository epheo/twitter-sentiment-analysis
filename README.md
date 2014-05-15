## Twitter Sentiment Analysis 

Twitter crawler (for on or more given keywords) that performs a simple sentiment analysis with [textblob](http://textblob.readthedocs.org/en/dev/) (extract Polariry and Subjectivity) to determine whether tweets about something/someone are positive or negative and store them in an [ElasticSearch](http://www.elasticsearch.org/) DB.

Once you have enough Tweets in your database you can graph them with [Kibana Dashboard](http://www.elasticsearch.org/overview/kibana/) in order to visualize positives and negatives Tweets in a graph

## Requirements

This script store your tweets in an ElasticSearch Database, see [ElasticSearch-Dockerfile](https://github.com/dockerfile/elasticsearch) to launch one with Docker.
It use the twitter REST API, so you need to provide Twitter API Key and Token, see the [Twitter-API](https://apps.twitter.com/app/new) to obtain them.

The python code need Tweepy textblob and elasticsearch

```
pip install tweepy

pip install -U textblob && python -m textblob.download_corpora

pip install elasticsearch
```
