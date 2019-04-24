echo "EVE-RASA-NLU: Docker Image Build"
echo "Criando a imagem (eve-rasa-nlu-image)..."
cd ..
cd ./containers/eve-rasa/docker/rasa-nlu
docker build -t eve-rasa-nlu-image .
PAUSE