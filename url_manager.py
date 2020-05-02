# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, Response

# import file
from controller import (gray_scale_controllers, resize_controllers)


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

    @app.route('/v1/resize/same-size/<float:times>/', methods=['POST'])
    def same_size(times):
        resize_controller = resize_controllers.resize_controller()
        return resize_controller.same_size(request, times)

    @app.route('/v1/resize/designation-size/<string:designation_size>/', methods=['POST'])
    def designation_size(designation_size):
        resize_controller = resize_controllers.resize_controller()
        return resize_controller.designation_size(request, designation_size)


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
