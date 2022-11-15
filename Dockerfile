FROM python:3.8-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONUNBUFFERED 1

FROM python:3.8-slim-bullseye as builder
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    gcc python3-dev \
    libsnmp-base \
    libsnmp-dev \
    #libmysqlclient-dev \
    python3-dev
    

# Set work directory
RUN mkdir /code
WORKDIR /code

# Install dependencies into a virtualenv
RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY . /code/


EXPOSE 8000