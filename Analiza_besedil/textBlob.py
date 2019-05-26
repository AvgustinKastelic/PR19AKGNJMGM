from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
#####
##Tukaj se uporablja textblob za analizo besedil
#####

def get_txt_sentiment(txt):
    # create TextBlob object of passed tweet text
    analysis = TextBlob(txt)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return ['positive', analysis.sentiment]
    elif analysis.sentiment.polarity == 0:
        return ['neutral', analysis.sentiment]
    else:
        return ['negative', analysis.sentiment]

def get_txt_sentiment_bayes(txt):
    # create TextBlob object of passed tweet text
    analysis = TextBlob(txt, analyzer=NaiveBayesAnalyzer())
    # set sentiment //adding neutral
    if(analysis.sentiment.p_pos >= 0.30 and analysis.sentiment.p_neg >= 0.30):
        return(["neutral"])
    elif(analysis.sentiment.classification == "pos"):
        return (["positive"])
    else:
        return (["negative"])

#a = "# Binance by-the-numbers: 151 coins listed 396 trading pairs 731 days of content @ BinanceAcademy 30K tokens supported @ TrustWalletApp 3M+ tokens retrieved for users 8.5M+ PV @ Binance_Info 10M+ users worldwide Highlights on what we accomplished in 2018! https://www.binance.com/en/blog/286445971261435904 …pic.twitter.com/BZdClcORBV"
#print(get_txt_sentiment_bayes(a))
#blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
#print(blob.sentiment)
#Zakomentirana koda spodaj je samo prikaz uspešnosti textBloba
'''txt = "Nice job btc"
print(txt, " : ", get_txt_sentiment(txt))
txt = "Nice job btc :("
print(txt, " : ", get_txt_sentiment(txt))
txt = "The price of bitcoin just fell under 3k"
print(txt, " : ", get_txt_sentiment(txt))
txt = "YES! The price of bitcoin just fell under 3k"
print(txt, " : ", get_txt_sentiment(txt))
txt = "woa getting rich, BTC to the moon"
print(txt, " : ", get_txt_sentiment(txt))
txt = "I lost all my money with btc"
print(txt, " : ", get_txt_sentiment(txt))
txt = "I hate fried chicken"
print(txt, " : ", get_txt_sentiment(txt))
txt = "Mexico must use its very strong immigration laws to stop the many thousands of people trying to get into the USA. Our detention areas are maxed out & we will take no more illegals. Next step is to close the Border! This will also help us with stopping the Drug flow from Mexico!"
print(txt, " : ", get_txt_sentiment(txt))'''