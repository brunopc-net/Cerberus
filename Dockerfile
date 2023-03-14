FROM python:3.11-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/src"

# Install requirements
RUN pip3 install -r requirements.txt

EXPORT username=""

#Keep the container running before execution
ENTRYPOINT sleep infinity