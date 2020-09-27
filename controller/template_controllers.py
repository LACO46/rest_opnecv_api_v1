# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local
import numpy as np

# import file
from logic import template_logics


class template_conrtoller:
    def template_img(self, request: local.LocalProxy, threshold: float):
        # 変数を定義
        template_logic = template_logics.template_logic()
        file = request.files

        # imgファイルが存在することを確認
        if ('template' not in file):
            return jsonify({'message': 'request image not found'}), 404

        if ('base' not in file):
            return jsonify({'message': 'request image not found'}), 404

        # logicの呼び出し
        temp_match_img = template_logic.template_img(base_img=file['base'],
                                                     template_img=file['template'],
                                                     threshold=threshold)

        # レスポンスを作成
        response = make_response(temp_match_img)
        response.headers.set('Content-Type', 'image/png')
        return response

    def template_count(self, request: local.LocalProxy, threshold: float):
        # 変数を定義
        template_logic = template_logics.template_logic()
        file = request.files

        # imgファイルが存在することを確認
        if ('template' not in file):
            return jsonify({'message': 'request image not found'}), 404

        if ('base' not in file):
            return jsonify({'message': 'request image not found'}), 404

        # logicの呼び出し
        count = template_logic.template_count(base_img=file['base'],
                                              template_img=file['template'],
                                              threshold=threshold)

        # レスポンスを作成
        return jsonify({'count': count}), 200
