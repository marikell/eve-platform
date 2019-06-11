echo "[EVE] starting local rasa action server"
if [ ! -d "env" ]; then
    python3 -m virtualenv env
fi
echo "[EVE] stopping eve_actionserver container"
docker stop eve_actionserver
source env/bin/activate
echo "[EVE] installing requirements.txt"
pip3 install -r requirements.txt

python -m rasa_sdk --actions actions --debug