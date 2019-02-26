import csv, nltk, re

DATA_PATH="../data/"

DATA = DATA_PATH + "labeled_data.csv"

def readData(path):
    data = []
    with open(path,'r') as file:
        data = [x for x in csv.reader(file, delimiter=',')]
    return data

def getTweets(raw):
    data = [x[6] for x in raw]
    return data

def removePattern(tweet, pattern):
    r = re.findall(pattern, tweet)
    for x in r:
        tweet = re.sub(x, '', tweet)
    return tweet

def preprocess(data):
    cleanData = []
    for tweet in data:
        tweet = removePattern(tweet, "@[\w]*")
        tweet = tweet.replace("#", "") # Removing '#' from hashtags
        tweet = tweet.replace("[^a-zA-Z#]", " ") # Removing punctuation and special characters
        tweet = re.sub(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',"<URL>", tweet)
        tweet = re.sub(" +", " ", tweet)
        tweet = tweet.lower()
        cleanData.append(tweet)
        print(tweet)
    return cleanData

if __name__ == "__main__":
    raw = readData(DATA) 
    tweets = getTweets(raw)
    preprocess(tweets)
