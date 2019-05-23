echo "[EVE] starting rasa interactive learning"
if [ ! -d "env" ]; then
    python3 -m virtualenv env
fi
echo "[EVE] stopping eve_core container"
docker stop eve-core
source env/bin/activate
echo "[EVE] installing requirements.txt"
pip3 install -r requirements.txt

rasa interactive -m models/20190523-210708.tar.gz --endpoints dev-endpoints.yml