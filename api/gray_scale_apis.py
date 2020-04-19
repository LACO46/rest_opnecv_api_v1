# -*- coding:utf-8 -*-

import numpy as np
import cv2


class gray_scale_api:
    def gray_scale(self, img_file):
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img_gray
