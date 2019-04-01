from textblob import TextBlob
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