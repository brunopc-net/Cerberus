FROM python:3.9-alpine

# Defining the Author
MAINTAINER Bruno PC

VOLUME /home/bruno

#Create a working directory
WORKDIR /app

# Install requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Add the source code into the image
COPY . .