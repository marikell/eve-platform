FROM python:3.7

WORKDIR /app

COPY ./actions.py .

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD python -m rasa_sdk --port $PORT --actions actions