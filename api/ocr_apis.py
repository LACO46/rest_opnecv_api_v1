# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import pytesseract
import cv2


class ocr_api:
    def ocr(self, img_file: datastructures.FileStorage, language: str) -> str:
        # imgの数値のリストを読み込み
        stream = img_file.stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # OCR処理
        result = pytesseract.image_to_string(img, lang=language)
        return result
