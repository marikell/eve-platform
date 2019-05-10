# Eve Platform
The eve platform is a project that is basically the combination of a smart assistant (chatbot) with an application developed in React Native, in order to monitor the prenatal of pregnant women.

## 1. Eve-mongo
Eve-mongo is a docker container, which contains all the application models. The tracker store of Rasa Core is also here.

### 1.1 Running

In your root directory (eve-platform), execute the commands below:

```sh
$ cd containers/eve-mongo
$ docker-compose -f mongo-compose.yml up
```
Now you are connected to mongodb://eve_mongo:27017.

### 1.2 Running MongoDb shell

To run the MongoDb shell, you must enter the mongo docker container and run:

```sh
$ docker exec -it eve_mongo /bin/bash
```
Now, inside the container, run the command below.

```sh
#root mongo
```

It will appear <i>MongoDB shell version and an available terminal to operate.</i>

### 1.3 Backup

Since we are using a docker container, there are some volumes inside. To do backups, you must execute, in the containers/eve-mongo directory:

```sh
docker run --rm --network evemongo_evenetwork --link eve_mongo:mongo -v $(pwd)/backups:/backups mongo bash -c "mongodump --out /backups --host mongo:27017"
```
This will generate two backup files and you can go to /container/eve-mongo/backups to get them. 

### 1.4 Restore

To restore backups, you must execute, in the containers/eve-mongo directory:

```sh
docker run --rm --network evemongo_evenetwork --link eve_mongo:mongo -v $(pwd)/backups:/backups mongo bash -c "mongorestore /backups --host mongo:27017"
```
## 2. Eve-Rasa
Eve-Rasa contains all the files and models to run a Rasa Chatbot. We've used Rasa-Core, Rasa-NLU and Rasa-SDK to custom actions.
### 2.1. Update your Rasa training data in the directory (eve-rasa).

### 2.2. Train the Rasa NLU Model

Go to /eve-rasa directory and run these commands below.

```
docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_nlu:/app/models \
  rasa/rasa_nlu:latest-tensorflow \
  run \
    python -m rasa_nlu.train \
    -c config/nlu_config.yml \
    -d project/data/json/nlu.json \
    -o models \
    --fixed_model_name nlu \
    --project current \
    --verbose
```

### 2.3. Train the Rasa Core Model

Go to /eve-rasa directory and run these commands below.

```
docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_core:/app/models \
  rasa/rasa_core:latest \
  train \
    --domain project/domain.yml \
    --stories project/data/stories.md \
    --out models
```

### 2.4. Run Rasa Core with Rasa NLU

To run all docker containers related to Rasa (eve_rasa_nlu, eve_action_server, eve_rasa_core), we will use a compose file. Go to {PROJECT_DIRECTORY}/containers/eve-rasa and run this command:

```sh
docker-compose -f rasa-compose.yml up
```
Now, all Rasa containers are running and you can see each container status using Portainer or running the command below

```sh
docker ps
```

Rasa containers communicate with mongo to track and store all bot's conversations.

### 2.5 Requests


## Tools

### Portainer

Portainer is a tool to build and manage your Docker environments. 

#### Running

Go to your home directory (not related to your project). And to run Portainer, we will create a docker container, by the command below.

```sh
docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock \
-v {USER_SYSTEM_FOLDER}/portainer/data:/data portainer/portainer
```

Acessing a URL http://localhost:9000 from your browser, it will appear a home screen of Portainer.
