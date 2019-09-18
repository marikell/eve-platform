import pandas as pd
from mongoengine import connect
from answer import Answer
from intent_answer import IntentAnswer
from bson.objectid import ObjectId    
from mongoengine.queryset.visitor import Q

# connect('evedb', host='mongodb://admin:eve2019@evecluster-shard-00-00-90nlz.mongodb.net:27017,evecluster-shard-00-01-90nlz.mongodb.net:27017,evecluster-shard-00-02-90nlz.mongodb.net:27017/evedb?ssl=true&replicaSet=EveCluster-shard-0&authSource=admin&retryWrites=true')
connect('evedb', host='mongodb://localhost:27017')

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