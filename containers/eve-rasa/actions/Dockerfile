FROM python:3.7

WORKDIR /app

COPY ./actions.py .

COPY ./route_config.py .

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# This line will take Heroku's port
# CMD python -m rasa_sdk --port $PORT --actions actions
CMD python -m rasa_sdk --port 5055 --actions actions --debug