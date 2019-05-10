# Eve Platform
The eve platform is a project that is basically the combination of a smart assistant (chatbot) with an application developed in React Native, in order to monitor the prenatal of pregnant women.

### 1. Eve-mongo
Eve-mongo is a docker container, which contains all the application models. The tracker store of Rasa Core is also here.

#### 1.1 Running

In your root directory (eve-platform), execute the commands below:

```sh
$ cd containers/eve-mongo
$ docker-compose -f mongo-compose.yml up
```
Now you are connected to mongodb://eve_mongo:27017.

#### 1.2 Running MongoDb shell

To run the MongoDb shell, you must enter the mongo docker container and run:


### 1. Eve-Rasa
Eve-Rasa contains all the files and models to run a Rasa Chatbot. We've used Rasa-Core, Rasa-NLU and Rasa-SDK to custom actions.
#### 1.1. Update your Rasa training data in the directory (eve-rasa).
- data/stories.md
- data/nlu.md
- domain.yml

#### 1.2. Train the Rasa NLU Model

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

#### 1.3. Train the Rasa Core Model

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

#### 1.4. Run Rasa Core with Rasa NLU
