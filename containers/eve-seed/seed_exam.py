import pandas as pd
import pymongo
from bson.objectid import ObjectId    
from enums import TipTypeEnum
from configuration import MONGO_DEV,MONGO_PROD

def main():
    try:
        client = pymongo.MongoClient(MONGO_PROD['HOST'])
        db = client['evedb']
        tip_col = db['exam']

        df = pd.read_csv('exams.csv')       

        exams = []

        for idx, obj in df.iterrows():
            description = obj['description']
            name = obj['name']
            trimester = int(obj['trimester'])

            if not description or not name or not trimester:
                continue

            exm = {
                "description" : description,
                "name" : name,
                "trimester" : trimester
            }          

            exams.append(exm)
        
        # print(tips)
        x = tip_col.insert_many(exams)

        print('Foram inseridos {} objetos.'.format(len(exams)))
        

    except Exception as e:
        print('[Exception] {}'.format(str(e)))


if __name__ == "__main__":
    main()