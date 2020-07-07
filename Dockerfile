FROM python:3.7

RUN apt-get update \
    && apt-get install -y wget \
    sudo \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6

RUN wget https://bootstrap.pypa.io/get-pip.py

ADD requirements.txt /
RUN pip install -r requirements.txt