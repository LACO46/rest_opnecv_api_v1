# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local

# import file
from logic import binarization_logics


class binarization_controller:
    def binarization(self, request: local.LocalProxy, threshold: int):
        # 変数を定義
        binarization_logic = binarization_logics.binarization_logic()
        file = request.files

        # imgファイルが存在することを確認
        if ('img' not in file):
            return jsonify({'message': 'request image not found'}), 404

        # logicの呼び出し
        img = binarization_logic.binarization(file['img'], threshold)

        # レスポンスの作成
        response = make_response(img)
        response.headers.set('Content-Type', 'image/png')
        return response

    def adaptive_binarization(self, request: local.LocalProxy, block_size: int, mean_c: int):
        # 変数を定義
        binarization_logic = binarization_logics.binarization_logic()
        file = request.files

        # imgファイルが存在することを確認
        if ('img' not in file):
            return jsonify({'message': 'request image not found'}), 404

        # block_sizeが機数であるか確認
        if(block_size % 2 != 1):
            return jsonify({'message': 'request block_size is must odd'}), 500

        # logicの呼び出し
        img = binarization_logic.adaptive_binarization(
            file['img'], block_size, mean_c)

        # レスポンスの作成
        response = make_response(img)
        response.headers.set('Content-Type', 'image/png')
        return response
