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

RUN addgroup --gid 1000 mygroup
RUN adduser --disabled-password --uid 1000 --ingroup mygroup bruno

RUN ps aux

USER 1000:1000