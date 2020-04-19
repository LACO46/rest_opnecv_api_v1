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

RUN pip3 install flask
RUN pip3 install matplotlib
RUN pip3 install numpy
RUN pip3 install opencv-contrib-python
RUN pip3 install opencv-python
RUN pip3 install Pillow