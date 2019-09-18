import pandas as pd
import pymongo
from bson.objectid import ObjectId    
from enums import TipTypeEnum
from configuration import MONGO_DEV,MONGO_PROD

def main():
    try:
        client = pymongo.MongoClient(MONGO_PROD['HOST'])
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