import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

authHeader = {'Authorization': 'Bearer ' + str(BEARER_TOKEN)}
baseURL = "https://api.twitter.com/2/"

def searchRecentTweets(query, max_result=10):
    currUrl = baseURL + "tweets/search/recent"
    res = requests.get(currUrl, params={'max_results': max_result, 'query': query}, headers=authHeader)
    print(res)
    #loadedResults = json.loads(res.text)
    return res.json()#loadedResults

def prepareTweetsForNLP(tweets):
    accumulatedText = ""
    for tweet in tweets['data']:
        accumulatedText += tweet['text']
    return accumulatedText