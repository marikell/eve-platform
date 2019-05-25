echo "[EVE] starting local Rasa X"
echo "Confira se o arquivo endpoints.yml está com as configurações desejadas."
if [ ! -d "env" ]; then
    python3 -m virtualenv env
fi
docker stop eve_core
source env/bin/activate
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
rasa x --endpoints ./dev-endpoints/local-endpoints.yml