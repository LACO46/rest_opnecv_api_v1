# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import (binarization_apis, img_apis)


class binarization_logic:
    def binarization(self, img_file: datastructures.FileStorage, threshold_numerical: int) -> bytes:
        # 変数を定義
        binarization_api = binarization_apis.binarization_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_resize_binary = binarization_api.binarization(
            img_file, threshold_numerical)
        return img_api.save_pil_img(img_resize_binary)

    def adaptive_binarization(self, img_file: datastructures.FileStorage, block_size: int, mean_c: int) -> bytes:
        # 変数を定義
        binarization_api = binarization_apis.binarization_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_resize_binary = binarization_api.adaptive_binarization(
            img_file, block_size, mean_c)
        return img_api.save_pil_img(img_resize_binary)
