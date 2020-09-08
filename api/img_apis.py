# -*- coding:utf-8 -*-

from datetime import datetime
from PIL import Image
import io
import os
import io
import numpy as np
import cv2


class img_api:
    def save_pil_img(self, img_binary):
        # OpenCV型からPIL型へ変換
        pil_img = img_binary.copy()
        if pil_img.ndim == 2:  # モノクロ
            pass
        elif pil_img.shape[2] == 3:  # カラー
            pil_img = cv2.cvtColor(pil_img, cv2.COLOR_BGR2RGB)
        elif pil_img.shape[2] == 4:  # 透過
            pil_img = cv2.cvtColor(pil_img, cv2.COLOR_BGRA2RGBA)
        pil_img = Image.fromarray(np.uint8(pil_img))

        # PIL確からbyte-PNG型へ変換
        modified_bin = io.BytesIO()
        pil_img.save(modified_bin, format='PNG')
        return modified_bin.getvalue()
