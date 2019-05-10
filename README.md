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

### 1.3 Backup from Volume

Since we are using a docker container, there are some volumes inside. To do backups, you must enter inside the container (step 1.2) and execute:

```sh
#root cd backups
#root mongodump --db rasa 
#root mongodump --db eveDb
```

This will generate two backup files and you can go to /container/eve-mongo/backups to get them. 

## 2. Eve-Rasa
Eve-Rasa contains all the files and models to run a Rasa Chatbot. We've used Rasa-Core, Rasa-NLU and Rasa-SDK to custom actions.
### 2.1. Update your Rasa training data in the directory (eve-rasa).
- data/stories.md
- data/nlu.md
- domain.yml

### 2.2. Train the Rasa NLU Model

```
docker run \
  -v $(pwd):/app/project \
  -v $(pwd)/models/rasa_nlu:/app/models \
  rasa/rasa_nlu:latest-tensorflow \
  run \
    python -m rasa_nlu.train \
    -c config.yml \
    -d project/data/nlu.md \
    -o models \
    --project current
```

### 2.3. Train the Rasa Core Model

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


## Tools

### Portainer

Portainer is a tool to build and manage your Docker environments. 

#### Running

Go to your home directory (not related to your project). And to run Portainer, we will create a docker container, by the command below.

```sh
docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock \
-v /home/{USER_SYSTEM_FOLDER}/portainer/data:/data portainer/portainer
```

Acessing a URL http://localhost:9000 from your browser, it will appear a home screen of Portainer.

### Rasa NLU Trainer

It's a tool to edit your training examples for Rasa NLU.

Go to {PROJECT_DIRECTORY}/containers/eve-rasa/data (NLU data directory). And to run Rasa NLU Trainer, we will create a docker container, by executing the code below.

```sh
docker run -p 8080:8080 -v $(pwd):/app --name rasanlutrainer dominicbreuker/rasa-nlu-trainer
```

This will search for the first .json file in the folder. Now, acessing a URL http://localhost:8080 from your browser, it will appear your formatted NLU json to edit. 





