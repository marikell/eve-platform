Write-host "EVE-APP: Execution" -ForegroundColor Yellow 
echo "[EXECUTION] Executando o projeto: eve-app"

echo "[DOCKER] Entrando no container"

docker exec -it eve-app-container sh

echo "[YARN] Instalando as dependências"
yarn install
echo "[YARN] Iniciando o projeto"
yarn start

echo "Aperte qualquer tecla para sair...";
cmd /c pause | out-null