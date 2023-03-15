FROM python:3.11-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/src"

ARG ARG_PCLOUD_USER=default
ARG ARG_PCLOUD_PASS=default

ENV PCLOUD_USER=$ARG_PCLOUD_USER
ENV PCLOUD_USER=$ARG_PCLOUD_PASS

# Install requirements
RUN pip3 install -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity