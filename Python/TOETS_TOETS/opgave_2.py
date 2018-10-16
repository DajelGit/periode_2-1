# OPGAVE 2 a
import json
from pprint import pprint

tweets = []
with open('twitter.json') as f:
    tweets = json.load(f)

print(len(tweets))
for i in range(5):
    pprint(tweets[i])




# OPGAVE 2 b
the_greatest_tweets_ever_its_just_true = [(tweet["text"], tweet["retweet_count"]) for tweet in tweets if tweet["retweet_count"] > 10000]

print(len(the_greatest_tweets_ever_its_just_true))
for i in range(5):
    pprint(the_greatest_tweets_ever_its_just_true[i])




# OPGAVE 2 c
the_best_of_the_best = sorted(the_greatest_tweets_ever_its_just_true, key=lambda x: x[1])[::-1]
for i in range(5):
    pprint(the_best_of_the_best[i])




# OPGAVE 2 d
short_tweets = min(the_greatest_tweets_ever_its_just_true, key=lambda x: len(x[0]))[::-1]
print(short_tweets)