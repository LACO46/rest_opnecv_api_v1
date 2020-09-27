# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, Response

# import file
from controller import (gray_scale_controllers, resize_controllers,
                        binarization_controllers, edge_detection_controllers,
                        blur_controllers, convolution_2d_filter_controllers,
                        ocr_controllers, template_controllers)


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

    @app.route('/v1/binarization/<int:threshold>/', methods=['POST'])
    def binarization(threshold):
        binarization_controller = binarization_controllers.binarization_controller()
        return binarization_controller.binarization(request, threshold)

    @app.route('/v1/adaptive/binarization/<int:block_size>/<int:mean_c>/', methods=['POST'])
    def adaptive_binarization(block_size, mean_c):
        binarization_controller = binarization_controllers.binarization_controller()
        return binarization_controller.adaptive_binarization(request, block_size, mean_c)

    @app.route('/v1/edge-detection/<int:threshold_max>/<int:threshold_min>/', methods=['POST'])
    def edge_detection(threshold_max, threshold_min):
        edge_detection_controller = edge_detection_controllers.edge_detection_controller()
        return edge_detection_controller.edge_detection(request, threshold_max, threshold_min)

    @app.route('/v1/blur/average/<int:x>/<int:y>/', methods=['POST'])
    def blurs_average(x, y):
        blur_controller = blur_controllers.blur_controller()
        return blur_controller.average(request, x, y)

    @app.route('/v1/blur/gaussian/<int:x>/<int:y>/<int:sigma>/', methods=['POST'])
    def blurs_gaussian(x, y, sigma):
        blur_controller = blur_controllers.blur_controller()
        return blur_controller.gaussian(request, x, y, sigma)

    @app.route('/v1/blur/median/<int:median_numeric>/', methods=['POST'])
    def blurs_median(median_numeric):
        blur_controller = blur_controllers.blur_controller()
        return blur_controller.median(request, median_numeric)

    @app.route('/v1/blur/bilateral/<int:pixel_interest>/<int:sigma_color>/<int:sigma_space>/', methods=['POST'])
    def blurs_bilateral(pixel_interest, sigma_color, sigma_space):
        blur_controller = blur_controllers.blur_controller()
        return blur_controller.bilateral(request, pixel_interest, sigma_color, sigma_space)

    @app.route('/v1/convolution-2d/<string:kernel>/', methods=['POST'])
    def convolution_2d_filter(kernel):
        convolution_2d_filter_controller = convolution_2d_filter_controllers.convolution_2d_filter_controller()
        return convolution_2d_filter_controller.convolution_2d_filter(request, kernel)

    @app.route('/v1/ocr/<string:language>/', methods=['POST'])
    def ocr(language):
        ocr_controller = ocr_controllers.ocr_controller()
        return ocr_controller.ocr(request, language)

    @app.route('/v1/template/<float:threshold>/', methods=['POST'])
    def template_img(threshold):
        template_conrtoller = template_controllers.template_conrtoller()
        return template_conrtoller.template_img(request, threshold)

    @app.route('/v1/template/<float:threshold>/count/', methods=['POST'])
    def template_count(threshold):
        template_conrtoller = template_controllers.template_conrtoller()
        return template_conrtoller.template_count(request, threshold)

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
