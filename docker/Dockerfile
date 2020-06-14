# Retrieve image from Dockerhub
FROM python:3.8

# Install Vim
USER root
RUN apt-get update
RUN apt-get -y install git curl vim

# Install pip
RUN mkdir /opt/trivial-purfuit
WORKDIR /opt/trivial-purfuit