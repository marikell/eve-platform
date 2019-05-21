echo "[EVE] Starting Rasa Core Interactive Learning"
if [ ! -d "env" ]; then
    python3 -m virtualenv env
fi
echo "[EVE] Stopping eve_nlu_core container"
docker stop eve_nlu_core
source env/bin/activate
echo "[EVE] Installing requirements.txt"
pip3 install -r requirements.txt

python -m rasa_core.train interactive --core models/rasa_core --nlu models/rasa_nlu/current/nlu --endpoints config/dev-endpoints.yml