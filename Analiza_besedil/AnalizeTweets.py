import os

import textBlob
import csv

import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords

#####
##Prebere twite jih analizira in zapiše v novo csv datoteko z istim imenom v drug direktorij
#####
def readFiles(path):
    tweets = []
    header = 0
    with open(path, newline='',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile,delimiter=';')
        for row in reader:
            if header != 0:
                dict = {}
                #username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink
                try:
                    dict["date"] = row[1]
                    dict["retweets"] = row[2]
                    dict["favorites"] = row[3]
                    dict["text"] = row[4]
                    #dict["geo"] = row[5]
                    dict["mentions"] = row[6]
                    dict["hashtags"] = row[7]
                    dict["id"] = row[8]
                    #dict["permalinks"] = row[9]
                    tweets.append(dict)
                except:
                    print("exception wrong data type")
            header+=1;
    return tweets;

#Zakomentirana koda spodaj je samo za kratko analizo oz. testiranje (koliko je poz, neg, neutr twitov)
######TEXT BLOB
'''neutral = 0
p = 0
n = 0
for tweet in tweets:
    sentiment = textBlob.get_txt_sentiment(tweet['text']);
    if(sentiment[0] == "negative"):
        print(tweet['retweets'], sentiment)
    if sentiment[0] == "positive":
        p+=1
    elif sentiment[0] == "negative":
        n+=1
    else:
        neutral+=1
print("positive: ",p," negative:", n,"neutral: ", neutral)
'''

#V podano datoteko zapiše analizirane podake
'''
with open('AnaliziraniPodatki/01.01.2017 - 01.01.2019/'+fileName, newline='', mode='w',encoding="utf8") as file:
    file_writer = csv.writer(file, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['date','retweets','favorites','text','sentiment','polarity','subjectivity'])
    for tweet in tweets:
        sentiment = textBlob.get_txt_sentiment(tweet['text'])
        file_writer.writerow([tweet['date'],tweet['retweets'],tweet["favorites"],tweet["text"],sentiment[0],sentiment[1][0],sentiment[1][1]])
 #   employee_writer.writerow(['John Smith', 'Accounting', 'November'])
 '''


#######NOVA ANALIZA
class PreProcessTweets:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    def processTweets(self, list_of_tweets_dict):
        processedTweets_dict = []
        for tweet in list_of_tweets_dict:
            tweet["text"] = (self._processTweet(tweet["text"]))
            processedTweets_dict.append(tweet)
        return processedTweets_dict

    def _processTweet(self, tweet):
        tweet = tweet.lower()  # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]


tweets = []
#reading all files from file:
path = 'podatki/01.01.2017 - 01.01.2019/'

for filename in os.listdir(path):
    tweets.extend(readFiles(path+filename))

#for i in tweets:
#    print(i)

a = PreProcessTweets()
tweets = PreProcessTweets.processTweets(a, tweets)
for i in tweets:
   print(i["text"])
