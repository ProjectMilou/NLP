import nltk

def getFrequencyFromTweets(tweets):
    # TODO: Implement
    tokens = nltk.word_tokenize(tweets)
    return tokens