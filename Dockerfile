FROM ubuntu:18.04

RUN apt-get update \
 && apt-get install -y wget \
 && apt-get install -y unzip \
 && apt-get install -y sudo \
 && apt-get install -y make \
 && apt-get install -y cmake \
 && apt-get install -y build-essential cmake unzip pkg-config \
 && apt-get install -y libjpeg-dev libpng-dev libtiff-dev \
 && apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
 && apt-get install -y libxvidcore-dev libx264-dev \
 && apt-get install -y libgtk-3-dev \
 && apt-get install -y libatlas-base-dev gfortran \
 && apt-get install -y python3-dev

RUN cd ~
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip
RUN unzip opencv.zip
RUN unzip opencv_contrib.zip
RUN mv opencv-4.0.0 opencv
RUN mv opencv_contrib-4.0.0 opencv_contrib

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN sudo python3 get-pip.py

RUN apt-get install -y software-properties-common vim
RUN add-apt-repository -r ppa:jonathonf/python-3.6
RUN apt-get update -q

RUN pip install flask
RUN pip install numpy
RUN pip install opencv-contrib-python
RUN pip install opencv-python

# RUN mkdir ./opencv/build
# # RUN cd ./opencv/build \
#  && cmake -D CMAKE_BUILD_TYPE=RELEASE \
#           -D CMAKE_INSTALL_PREFIX=/usr/local \
#           -D INSTALL_PYTHON_EXAMPLES=ON \
#           -D INSTALL_C_EXAMPLES=OFF \
#           -D OPENCV_ENABLE_NONFREE=ON \
#           -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
#           -D BUILD_EXAMPLES=ON ..

# RUN make -j4
# RUN make install
# RUN ldconfig