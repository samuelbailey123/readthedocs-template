FROM nikolaik/python-nodejs:latest
WORKDIR /app
COPY . .
RUN npm install --global http-server
RUN pip install -r requirements.txt
EXPOSE 8080
CMD [ "make", "all" ]
