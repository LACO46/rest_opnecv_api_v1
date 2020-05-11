FROM ubuntu:18.04

RUN apt-get update \
 && apt-get install -y wget \
    sudo \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    python-pip \
    python3-pip

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN pip3 install flask \
                 matplotlib \
                 numpy \
                 opencv-contrib-python \
                 opencv-python \
                 Pillow

WORKDIR /home