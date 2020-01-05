FROM ubuntu:18.04

RUN apt-get update \
 && apt-get install -y wget \
 && apt-get install -y sudo \
 && apt-get install -y python3-dev

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN sudo python3 get-pip.py

RUN pip install flask
RUN pip install numpy
RUN pip install opencv-contrib-python
RUN pip install opencv-python