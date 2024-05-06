# Build step 1(Installing node modules and preparing compiled build)
From node:lts-alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
RUN npm i --silent
COPY . ./
# ENV REACT_APP_HOST_IP_ADDRESS
RUN npm run build

# BUILD step 2(Deploying build on NGINX)
FROM nginx:1.21
RUN apt-get update \
    && apt-get install -y wget \
    && rm -rf /var/lib/apt/lists/*
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf:ro
COPY --from=build /app/dist /usr/share/nginx/html