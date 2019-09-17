FROM python:3.7

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ADD ./models /app/models
ADD ./actions /app/actions
COPY ./endpoints.yml .
COPY ./dev-endpoints /app/dev-endpoints

# This line will take Heroku's port and Heroku's Action Server
# CMD rasa run -m models/core.tar.gz --endpoints endpoints.yml -p $PORT --enable-api --debug
CMD rasa run -m models/core.tar.gz --endpoints dev-endpoints/docker-endpoints.yml -p 5005 --enable-api --debug