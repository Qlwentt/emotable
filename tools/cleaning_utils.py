#!/usr/bin/env python
import re

def remove_emojis(text):
    text = u'This dog \U0001f602'
    print(text) # with emoji

    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            # u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            # u"\U0001F680-\U0001F6FF"  # transport & map symbols
            # u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    without_emoji = emoji_pattern.sub(r'', text) # no emoji
    print (without_emoji)
    return without_emoji

def remove_unwated_tweets(tweets):
    cleaned_tweets = []
    for tweet in tweets:
        if tweet.lang == 'en' and "?" not in tweet.text and len(tweet.text) <= 150:
            print(tweet.text)
            cleaned_tweets.append(tweet)
    # print ("there are {0} tweets".format(len(cleaned_tweets)))
    return cleaned_tweets
