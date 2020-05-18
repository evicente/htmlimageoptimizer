#!/usr/bin/env python3
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
