FROM python:3.9-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

# Install requirements
RUN pip3 install -r requirements.txt

#Adding proper user
#RUN addgroup --g 1024 groupcontainer
#RUN adduser -u 1024 -G groupcontainer -h /home/containeruser -D containeruser

RUN addgroup --g 1002 sambashare
RUN adduser -u 1001 -G sambashare -h /home/sambauser -D sambauser
USER sambauser