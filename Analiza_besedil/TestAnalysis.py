import textBlob
import csv
#####
##Prebere twite jih analizira in zapiše v novo csv datoteko z istim imenom v drug direktorij
#####
tweets = []
fileName="fluffypony.csv"
header = 0
with open('podatki/TestAnalysis/'+fileName, newline='',encoding="utf8") as csvfile:
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
                dict["reacton"] = row[5]
                tweets.append(dict)
            except:
                print("exception wrong data type")
        header+=1;
#Zakomentirana koda spodaj je samo za kratko analizo oz. testiranje (koliko je poz, neg, neutr twitov)
correct = 0
incorrect = 0
count = 0
for tweet in tweets:
    sentiment = textBlob.get_txt_sentiment(tweet['text']);
    if(sentiment[0] == tweet['reacton']):
        correct+=1;
    else:
        incorrect+=1
    count+=1
print("correct: ",correct," incorrect:", incorrect, "All test cases:",count)
print("result: ", correct/count)
