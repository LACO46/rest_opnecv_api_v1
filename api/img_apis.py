# -*- coding:utf-8 -*-

from datetime import datetime
from PIL import Image
import io
import os
import cv2
import random
import io
import numpy as np


class img_api:
    def save_pil_img(self, img_binary):
        pil_img = Image.fromarray(np.uint8(img_binary))
        modified_bin = io.BytesIO()
        pil_img.save(modified_bin, format='PNG')
        return modified_bin.getvalue()
