FROM python:3.7

WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt

ADD ./actions /app/actions/
ADD ./api /app/api

CMD python3 -m rasa_core_sdk.endpoint --actions actions.actions --port 5055 --cors '*'