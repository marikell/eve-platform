echo "[EVE] creating eve core image"
docker build -t evecoreimage .
echo "[EVE] creating eve action server image"
docker build -t eveactionimage ./actions
echo "[EVE] starting local containers"
docker-compose -f rasa-compose.yml up -d