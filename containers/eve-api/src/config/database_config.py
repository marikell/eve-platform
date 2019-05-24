#NEVER COMMIT THIS FILE WITH TRUE CREDENTIALS

DEV_MONGO_CONFIGURATION = {
    'DATABASE_NAME': 'evedb',
    'DATABASE_URL': 'mongodb://eve_mongo:27017/evedb'
}

PROD_MONGO_CONFIGURATION ={
    'DATABASE_NAME': 'evedb',
    'DATABASE_URL': 'mongodb://admin:eve2019@evecluster-shard-00-00-90nlz.mongodb.net:27017,evecluster-shard-00-01-90nlz.mongodb.net:27017,evecluster-shard-00-02-90nlz.mongodb.net:27017/evedb?ssl=true&replicaSet=EveCluster-shard-0&authSource=admin&retryWrites=true'
}