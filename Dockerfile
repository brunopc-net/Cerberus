FROM python:3.11-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/src"
ENV PCLOUD_USER=${PCLOUD_USER}
ENV PCLOUD_PASS=${PCLOUD_PASS}

# Install requirements
RUN pip3 install -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity