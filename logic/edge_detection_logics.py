# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import (edge_detection_apis, img_apis)


class edge_detection_logic:
    def edge_detection(self, img_file: datastructures.FileStorage, threshold_max: int, threshold_min: int) -> bytes:
        # 変数を定義
        edge_detection_api = edge_detection_apis.edge_detection_api()
        img_api = img_apis.img_api()

        # APIから画像を取得
        edge_detection = edge_detection_api.edge_detection(
            img_file, threshold_max, threshold_min)

        return img_api.save_pil_img(edge_detection)
