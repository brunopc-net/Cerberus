FROM python:3.11-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

# Install requirements with non-root user
RUN adduser -D python
USER python
WORKDIR /home/python

COPY --chown=python:python requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# Adding src to python path
ENV PYTHONPATH "${PYTHONPATH}:/src"

#Keep the container running before execution
ENTRYPOINT sleep infinity