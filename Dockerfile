
FROM node:12

WORKDIR /userapi
COPY /userapi/package.json .

RUN npm install
COPY . .
CMD [ "npm", "start" ]