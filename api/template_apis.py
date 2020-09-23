# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np
import cv2
import sys


class template_api:
    def template_img(self, base_img: datastructures.FileStorage,
                     template_img: datastructures.FileStorage,
                     threshold: float) -> list:
        # base imgの数値のリストを読み込み
        base_stream = base_img.stream
        base_img_array = np.asarray(
            bytearray(base_stream.read()), dtype=np.uint8)
        base_img = cv2.imdecode(base_img_array, 0)

        # template imgの数値のリストを読み込み
        template_stream = template_img.stream
        template_img_array = np.asarray(
            bytearray(template_stream.read()), dtype=np.uint8)
        template_img = cv2.imdecode(template_img_array, 0)

        # マッチングテンプレートを実行
        match_result = cv2.matchTemplate(
            base_img, template_img, cv2.TM_CCOEFF_NORMED)

        # 検出結果から検出領域の位置を取得
        loc = np.where(match_result >= threshold)

        # カラー画像の読み込み
        result = cv2.imdecode(base_img_array, 1)

        # 検出領域を四角で囲んで保存
        w, h = template_img.shape[::-1]
        for pt in zip(*loc[::-1]):
            cv2.rectangle(result, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

        # # ここから
        # cv2.rectangle(result, top_left, bottom_right, (255, 0, 0), 10)

        return result
