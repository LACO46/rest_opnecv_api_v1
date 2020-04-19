# -*- coding:utf-8 -*-

from logic import gray_scale_logics
from flask import send_file, make_response


class gray_scale_controller:
    def gray_scale(self, request):
        gray_scale_logic = gray_scale_logics.gray_scale_logic()

        file = request.files
        gray_scale_img = gray_scale_logic.gray_scale(file)
        response = make_response(gray_scale_img)
        response.headers.set('Content-Type', 'image/png')
        return response


1
