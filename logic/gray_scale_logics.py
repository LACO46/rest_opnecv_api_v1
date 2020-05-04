# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import (gray_scale_apis, img_apis)


class gray_scale_logic:
    def gray_scale(self, img_file: datastructures.FileStorage, gamma_numerical: float) -> bytes:
        # 変数を定義
        gray_scale_api = gray_scale_apis.gray_scale_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        img_gray_binary = gray_scale_api.gamma_correction_gray_scale_api(
            img_file, gamma_numerical)

        return img_api.save_pil_img(img_gray_binary)
