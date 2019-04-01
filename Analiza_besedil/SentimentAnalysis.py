from monkeylearn import MonkeyLearn
#####
##Monkey learn za analizo texta (NEUPORABLJENO - LAHKO KOT TEST)
#####
#na spletni strani se lahko tudi naloži csv pa analizira na sami spletni strani
#omejitev 300 queryev / mesec
#input token (trenutno moj token):
ml = MonkeyLearn('6d7e6d694ed5ed2c3cbb097a568b8b8e4125e0f1')
data = ["This video sucks","Wow i like this", "nice job", "I ate a sandwich"]
model_id = 'cl_pi3C7JiL'
#result = ml.classifiers.classify(model_id, data)

'''text = result.body[0]['text']
external_id = result.body[0]['external_id']
error = result.body[0]['error']
classification = result.body[0]['classifications']
########
#Classification result (tag):
########
tag_name = classification[0]['tag_name']
tag_id = classification[0]['tag_id']
confidence = classification[0]['confidence']'''
#print(result.body)
