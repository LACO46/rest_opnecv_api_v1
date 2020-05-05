# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import cv2
import sys


class blur_api:
    def average(self, img_file: datastructures.FileStorage, x: int, y: int) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # エッジ検出する
        return cv2.blur(img, (x, y))
