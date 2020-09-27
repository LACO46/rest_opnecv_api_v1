# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import (template_apis, img_apis)


class template_logic:
    def template_img(self, base_img: datastructures.FileStorage,
                     template_img: datastructures.FileStorage,
                     threshold: float) -> bytes:
        # 変数を定義
        template_api = template_apis.template_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        match_img_binary = template_api.template_img(base_img=base_img,
                                                     template_img=template_img,
                                                     threshold=threshold)

        return img_api.save_pil_img(match_img_binary)

    def template_count(self, base_img: datastructures.FileStorage,
                     template_img: datastructures.FileStorage,
                     threshold: float) -> int:
        # 変数を定義
        template_api = template_apis.template_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        match_count = template_api.matching_count(base_img=base_img,
                                                  template_img=template_img,
                                                  threshold=threshold)

        return match_count
