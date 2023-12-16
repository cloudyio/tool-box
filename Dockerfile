FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm ci --only=production

RUN npm install

COPY . .

RUN npm run build

EXPOSE 80

CMD ["node", "build/index.js", "--port", "80"]
