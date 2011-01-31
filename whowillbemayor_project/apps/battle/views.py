from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import cache_page

import datetime
import tweepy


@cache_page(60 * 5)
def home(request):
    smack_talk = tweepy.api.search("gsiegman jennidigital")
    
    g_tweets = []
    j_tweets = []
    
    for tweet in smack_talk:
        if tweet.from_user_id_str == "1343613":
            g_tweets.append(tweet)
        elif tweet.from_user_id_str == "161171102":
            j_tweets.append(tweet)
    
    now = datetime.datetime.now()
    
    return render_to_response("battle/home.html", {
        "g_tweets": g_tweets[:5],
        "j_tweets": j_tweets[:5],
        "now": now,
    }, context_instance=RequestContext(request))

