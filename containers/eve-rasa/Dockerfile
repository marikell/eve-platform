FROM rasa/rasa:latest-full

WORKDIR /app

ADD ./models /app/models/
ADD ./data /app/data
COPY /domain.yml .
COPY /endpoints.yml .

CMD python3 -m rasa_core.run --enable_api --core /app/models/rasa_core -u /app/models/rasa_nlu/current/nlu --endpoints /app/config/dev-endpoints.yml --credentials /app/config/credentials.yml -p 5005 --debug