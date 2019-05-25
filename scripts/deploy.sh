#!/bin/bash

while true; do
    read -p "Deploy no diretório $PWD. Deseja continuar? (y/n)  " yn
    case $yn in
        [Yy]* ) 
        
        heroku login
        heroku container:login

        if [ -f "$PWD/Dockerfile" ]
        then
            
            read -p "Nome do app no heroku: " app

            heroku container:push web --app $app
            heroku container:release web --app $app

        else
            echo "Arquivo dockerfile não encontrado."
        fi
        
        break;;
        [Nn]* ) exit;;
        * ) echo "Apenas y/n são aceitos como resposta.";;
    esac
done