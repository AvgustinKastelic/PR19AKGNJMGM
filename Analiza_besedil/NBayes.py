import os
import re
import csv
import nltk
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords



#####
### "Ročno" zgrajen Naivni Bayes klasifikator z uporabo prosto dostopne učne množice iz projekta Sentiment140
### Ta programska datoteka ja nadaljevanje programske datoteke AnalizeTweets.py
#####



# Razred za predprocesiranje tweetov - odstranjevanje nepotrebnih besed ipd. iz besedila
class PreProcessTweets:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    def process_tweets(self, tweets_list):
        processed_tweets = []
        for tweet in tweets_list:
            processed_tweets.append((self._process_tweet(tweet["text"]), "undef"))
        return processed_tweets

    # ločena funkcija za učne podatke, saj jih iz datoteke preberemo na nekoliko drugačen način
    def process_training_data(self, train_data):
        processed_data = []
        for text in train_data:
            processed_data.append((self._process_tweet(text), train_data[text]))
        return processed_data

    # odstrani irelevantne znake iz besedila
    def _process_tweet(self, tweet):
        tweet = tweet.lower()  # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]



# funkcija za branje tweetov iz naših datotek; izvorna datoteka te funkcije je AnalizeTweets.py
def read_files(path):
    tweets = []
    header = 0
    with open(path, newline='',encoding="utf8") as csvfile:
        reader = csv.reader(csvfile,delimiter=';')
        for row in reader:
            if header != 0:
                tweet_dict = {}
                #username;date;retweets;favorites;text;geo;mentions;hashtags;id;permalink
                try:
                    tweet_dict["date"] = row[1]
                    tweet_dict["retweets"] = row[2]
                    tweet_dict["favorites"] = row[3]
                    tweet_dict["text"] = row[4]
                    tweet_dict["geo"] = row[5]
                    tweet_dict["mentions"] = row[6]
                    tweet_dict["hashtags"] = row[7]
                    tweet_dict["id"] = row[8]
                    tweet_dict["permalinks"] = row[9]
                    tweets.append(tweet_dict)
                except:
                    print("exception wrong data type")
                    # dodan izpis vrstice, kjer se zgodi morebitna izjema, da se lahko preveri zakaj do nje pride
                    print("At row:")
                    print(row)

            header+=1
    return tweets


# prebere učne podatke, "skip" argument se uporabi, če hočemo prebrati manj vrstic, kot jih ima datoteka,
# saj je vseh vrstic 1.600.000, kar pa bi bila prevelika učna množica in bi učenje ter klasifikacija trajala predolgo
def read_training_data(path, skip=0):
    data = {}
    with open(path, newline="", encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for row in reader:
            for i in range(skip):
                try:
                    next(reader)
                except:
                    break
            label = ""
            field1 = row[0] # Sentiment140: field 1 == polarity -> 0/2/4 -> neg/neu/pos, učna množica brez neu vrstic
            if field1 == "0":
                label = "neg"
            elif field1 == "4":
                label = "pos"
            data[row[-1]] = label # Sentiment140: last field == tweet text

    return data


# funkcija za gradnjo t.i. "slovarja" vseh besed, ki jih vsebuje učna množica
def build_vocabulary(train_data):
    all_words = []

    for words in train_data:
        all_words.extend(words[0])

    wordlist = nltk.FreqDist(all_words)

    return wordlist.keys()


# funkcija za pridobivanje lastnosti tweetov - podatek za vsako besedo iz slovarja, če jo tweet vsebuje
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features


# zapis obstoječih podatkov in dodatno pridobljena podatka - verjetnosti pozitivno/negativno, ki se seštejata v 1
def write_to_file(filename, index):
    with open('NB_AnaliziraniPodatki/01.01.2017 - 01.01.2019/'+filename, newline='', mode='w',encoding="utf8") as file:
        file_writer = csv.writer(file, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(['date','retweets','favorites','text','geo','mentions','hashtags','id','permalink',
                              'positive','negative'])
        i = 0
        for tweet in all_tweets[index]:
            pos = NBResultLabels[index][i].prob("pos")
            neg = NBResultLabels[index][i].prob("neg")
            file_writer.writerow([tweet['date'],tweet['retweets'],tweet['favorites'],tweet['text'],tweet['geo'],
                                  tweet['mentions'],tweet['hashtags'],tweet['id'],tweet['permalinks'],pos,neg])
            i += 1



# branje podatkov za učno množico
train_tweets = read_training_data("podatki/train_Sentiment140.csv", skip=360)

# branje vseh datotek s tweeti, ki jih želimo analizirati
all_tweets = []
data_path = 'podatki/01.01.2017 - 01.01.2019/'
for fname in os.listdir(data_path):
    all_tweets.append(read_files(data_path + fname))

# učna množica in podatki za analizo
a = PreProcessTweets()
train_set = a.process_training_data(train_tweets)
tweet_data = [a.process_tweets(tweet_list) for tweet_list in all_tweets]

# slovar vseh besed
word_features = build_vocabulary(train_set)

# lastnosti, pridobljene iz učne množice, uporabljanje za učenje klasifikatorja
training_features = nltk.classify.apply_features(extract_features, train_set)

# učenje klasifikatorja
NBayesClassifier = nltk.NaiveBayesClassifier.train(training_features)

# seznam, ki vsebuje sezname ocen tweetov iz posamezne datoteke
NBResultLabels = [[NBayesClassifier.prob_classify(extract_features(tweet[0]))for tweet in t_set] for t_set in tweet_data]



# zapis pridobljenih podatkov v nove datoteke
# uporabljena imena originalnih datotek (z neanaliziranimi podatki), indeksi v naprej določeni pri branju datotek
write_to_file("aantonop.csv", 0)
write_to_file("binance.csv", 1)
write_to_file("BittrexExchange.csv", 2)
write_to_file("coinbase.csv", 3)
write_to_file("fluffypony.csv", 4)
write_to_file("justinsuntron - TRX.csv", 5)
write_to_file("lopp.csv", 6)
write_to_file("SatoshiLite - LTC.csv", 7)
write_to_file("vitalikbuterin - ETH.csv", 8)