ARG USERNAME=python
ARG USER_UID=1000
ARG USER_GID=$USER_UID

FROM python:3.11.2-alpine

# Defining the Author
MAINTAINER Bruno PC

#Create a working directory
WORKDIR /app

# Add the source code into the image
COPY . .

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Add sudo support
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Use non-root user
USER $USERNAME

# Install requirements
RUN sudo pip3 install -r requirements.txt

#Keep the container running before execution
ENTRYPOINT sleep infinity