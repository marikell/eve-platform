Write-host "EVE-APP: Build" -ForegroundColor Yellow 
echo "Subindo os containers (eve-app)..."

cd ..
cd ./containers/eve-app
echo "[DOCKER] Criando a imagem eve-app-image"
docker build -t eve-app-image .
cd ..
echo "[DOCKER] Criando o container eve-app"
docker-compose up -d

& .\execute-eve-app.ps1

echo "Aperte qualquer tecla para sair...";
cmd /c pause | out-null