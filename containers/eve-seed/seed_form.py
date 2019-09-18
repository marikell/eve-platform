import pandas as pd
import pymongo
from bson.objectid import ObjectId    
from enums import TipTypeEnum

def main():
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017')
        # client = pymongo.MongoClient('mongodb://admin:eve2019@evecluster-shard-00-00-90nlz.mongodb.net:27017,evecluster-shard-00-01-90nlz.mongodb.net:27017,evecluster-shard-00-02-90nlz.mongodb.net:27017/evedb?ssl=true&replicaSet=EveCluster-shard-0&authSource=admin&retryWrites=true')
        db = client['evedb']
        tip_col = db['form']

        df = pd.read_csv('form.csv')       

        objs = []

        for idx, obj in df.iterrows():
            name = obj['name']

            if not name:
                continue

            ent = {
                "name" : name
            }

            objs.append(ent)
        
        # print(tips)
        x = tip_col.insert_many(objs)

        print('Foram inseridos {} objetos.'.format(len(objs)))
        

    except Exception as e:
        print('[Exception] {}'.format(str(e)))


if __name__ == "__main__":
    main()