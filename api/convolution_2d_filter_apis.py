# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import cv2
import sys


class convolution_2d_filter_api:
    def convolution_2d_filter(self, img_file: datastructures.FileStorage, kernel_list: np.ndarray) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # opencvのfilter2Dを利用する
        return cv2.filter2D(img, -1, kernel_list)
