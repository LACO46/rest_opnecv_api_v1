# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local
import numpy as np

# import file
from logic import ocr_logics


class ocr_controller:
    def ocr(self, request: local.LocalProxy, language: str) -> tuple:
        # 変数を定義
        ocr_logic = ocr_logics.ocr_logic()
        file = request.files

        # imgファイルが存在することを確認
        if ('img' not in file):
            return jsonify({'message': 'request image not found'}), 404

        # logicの呼び出し
        img_word = ocr_logic.ocr(file['img'], language)

        # レスポンスの作成
        response = jsonify({'word': img_word}), 200
        return response
