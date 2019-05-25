echo "[EVE] training rasa model"

docker run --rm -v $(pwd):/app rasa/rasa:latest-full train --domain domain.yml --data data --fixed-model-name core --out models