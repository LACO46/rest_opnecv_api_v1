# -*- coding:utf-8 -*-

from werkzeug import datastructures
import numpy as np

# import file
from api import (convolution_2d_filter_apis, img_apis)


class convolution_2d_filter_logic:
    def convolution_2d_filter(self, img_file: datastructures.FileStorage, kernel_size: int, kernel_list: list) -> bytes:
        # 変数を定義
        kernel_np_array = np.array(kernel_list).reshape(kernel_size, kernel_size)
        convolution_2d_filter_api = convolution_2d_filter_apis.convolution_2d_filter_api()
        img_api = img_apis.img_api()

        # # APIから画像を取得
        img_gray_binary = convolution_2d_filter_api.convolution_2d_filter(img_file, kernel_np_array)
        return img_api.save_pil_img(img_gray_binary)
