FROM python:3.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV TZ=America/Sao_Paulo

ENV RUN_TIME="13:20"

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["python", "run.py"]