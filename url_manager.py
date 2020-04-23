# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, Response
from controller import gray_scale_controllers


class urls:
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    @app.route('/', methods=['GET'])
    def index():
        return "Hello World\n"

    @app.route('/v1/gray/', methods=['POST'])
    def gray_scale():
        gray_scale_controller = gray_scale_controllers.gray_scale_controller()
        return gray_scale_controller.gray_scale(request)

    @app.errorhandler(400)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def error_handler(error):
        response = jsonify(
            {
                "code": error.code,
                "status": error.code,
                "result": {
                    'error_name': error.name,
                    'type': error.description
                }
            }
        )
        return response
