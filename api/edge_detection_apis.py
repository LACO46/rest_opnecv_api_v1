# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import cv2
import sys


class edge_detection_api:
    def edge_detection(self, img_file: datastructures.FileStorage, threshold_max: int, threshold_min: int) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 0)

        # エッジ検出する
        return cv2.Canny(img, threshold_max, threshold_min)
