FROM rasa/rasa:latest-full

WORKDIR /app

# RUN pip install rasa

ADD ./models /app/models
COPY ./endpoints.yml /app/
# ADD ./data .
# ADD ./domain.yml .

# CMD run -m models/20190522-023305.tar.gz --endpoints endpoints.yml -p 5005 --enable-api
CMD run -m models/20190522-023305.tar.gz --endpoints endpoints.yml --enable-api --debug
CMD ["run","-m","models/20190522-023305.tar.gz","--endpoints","endpoints.yml","-p","5005","--enable-api","--debug"]