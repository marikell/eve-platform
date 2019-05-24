FROM python:3.7

WORKDIR /app

RUN pip install rasa

ADD ./models /app/models
COPY ./endpoints.yml .
COPY ./dev-endpoints.yml .

# This line will take Heroku's port and Heroku's Action Server
# CMD rasa run -m models/core.tar.gz --endpoints endpoints.yml -p $PORT --enable-api
CMD rasa run -m models/core.tar.gz --endpoints dev-endpoints.yml -p 5005 --enable-api --debug