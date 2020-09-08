# -*- coding:utf-8 -*-

from flask import send_file, make_response, jsonify, wrappers
from werkzeug import local
import numpy as np

# import file
from logic import convolution_2d_filter_logics


class convolution_2d_filter_controller:
    def convolution_2d_filter(self, request: local.LocalProxy, kernel: str) -> wrappers.Response:
        # 変数を定義
        convolution_2d_filter_logic = convolution_2d_filter_logics.convolution_2d_filter_logic()
        file = request.files
        kernel_list = []

        # imgファイルが存在することを確認
        if (not 'img' in file):
            return jsonify({'message': 'request image not found'}), 404
        try:
            kernel_list = [int(k) for k in kernel.split(",")]
        except:
            return jsonify({'message': 'requested kernel is invalid'}), 500

        size = np.sqrt(len(kernel_list))
        if(len(kernel_list) != size*size):
            return jsonify({'message': 'requested kernel is invalid'}), 500

        # logicの呼び出し
        filter_img = convolution_2d_filter_logic.convolution_2d_filter(
            file['img'], int(size), kernel_list)

        # レスポンスを作成
        response = make_response(filter_img)
        response.headers.set('Content-Type', 'image/png')
        return response
