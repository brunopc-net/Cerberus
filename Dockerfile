ARG USER=python

# Defining the Author
MAINTAINER Bruno PC

FROM python:3.11-alpine

#upgrade pip
RUN pip install --upgrade pip

#Add non-root user and create a working directory
RUN adduser -D $USER
USER $USER
WORKDIR /home/$USER

# Add the source code into the image
COPY --chown=myuser:myuser . .

# Install python requirements
RUN pip install --user -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity