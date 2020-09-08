# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import (resize_apis, img_apis)


class resize_logic:
    def same_size(self, img_file: datastructures.FileStorage, times_numerical: float) -> bytes:
        # 変数を定義
        resize_api = resize_apis.resize_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_resize_binary = resize_api.same_size_api(img_file, times_numerical)
        return img_api.save_pil_img(img_resize_binary)

    def designation_size(self, img_file, x_numerical: int, y_numerical: int) -> bytes:
        # 変数を定義
        resize_api = resize_apis.resize_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_designation_binary = resize_api.designation_size_api(
            img_file, x_numerical, y_numerical)
        return img_api.save_pil_img(img_designation_binary)
