echo "[EVE] Starting Rasa Action Server"
if [ ! -d "env" ]; then
    python3 -m virtualenv env
fi
echo "[EVE] Stopping eve_action_server container"
docker stop eve_action_server
source env/bin/activate
echo "[EVE] Installing requirements.txt"
pip3 install -r requirements.txt

python -m rasa_core_sdk.endpoint --actions actions.actions