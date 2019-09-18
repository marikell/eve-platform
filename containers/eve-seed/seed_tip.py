import pandas as pd
import pymongo
from bson.objectid import ObjectId    
from enums import TipTypeEnum
from configuration import MONGO_DEV, MONGO_PROD

def main():
    try:
        client = pymongo.MongoClient(MONGO_PROD['HOST'])
        db = client['evedb']
        tip_col = db['tip']

        df = pd.read_csv('tip-birth.csv')       
        
        tip_type = int(TipTypeEnum.after_birth)

        tips = []

        for idx, obj in df.iterrows():
            description = obj['dica']

            if not description:
                continue

            tip = {
                "description" : description,
                "tip_type" : tip_type,
                "send" : False
            }          

            tips.append(tip)
        
        # print(tips)
        x = tip_col.insert_many(tips)

        print('Foram inseridos {} objetos.'.format(len(tips)))
        

    except Exception as e:
        print('[Exception] {}'.format(str(e)))


if __name__ == "__main__":
    main()