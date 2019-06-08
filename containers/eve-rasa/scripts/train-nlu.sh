echo "[EVE] training rasa nlu model"

docker run --rm -v $(pwd):/app rasa/rasa:latest-full train nlu -c config.yml