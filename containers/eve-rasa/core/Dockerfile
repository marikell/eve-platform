FROM python:3.7

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN python3 -m spacy download en

ADD ./models /app/models/
ADD ./config /app/config/
ADD ./data /app/data
COPY /domain.yml .

CMD python3 -m rasa_core.run --enable_api --core /app/models/rasa_core -u /app/models/rasa_nlu/current/nlu --endpoints /app/config/dev-endpoints.yml --credentials /app/config/credentials.yml -p 5005 --debug