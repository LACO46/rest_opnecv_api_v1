# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import cv2
import sys


class gray_scale_api:
    def gamma_correction_gray_scale_api(self, img_file: datastructures.FileStorage, gamma_numerical: float) -> list:
        # imgを低輝度に対応した数値のリストに変更
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)

        # opencvのガンマ補正を利用してグレースケールにする
        img = cv2.imdecode(img_array, 1)
        gamma22LUT = np.array([pow(x / 255.0, gamma_numerical)
                               for x in range(256)], dtype='float32')
        img_of_lut = cv2.LUT(img, gamma22LUT)
        gray_img_of_lut = cv2.cvtColor(
            img_of_lut, cv2.COLOR_BGR2GRAY)
        return pow(gray_img_of_lut, 1.0 / gamma_numerical) * 255
