FROM python:3.11-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/src"

ARG PCLOUD_USER=default
ENV PCLOUD_USER=$PCLOUD_USER

# Install requirements
RUN pip3 install -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity