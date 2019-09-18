import pandas as pd
from mongoengine import connect
from answer import Answer
from intent_answer import IntentAnswer
from bson.objectid import ObjectId    
from mongoengine.queryset.visitor import Q
from configuration import MONGO_DEV, MONGO_PROD

connect('evedb', host=MONGO_PROD['HOST'])

df = pd.read_csv('intent.csv')

df.insert(2,"id","")

for i,j in df['answer'].items():
    try:
        existed_answer = Answer.objects.get(Q(text=j))
    except:
        existed_answer = Answer(text=j)
        existed_answer.save()               

    id = ObjectId(existed_answer['id'])
    df.iloc[i, df.columns.get_loc('id')] = id

for i,j in df.iterrows():
    intent = j['intent']
    id = j['id']
    answer = Answer.objects.get(id=id)
    if answer is None:
        print("ERROR AO INSERIR: {}".format(id))
        continue
    intent_answer = IntentAnswer(answer_id=answer.to_dbref(), intent=intent)
    intent_answer.save()

print('Processo finalizado!')  