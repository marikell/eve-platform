FROM python:3.7

WORKDIR /app

RUN pip install rasa

ADD ./models .
COPY ./endpoints.yml .

CMD rasa run -m models/20190522-023305.tar.gz --endpoints endpoints.yml -p 5005 --enable-api 
# ADD ./data .
# ADD ./domain.yml .

# CMD run -m models/20190522-023305.tar.gz --endpoints endpoints.yml -p 5005 --enable-api
# CMD rasa run -m models/20190522-023305.tar.gz --endpoints endpoints.yml -p 5005 --enable-api --debug
#funciona
# CMD ["run","-m","models/20190522-023305.tar.gz","--endpoints","endpoints.yml","-p","5005","--enable-api","--debug"]