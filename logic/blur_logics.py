# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import (blur_apis, img_apis)


class blur_logic:
    def average(self, img_file: datastructures.FileStorage, x: int, y: int) -> bytes:
        # 変数を定義
        blur_api = blur_apis.blur_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_blur_binary = blur_api.average(img_file, x, y)
        return img_api.save_pil_img(img_blur_binary)

    def gaussian(self, img_file: datastructures.FileStorage, x: int, y: int, sigma: int) -> bytes:
        # 変数を定義
        blur_api = blur_apis.blur_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_blur_binary = blur_api.gaussian(img_file, x, y, sigma)
        return img_api.save_pil_img(img_blur_binary)

    def median(self, img_file: datastructures.FileStorage, median_numeric: int) -> bytes:
        # 変数を定義
        blur_api = blur_apis.blur_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_blur_binary = blur_api.median(img_file, median_numeric)
        return img_api.save_pil_img(img_blur_binary)

    def bilateral(self, img_file: datastructures.FileStorage, pixel_interest: int, sigma_color: int, sigma_space: int) -> bytes:
        # 変数を定義
        blur_api = blur_apis.blur_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_blur_binary = blur_api.bilateral(img_file, pixel_interest, sigma_color, sigma_space)
        return img_api.save_pil_img(img_blur_binary)