echo "[EVE] Training Rasa NLU Model"

docker run --rm -v $(pwd):/app eve-core-nlu python3 -m rasa_nlu.train -c /app/config/nlu_config.yml -d /app/data/json/nlu.json --fixed_model_name nlu -o /app/models/rasa_nlu --project current