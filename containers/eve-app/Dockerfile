FROM node:latest

WORKDIR /src/app

RUN echo "fs.inotify.max_user_watches=524288" >> /etc/sysctl.conf

COPY app.json package*.json ./

COPY . .

RUN npm install

EXPOSE 19000
EXPOSE 19001
EXPOSE 19002

CMD [ "npm", "start" ]

