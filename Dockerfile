FROM python:3.7

RUN apt-get update \
    && apt-get install -y wget \
    sudo \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    tesseract-ocr \
    libtesseract-dev \
    tesseract-ocr-jpn  tesseract-ocr-jpn-vert \
    tesseract-ocr-script-jpan tesseract-ocr-script-jpan-vert

RUN wget https://bootstrap.pypa.io/get-pip.py

ADD requirements.txt /
RUN pip install -r requirements.txt