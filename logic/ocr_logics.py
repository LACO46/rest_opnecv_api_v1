# -*- coding:utf-8 -*-

from werkzeug import datastructures

# import file
from api import (ocr_apis)


class ocr_logic:
    def ocr(self, img_file: datastructures.FileStorage, language: str) -> str:
        # 変数を定義
        ocr_api = ocr_apis.ocr_api()

        # APIから文字列を取得
        return ocr_api.ocr(img_file, language)
