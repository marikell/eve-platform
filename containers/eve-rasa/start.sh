echo "[EVE] Creating Rasa Core NLU image"
docker build -t eve-core-nlu ./core
echo "[EVE] Creating Rasa Action Server"
docker build -t eve-action-server ./action-server
echo "[EVE] Starting local containers"
docker-compose -f rasa-compose.yml up -d
