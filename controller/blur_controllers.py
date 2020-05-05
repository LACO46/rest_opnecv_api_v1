# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local

# import file
from logic import blur_logics


class blur_controller:
    def average(self, request: local.LocalProxy, x: int, y: int) -> wrappers.Response:
        # 変数を定義
        blur_logic = blur_logics.blur_logic()
        file = request.files

        # imgファイルが存在することを確認
        if (not 'img' in file):
            return jsonify({'message': 'request image not found'}), 404

        # logicの呼び出し
        blur_img = blur_logic.average(file['img'], x, y)

        # レスポンスを作成
        response = make_response(blur_img)
        response.headers.set('Content-Type', 'image/png')
        return response

    def gaussian(self, request: local.LocalProxy, x: int, y: int, sigma: int) -> wrappers.Response:
        # 変数を定義
        blur_logic = blur_logics.blur_logic()
        file = request.files

        # imgファイルが存在することを確認
        if (not 'img' in file):
            return jsonify({'message': 'request image not found'}), 404

        # logicの呼び出し
        blur_img = blur_logic.gaussian(file['img'], x, y, sigma)

        # レスポンスを作成
        response = make_response(blur_img)
        response.headers.set('Content-Type', 'image/png')
        return response