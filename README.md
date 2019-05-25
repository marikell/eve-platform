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
- Now you are connected to mongodb://eve_mongo:27017.

### 1.2 Running MongoDb shell

To run the MongoDb shell, you must enter the mongo docker container and run:

```sh
$ docker exec -it eve_mongo /bin/bash
```
Now, inside the container, run the command below.

```sh
#root mongo
```

- It will appear <i>MongoDB shell version and an available terminal to operate.</i>

### 1.3 Backup

Since we are using a docker container, there are some volumes inside. To do backups, you must execute, in the containers/eve-mongo directory:

```sh
docker run --rm --network evemongo_evenetwork \
--link eve_mongo:mongo -v $(pwd)/backups:/backups \
mongo bash -c "mongodump --out /backups \
--host mongo:27017"
```
- This will generate two backup files and you can go to /container/eve-mongo/backups to get them. If you wish to backup your production database, you can change the host argument and run the command above.

### 1.4 Restore

To restore backups, you must execute, in the containers/eve-mongo directory:

```sh
docker run --rm --network evemongo_evenetwork \
--link eve_mongo:mongo -v $(pwd)/backups:/backups \
mongo bash -c "mongorestore /backups \
--host mongo:27017"
```

- You can run the same command to production database. Just change host argument. 

## 2. Eve-api

Eve-api is the main api of the platform. Through requests, we communicate with basically the entire application. The api that makes the main communication with the database.

### 2.1 Running

In your root directory (eve-platform), execute the commands below:

```sh
$ cd containers/eve-api

$ docker-compose -f api-compose.yml up
```
- Open up URL http://localhost:5001/ and it will appear a message <i>Flask is running in port 5001</i>.

### 2.2 Configuration

If you look inside /eve-api/src/config, you will find a file named database_config.py. In this file, we configure all mongo settings.

| Mongo Database Name | Mongo Uri |
| :---: | :---: |
| evedb  | mongodb://eve_mongo:27017/evedb  |

- If you need to change it, you have to change in this code. Our API is already pointing to the mongo inside docker container, by default. 

## 3. Eve-rasa
Eve-Rasa contains all the files and models to run a Rasa Chatbot. We've used Rasa-Core, Rasa-NLU and Rasa-SDK to custom actions.

### 3.1. Update your Rasa training data in the directory (eve-rasa).

### 3.2. Running in Docker

#### 3.2.1. Building Image

- In this step, we will build docker images and run Rasa containers.

##### 3.2.1.1 Rasa NLU and Rasa Core
If you just cloned our project, you should build our rasa image, so you can run commands inside containers. 

To build our image, go to containers/eve-rasa/core and run the script below

```sh
chmod +x build-rcn.sh
./build-rcn.sh
```
##### 3.2.1.2 Action Server

You should also build Action Server image. To do it, you must run the script below, in containers/eve-rasa/action-server directory.

```sh
chmod +x build-as.sh
./build-as.sh
```

#### 3.2.2 Containers

Now you have built all our images, make sure you have your trained models. If you have not, Rasa Core container will not run. 

Go to containers/eve-rasa and run:
```sh
docker-compose -f rasa-compose.yml up -d
```
Now, our Rasa containers are running and you can check their status using Portainer or running the command below

```sh
docker ps
```
- To make sure everything is working, you can open URL http://localhost:5005 and http://localhost:5055/health. It will appear <i> hello from Rasa: 0.15.0a1</i> (Rasa Core) and <i>status OK</i> (Rasa Action Server).

- Rasa containers communicate with mongo to track and store all bot's conversations.

#### 3.2.3 Script

To do all the steps before, you can run them by a single script. Our <i>start.sh</i> script builds our images and run the containers. 

- Go to containers/eve-rasa and run the commands below

```sh
chmod +x start.sh
./start.sh
```

### 3.2. Train the Rasa NLU Model

Go to /eve-rasa/core directory and run these commands below, so you can run train-nlu.sh script. This step will require our built docker images  .

```
chmod +x train-nlu.sh
./train-nlu.sh
```

### 3.3. Train the Rasa Core Model

Go to /eve-rasa/core directory and run these commands below, so you can run train-core.sh script.

```
chmod +x train-core.sh
./train-core.sh
```

### 3.4. Interactive Learning

You can execute Rasa Interactive Learning, but not inside docker container. Run the script below, and it will run outside our containers. You must know that all Rasa running containers will be stopped.

```
chmod +x train-interactive.sh
./train-interactive.sh
```

### 3.5 Requests

#### 3.5.1 Talking to your bot

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
- This will be stored in Rasa database in our Mongo container. 

### 3.6 Tracker store configuration

If you wish to change mongo's db endpoint, you should insert your new URL in the ./containers/eve-rasa/config/dev-endpoints.yml file. Then, run <b>3.2.2</b> commands.

## Heroku

Heroku is hosting our Eve API, Eve Rasa Action Server and Eve Rasa Core. Basically, to refresh your changes there, you must run the commands below. 

```
heroku login
heroku container:login
heroku container:push web --app <HEROKU_APP_NAME>
heroku container:release web --app <HEROKU_APP_NAME>
```

## Tools

### Portainer

Portainer is a tool to build and manage your Docker environments. 

#### Running

Go to your home directory (not related to your project). And to run Portainer, we will create a docker container, by the command below.

```sh
docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock
-v {USER_SYSTEM_FOLDER}/portainer/data:/data portainer/portainer
```

- Acessing a URL http://localhost:9000 from your browser, it will appear a home screen of Portainer.

### Rasa NLU Trainer

It's a tool to edit your training examples for Rasa NLU.

#### Running

Go to {PROJECT_DIRECTORY}/containers/eve-rasa/data/json (NLU data directory). And to run Rasa NLU Trainer, we will create a docker container, by executing the code below.

```sh
docker run -t --name rasa-nlu-trainer -v $(pwd):/rasa-nlu-trainer/src/state -p 5006:8080 -i \
dominicbreuker/rasa-nlu-trainer
```

- This will search for the first .json file in the folder. Now, acessing a URL http://localhost:5006 from your browser, it will appear your formatted NLU json to edit. 
