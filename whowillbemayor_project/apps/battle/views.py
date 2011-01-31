from django.shortcuts import render_to_response
from django.template import RequestContext

import tweepy


def home(request):
    g_timeline = tweepy.api.user_timeline("gsiegman")
    g_tweets = []
    
    for tweet in g_timeline:
        if "JenniDigital" in tweet.text or "liquor" in tweet.text:
            g_tweets.append(tweet)
    
    j_timeline = tweepy.api.user_timeline("JenniDigital")
    j_tweets = []
    
    for tweet in j_timeline:
        if "gsiegman" in tweet.text or "liquor" in tweet.text:
            j_tweets.append(tweet)
    
    return render_to_response("battle/home.html", {
        "g_tweets": g_tweets[:5],
        "j_tweets": j_tweets[:5]
    }, context_instance=RequestContext(request)
    )


