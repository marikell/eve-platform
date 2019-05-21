# Eve-rasa

These commands below are made to run outside docker container.

### 1. Train NLU Model

```sh
python -m rasa_nlu.train -c config/nlu_config.json --data data/data.json -o models --fixed_model_name nlu --project nlu --verbose
```
### 2. Train Rasa Core Model

```sh
python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue
```

### 3. Chatbot conversation

```sh
python -m rasa_core.run -d models/dialogue --endpoints endpoints.yml
```

### 4. Debugging chatbot conversation

```sh
python -m rasa_core.run -d models/dialogue -u models/nlu/nlu --debug --endpoints endpoints.yml
```

### 5. Activate Action Server

```sh
python -m rasa_core_sdk.endpoint --actions actions.actions
```
### 6. Interactive learning

```sh
python -m rasa_core.train interactive --core models/dialogue --nlu models/nlu/nlu --endpoints endpoints.yml
```
