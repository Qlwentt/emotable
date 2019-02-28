#!/usr/bin/env python

"""Utility class for searching Twitter API for specific emojis
and saving to csv files for training/validation data"""

import pandas
import os, sys, re
import json
import tweepy
import searchtweets
from definitions import ROOT_DIR


class TweetCollector:
    def __init__(self):
        self.twitter_api_key = os.environ['TWITTER_API_KEY']
        self.twitter_api_secret = os.environ['TWITTER_API_SECRET']
        self.twitter_access_token = os.environ['TWITTER_API_TOKEN']
        self.twitter_access_token_secret = os.environ['TWITTER_API_TOKEN_SECRET']
        self.positive_emojis_csv = "{0}/data/emojis/positive/face-smiley.csv".format(ROOT_DIR)
        self.negative_emojis_csv = "{0}/data/emojis/negative/face-negative.csv".format(ROOT_DIR)

    def authenticate(self):
        self.premium_search_args = searchtweets.load_credentials("{0}/.twitter_keys.yaml".format(ROOT_DIR),
                                       yaml_key="search_tweets_30_day",
                                       env_overwrite=False)
        auth = tweepy.OAuthHandler(self.twitter_api_key, self.twitter_api_secret)
        auth.set_access_token(self.twitter_access_token, self.twitter_access_token_secret)
        self.api = tweepy.API(auth)

    def get_positive_tweets(self):
        positive_emoji_codes = get_emoji_unicodes_list(self.positive_emojis_csv)
        positive_tweets = self.get_emoji_tweets(positive_emoji_codes)
        return clean_tweets(positive_tweets, 1)
        # for positive_emoji_code in positive_emoji_codes:
        #     positive_tweets =
        #     return clean_tweets(positive_tweets, 1)
        #     # write to file
        #     # path = "{0}/data/tweets/positive/".format(ROOT_DIR)
        #     # filename = "raw_positive_tweets.csv"
        #     # write_to_csv(tweets_dict, filename)
        #     # # writeToJSONFile(path, filename, positive_tweets)

    def get_negative_tweets(self):
        negative_emoji_codes = get_emoji_unicodes_list(self.negative_emojis_csv)
        negative_tweets = self.get_emoji_tweets(negative_emoji_codes)
        return clean_tweets(negative_tweets, 0)
        # for negative_emoji_code in negative_emoji_codes:
        #     # negative_tweets =
        #     return clean_tweets(negative_tweets, 0)
        #     # write_to_csv(negative_tweet_dict, filename)
        #     # write to file
        #     # path = "{0}/data/tweets/negative/".format(ROOT_DIR)
        #     # filename = "raw_negative_tweets.json"
        #     # writeToJSONFile(path, filename, negative_tweet_group)


    def get_emoji_tweets(self, emoji_list):
        emoji_list = ' OR '.join(emoji_list);
        print(emoji_list)
        max_tweets = 100
        rule = searchtweets.gen_rule_payload(emoji_list,
                        # from_date="2017-01-01", #UTC 2017-09-01 00:00
                        # to_date="2019-02-12",#UTC 2017-10-30 00:00
                        results_per_call=max_tweets)
        print(rule)
        tweets = searchtweets.collect_results(rule, max_results=500, result_stream_args=self.premium_search_args)
        return tweets


# def writeToJSONFile(path, filename, data):
#     with open(filename, 'w') as fp:
#         json.dump(data, fp, indent=2)
#     try:
#         filePathNameWExt = path + filename
#         with open(filePathNameWExt, 'w') as fp:
#             json.dump(data, fp)
#     except Exception as e:
#         print ("writeToJSONFile exception")
#         print (e)

 # - english only
 # - no question marks
 # - no negative emoji
 # - must have a subject and a verb


# def limit_handled(cursor):
#     while True:
#         try:
#             yield cursor.next()
#         except tweepy.RateLimitError:
#             time.sleep(15 * 60)


# def clean_emoji_code(raw_code):
#     return raw_code.replace('U+','')

def remove_emojis(text):
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    without_emoji = emoji_pattern.sub(r'', text) # no emoji
    return text

def clean_tweets(tweets, sentiment):
    cleaned_tweets = {'tweet_text':[], 'sentiment': []}
    for tweet in tweets:
        if tweet.lang == 'en' and "?" not in tweet.text:
            tweet_text = " ".join(filter(lambda x:x[0]!='@', tweet.text.split()))
            cleaned_tweets['sentiment'].append(sentiment)
            cleaned_tweets['tweet_text'].append(tweet_text)

    # print(cleaned_tweets['tweet_text'])
    return cleaned_tweets

def write_to_csv(tweets_dict, filename):
    tweets_df = pandas.DataFrame(tweets_dict)
    tweets_df.to_csv(filename, sep=',')



def get_emoji_unicodes_list(file):
    # reads csv of emojis
    # returns list of unicode representations of emojis
    emoji_data = pandas.read_csv(file)
    return emoji_data['Browser'].tolist()
