# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local

# import file
from logic import gray_scale_logics


class gray_scale_controller:
    def gray_scale(self, request: local.LocalProxy) -> wrappers.Response:
        # 変数を定義
        gray_scale_logic = gray_scale_logics.gray_scale_logic()
        file = request.files
        gamma = 2.2

        # imgファイルが存在することを確認
        if (not 'img' in file):
            return jsonify({'message': 'request image not found'}), 404
        try:
            if (request.args.get('gamma')):
                gamma = float(request.args.get('gamma'))
        except ValueError:
            return jsonify({'message': 'incorrect gamma param'}), 500

        # logicの呼び出し
        gray_scale_img = gray_scale_logic.gray_scale(
            file['img'], gamma)

        # レスポンスを作成
        response = make_response(gray_scale_img)
        response.headers.set('Content-Type', 'image/png')
        return response
