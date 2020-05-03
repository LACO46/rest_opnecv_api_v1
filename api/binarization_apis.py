# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import cv2
import sys


class binarization_api:
    def binarization(self, img_file: datastructures.FileStorage, threshold_numerical: int) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # 二値化(閾値100を超えた画素を255にする。)
        ret, img_thresh = cv2.threshold(img, threshold_numerical, 255, cv2.THRESH_BINARY)
        return img_thresh

    def adaptive_binarization(self, img_file: datastructures.FileStorage, block_size: int, mean_c: int) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 0)

        # 二値化(閾値100を超えた画素を255にする。
        img_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, mean_c)
        return img_thresh