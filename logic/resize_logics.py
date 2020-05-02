# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import resize_apis
from api import img_apis


class resize_logic:
    def same_size(self, img_file: datastructures.FileStorage, times_numerical: float) -> bytes:
        # 変数を定義
        resize_api = resize_apis.resize_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_resize_binary = resize_api.same_size_api(img_file, times_numerical)

        return img_api.save_pil_img(img_resize_binary)
