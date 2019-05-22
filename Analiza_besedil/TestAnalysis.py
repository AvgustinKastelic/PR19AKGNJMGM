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
for tweet in tweets:
    sentiment = textBlob.get_txt_sentiment(tweet['text']);
    if(sentiment[0] == tweet['reacton'] and tweet['reacton'] != ""):
        print("correct: " + sentiment[0]+ " original: "+tweet['reacton'])
        correct+=1;
    elif(tweet['reacton'] != ""):
        print("incorrect: "+sentiment[0]+ " original: "+tweet['reacton'])
        incorrect+=1
print("correct: ",correct," incorrect:", incorrect)

'''
pos = 0
neg = 0
neut = 0
i=0
for tweet in tweets:
    if(tweet['reacton'] == "neutral"):
        neut+=1
    elif (tweet['reacton'] == "positive"):
        pos+=1
    elif (tweet['reacton'] == "negative"):
        neg+=1
    elif(tweet['reacton'] == ""):
        continue
    i+=1
print("positive: ",pos,"negative: ",neg," neutral: ",neut)
print(i)
'''
#V podano datoteko zapiše analizirane podake
#with open('AnaliziraniPodatki/01.01.2017 - 01.01.2019/'+fileName, newline='', mode='w',encoding="utf8") as file:
#    file_writer = csv.writer(file, delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
#    file_writer.writerow(['date','retweets','favorites','text','sentiment','polarity','subjectivity'])
#    for tweet in tweets:
#        sentiment = textBlob.get_txt_sentiment(tweet['text'])
#        file_writer.writerow([tweet['date'],tweet['retweets'],tweet["favorites"],tweet["text"],sentiment[0],sentiment[1][0],sentiment[1][1]])
 #   employee_writer.writerow(['John Smith', 'Accounting', 'November'])