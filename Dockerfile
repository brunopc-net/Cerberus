FROM python:3.9-slim-bullseye

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

# Install requirements
RUN pip3 install -r requirements.txt

#Adding proper user

RUN whoami

RUN addgroup --gid 114 mygroup
RUN adduser --disabled-password --uid 110 --ingroup mygroup myuser
USER 114:110

RUN whoami