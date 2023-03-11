FROM python:3.11.2-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

# Use non-root user
USER python

# Install requirements
RUN pip3 install -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity