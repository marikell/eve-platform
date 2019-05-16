# Eve Platform
The eve platform is a project that is basically the combination of a smart assistant (chatbot) with an application developed in React Native, in order to monitor the prenatal of pregnant women.

## 1. Eve-mongo
Eve-mongo is a docker container, which contains all the application models. The tracker store of Rasa Core is also here.

### 1.1 Running

In your root directory (eve-platform), execute the commands below:

```sh
$ cd containers/eve-mongo
$ docker-compose -f mongo-compose.yml up -d
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
docker run --rm --network evemongo_evenetwork \
--link eve_mongo:mongo -v $(pwd)/backups:/backups \
mongo bash -c "mongodump --out /backups \
--host mongo:27017"
```
This will generate two backup files and you can go to /container/eve-mongo/backups to get them. 

### 1.4 Restore

To restore backups, you must execute, in the containers/eve-mongo directory:

```sh
docker run --rm --network evemongo_evenetwork \
--link eve_mongo:mongo -v $(pwd)/backups:/backups \
mongo bash -c "mongorestore /backups \
--host mongo:27017"
```
## 2. Eve-app

The idea of the application is to answer common questions about pregnancy, remind your users of important exams to be done, during pregnancy, to provide health.

### 2.1 Running

In your root directory (eve-platform), execute the commands below:

```sh
$ cd containers/eve-app

$ docker build -t eve-app-image .

$ docker run -d -p 19000:19000 -p 19001:19001 -p 19002:19002 -v $(pwd):/app \ 
--name eve_app eve-app-image
```
If you wish the docker container runs in the background, keep the <i>-d</i> option. Otherwise, remove it.

Open up URL http://localhost:19002 and change the network type to tunnel. This will generate a QR Code, which will be used to open the app into Expo (Playstore App). Open <i><b>Expo</b></i> in your device and press the option to scan QR Code, and scan your app QR Code. 

If you change anything in your app, it will be built inside docker container and refreshed.

## 3. Eve-api

Eve-api is the main api of the platform. Through requests, we communicate with basically the entire application. The api that makes the main communication with the database.

### 3.1 Running

In your root directory (eve-platform), execute the commands below:

```sh
$ cd containers/eve-api

$ docker-compose -f api-compose.yml up
```
Open up URL http://localhost:5001/ and it will appear a message <i>Flask is running in port 5001</i>.

### 3.2 Configuration

If you look inside /eve-api/src/config, you will find a file named database_config.py. In this file, we configure all mongo settings.

| Mongo Database Name | Mongo Uri |
| :---: | :---: |
| evedb  | mongodb://eve_mongo:27017/evedb  |

If you need to change it, you have to change in this code. Our API is already pointing to the mongo inside docker container, by default. 

## 4. Eve-rasa
Eve-Rasa contains all the files and models to run a Rasa Chatbot. We've used Rasa-Core, Rasa-NLU and Rasa-SDK to custom actions.
### 4.1. Update your Rasa training data in the directory (eve-rasa).

### 4.2. Train the Rasa NLU Model

Go to /eve-rasa directory and run these commands below.

```sh
docker run --rm --network evemongo_evenetwork -v $(pwd):/app/project -v $(pwd)/models/rasa_nlu:/app/models rasa/rasa_nlu:latest-tensorflow run python -m rasa_nlu.train -c project/config/nlu_config.yml -d project/data/json/nlu.json -o models --fixed_model_name nlu --project current --verbose
```

### 4.3. Train the Rasa Core Model

Go to /eve-rasa directory and run these commands below.

```sh
docker run --rm --network evemongo_evenetwork -v $(pwd):/app/project -v $(pwd)/models/rasa_core:/app/models rasa/rasa_core:latest train --domain project/domain.yml --stories project/data/stories.md --out models --verbose
```

### 4.4. Run Rasa Core with Rasa NLU

To run all docker containers related to Rasa (eve_rasa_nlu, eve_action_server, eve_rasa_core), we will use a compose file. Go to {PROJECT_DIRECTORY}/containers/eve-rasa and run this command:

```sh
docker-compose -f rasa-compose.yml up -d
```
Now, all Rasa containers are running and you can see each container status using Portainer or running the command below

```sh
docker ps
```
To make sure your rasa API is working, you can open URL http://localhost:5005 and http://localhost:5000. It will appear <i> hello from Rasa: 0.15.0a1</i> (Rasa Core) and <i>hello from Rasa NLU: 0.15.0a1</i> (Rasa NLU).

Rasa containers communicate with mongo to track and store all bot's conversations.

### 4.5 Requests

#### 4.5.1 Talking to your bot

You can talk with your bot by sending POST requests with some parameters to URL http://localhost:5005/webhooks/rest/webhook.

Open a tool called <i><b>Postman</b></i> or your can use curl to do it. Your JSON example data is below, which you can send a message, with the sender (user_id). 

```json
{
    "message": "Hello",
    "sender":"1"
}
```
This will return a bot response, like shown below.

```json
[
    {
        "recipient_id": "10",
        "text": "Hello!"
    }
]
```
This will be stored in Rasa database in our Mongo container. 
### 4.6 Tracker store configuration

If you wish to change mongo's db endpoint, you should insert your new URL in the ./containers/eve-rasa/config/endpoints.yml file. Then, run <b>4.4</b> commands.

## Tools

### Portainer

Portainer is a tool to build and manage your Docker environments. 

#### Running

Go to your home directory (not related to your project). And to run Portainer, we will create a docker container, by the command below.

```sh
docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock
-v {USER_SYSTEM_FOLDER}/portainer/data:/data portainer/portainer
```

Acessing a URL http://localhost:9000 from your browser, it will appear a home screen of Portainer.

### Rasa NLU Trainer

It's a tool to edit your training examples for Rasa NLU.

#### Running

Go to {PROJECT_DIRECTORY}/containers/eve-rasa/data/json (NLU data directory). And to run Rasa NLU Trainer, we will create a docker container, by executing the code below.

```sh
docker run -t --name rasa-nlu-trainer -v $(pwd):/rasa-nlu-trainer/src/state -p 5006:8080 -i \
dominicbreuker/rasa-nlu-trainer
```

This will search for the first .json file in the folder. Now, acessing a URL http://localhost:5006 from your browser, it will appear your formatted NLU json to edit. 
