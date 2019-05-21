echo "[EVE] Training Rasa Core Model"

docker run --rm -v $(pwd):/app eve-core-nlu python3 -m rasa_core.train -d /app/domain.yml -s /app/data/stories.md -o /app/models/rasa_core