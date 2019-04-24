# EVE-RASA

## Rodando o Rasa NLU

- No diretório raiz do projeto, procure pela pasta ./scripts e execute o script para buildar a imagem do rasa nlu.

- Execute o arquivo build-rasa-nlu-image.bat e aguarde o processo terminar.

- Ainda no diretório scripts, execute o script execute-rasa-nlu.bat para subir o container.

Deverá aparecer no log do container a seguinte frase: "Site starting on 5000".

### HTTP API

- O Rasa NLU está rodando nos containers utilizando uma api, que está configurada na porta :5000 do container. Portanto, algumas requests de interação com o modelo estão disponíveis para utilização.
- Dentro da pasta ./eve-rasa/json, os arquivos .json se referem ao objetos que serão enviados nas requests feitas na API do Rasa. 

#### Treinando o Modelo

- Para treinar o modelo do nlu com novos intents, basta acrescentar no arquivo nlu_train_data.json. Após esse processo, copie o conteúdo desse arquivo e o utilize como parâmetro no body da request (application/json) para o endpoint.

##### WINDOWS
```
http://localhost:5000/train?project=nlu&model=evedefault
```
###### PARÂMETROS
- <b>project</b>: se refere ao nome do projeto que será criado no Rasa NLU. Portanto, nesse container, está configurado o nome <b>nlu</b>.
- <b>model</b>: se refere ao nome do modelo que será gerado após o treinamento. (Esse pode ser determinado, de acordo com o tipo de treinamento)

### Testando o Modelo

- Para testar o modelo nlu, execute a request abaixo com o body do json
