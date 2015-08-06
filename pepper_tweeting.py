# coding:utf-8

from naoqi import ALProxy

import sys
import json
import re

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from settings import consumer_key, consumer_secret, access_token, access_token_secret

class StdOutListener(StreamListener):

    def __init__(self, pepper_host, pepper_port):
        self.pepper_host = pepper_host
        self.pepper_port = pepper_port

    def on_data(self, data):
        d = json.loads(data)
        raw_tweet = d["text"]

        tweet = Cleanser.cleanse(raw_tweet)
        print("%s -> %s" % (raw_tweet, tweet))

        tts = ALProxy("ALTextToSpeech", self.pepper_host, self.pepper_port)
        tts.say(str(tweet.encode("utf-8")))

        return True

    def on_error(self, status):
        print(status)

class Cleanser(object):

    @classmethod
    def cleanse(cls, tweet):
        # remove RT:
        tweet = re.sub(r"(RT)", " ", tweet)
        # remove URL
        tweet = re.sub(r"(?:^|[\s　]*)((?:https?|ftp)://[\w/:%#\$&\?\(\)~\.=\+\-]+)", " ", tweet)
        # remove hash tag
        tweet = re.sub(r"\s#([a-zA-Z0-9_]+)", " ", tweet)
        # remove screen name
        tweet = re.sub(r"(@[A-Za-z0-9_]{1,15})", " ", tweet)

        return tweet


if __name__ == "__main__":
    pepper_host = sys.argv[1]  # e.g. "192.168.0.2"
    hash_tag = sys.argv[2]  # e.g. "#pepper_say"
    pepper_port = 9559

    l = StdOutListener(pepper_host, pepper_port)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[hash_tag])
