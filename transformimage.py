#!/usr/bin/env python3
from PIL import Image
import os

"""
Upload width size:
- 100  pixels
- 300  pixels
- 500  pixels
- 750  pixels
- 1000 pixels
- 1500 pixels
- 2500 pixels

Image Requirements
File types:
    - .jpg
    - .gif
    - .png
"""

from PIL import Image
import pathlib


def transform_image(image_path, dir_out, img_format):
    size = (128, 128)
    out_file = pathlib.Path(dir_out).joinpath(pathlib.Path(image_path).stem + img_format)
    if pathlib.Path(image_path).suffix != img_format:
        try:
            with Image.open(image_path) as im:
                im.thumbnail(size)
                im.save(out_file)
        except IOError:
            print("cannot create thumbnail for", image_path)
