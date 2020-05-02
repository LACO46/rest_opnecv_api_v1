# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import cv2
import sys


class resize_api:
    def same_size_api(self, img_file: datastructures.FileStorage, times_numerical: float) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # サイズ取得
        height = img.shape[0]
        width = img.shape[1]

        # リサイズ
        return cv2.resize(img, (int(width * times_numerical), int(height * times_numerical)))
