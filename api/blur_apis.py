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

        # xとyの平均値を利用したぼかし画像を作成
        return cv2.blur(img, (x, y))

    def gaussian(self, img_file: datastructures.FileStorage, x: int, y: int, sigma: int) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # ガウシアンフィルタを利用したぼかし画像を作成
        return cv2.GaussianBlur(img, (x, y), sigma)

    def median(self, img_file: datastructures.FileStorage, median_numeric: int) -> list:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # 中央値を利用したぼかし画像を作成
        return cv2.medianBlur(img,median_numeric)