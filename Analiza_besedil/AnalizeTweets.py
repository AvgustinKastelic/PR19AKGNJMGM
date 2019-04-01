import textBlob
import csv
#####
##Prebere twite jih analizira in zapiše v novo csv datoteko z istim imenom v drug direktorij
#####
tweets = []
fileName="vitalikbuterin - ETH.csv"
header = 0
with open('podatki/01.01.2017 - 01.01.2019/'+fileName, newline='',encoding="utf8") as csvfile:
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
                dict["geo"] = row[5]
                dict["mentions"] = row[6]
                dict["hashtags"] = row[7]
                dict["id"] = row[8]
                dict["permalinks"] = row[9]
                tweets.append(dict)
            except:
                print("exception wrong data type")
        header+=1;
#Zakomentirana koda spodaj je samo za kratko analizo oz. testiranje (koliko je poz, neg, neutr twitov)
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
with open('AnaliziraniPodatki/01.01.2017 - 01.01.2019/'+fileName, newline='', mode='w',encoding="utf8") as file:
    file_writer = csv.writer(file, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerow(['date','retweets','favorites','text','sentiment','polarity','subjectivity'])
    for tweet in tweets:
        sentiment = textBlob.get_txt_sentiment(tweet['text'])
        file_writer.writerow([tweet['date'],tweet['retweets'],tweet["favorites"],tweet["text"],sentiment[0],sentiment[1][0],sentiment[1][1]])
 #   employee_writer.writerow(['John Smith', 'Accounting', 'November'])