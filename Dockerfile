ARG USER=python
ARG UID=1000

FROM python:3.11.2-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

# Create the user
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

# Use non-root user
USER $USER

# Install requirements
RUN sudo pip3 install -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity