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

RUN addgroup --gid 1002 mygroup
RUN adduser --disabled-password --uid 1001 --ingroup myuser mygroup
USER 1001:1002

RUN whoami