# -*- coding:utf-8 -*-

from api import gray_scale_apis
from api import img_apis


class gray_scale_logic:
    def gray_scale(self, file):
        gray_scale_api = gray_scale_apis.gray_scale_api()
        img_api = img_apis.img_api()

        if(('img' in file) == True):
            img_gray_binary = gray_scale_api.gray_scale(file['img'])
            return img_api.save_pil_img(img_gray_binary)
        return None
