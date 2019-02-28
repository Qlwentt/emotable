#!/usr/bin/env python

"""Gets tweets by searching Twitter API for specific emojis
and saves to file for training/validation data"""
import pandas
import sys
import time;
from tools.tweet_collector import TweetCollector

tweet_collector = TweetCollector()
tweet_collector.authenticate()
pos_dict = tweet_collector.get_positive_tweets()
neg_dict = tweet_collector.get_negative_tweets()

pos_df = pandas.DataFrame(pos_dict)
neg_df = pandas.DataFrame(neg_dict)

tweets_df = pandas.concat([pos_df, neg_df])

ts = time.time()
tweets_df.to_csv("labled_tweets-{0}.csv".format(ts), sep=',')
