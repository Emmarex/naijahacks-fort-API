import io
import base64
import cv2
import numpy as np
from PIL import Image

default_image_size = tuple((256, 256))

def convert_image(image_data):
    try:
        image_grayscale = Image.open(io.BytesIO(base64.b64decode(image_data))).convert('L')
        image_grayscale = image_grayscale.resize(default_image_size, Image.ANTIALIAS)
        image_np = np.array(image_grayscale)
        img_list = []
        for line in image_np:
            for value in line:
                img_list.append(value)
        return [img_list], None
    except Exception as e:
        return None, str(e)