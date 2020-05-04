# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local

# import file
from logic import edge_detection_logics


class edge_detection_controller:
    def edge_detection(self, request: local.LocalProxy, threshold_max:int, threshold_min:int) -> wrappers.Response:
        # 変数を定義
        edge_detection_logic = edge_detection_logics.edge_detection_logic()
        file = request.files

        # imgファイルが存在することを確認
        if (not 'img' in file):
            return jsonify({'message': 'request image not found'}), 404
        if(threshold_max < threshold_min):
            return jsonify({'message': 'threshold max is less than the threshold min'})
        # logicの呼び出し
        edge_img = edge_detection_logic.edge_detection(file['img'], threshold_max, threshold_min)

        # レスポンスを作成
        response = make_response(edge_img)
        response.headers.set('Content-Type', 'image/png')
        return response
