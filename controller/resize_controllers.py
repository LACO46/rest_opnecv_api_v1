# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local

# import file
from logic import resize_logics


class resize_controller:
    def same_size(self, request: local.LocalProxy):
        # 変数を定義
        resize_logic = resize_logics.resize_logic()
        file = request.files
        times = 1.0

        # imgファイルが存在することを確認
        if ('img' not in file):
            return jsonify({'message': 'request image not found'}), 404
        try:
            if (request.args.get('times')):
                times = float(request.args.get('times'))
        except ValueError:
            return jsonify({'message': 'incorrect times param'}), 500

        # logicの呼び出し
        some_size_img = resize_logic.same_size(file['img'], times)

        # レスポンスの作成
        response = make_response(some_size_img)
        response.headers.set('Content-Type', 'image/png')
        return response

    def designation_size(self, request: local.LocalProxy, designation_size: str):
        # 変数を定義
        resize_logic = resize_logics.resize_logic()
        file = request.files
        size = designation_size.split("*")
        x = int(size[0])
        y = int(size[1])

        # imgファイルが存在することを確認
        if ('img' not in file):
            return jsonify({'message': 'request image not found'}), 404

        # logicの呼び出し
        designation_size_img = resize_logic.designation_size(file['img'], x, y)
        
        # レスポンスの作成
        response = make_response(designation_size_img)
        response.headers.set('Content-Type', 'image/png')
        return response