FROM python:3.11-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/src"
ENV username=${PCLOUD_CREDENTIALS_USR}
ENV password=${PCLOUD_CREDENTIALS_PWD}

# Install requirements
RUN pip3 install -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity