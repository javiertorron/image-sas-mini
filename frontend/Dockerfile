FROM node:14-alpine as build

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:1.19-alpine

COPY --from=build /app/dist/frontend /usr/share/nginx/html
EXPOSE 4000

CMD ["nginx", "-g", "daemon off;"]
