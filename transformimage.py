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


def open_image(my_image_path, image_format):
    image_width_values = [100, 300, 500, 750, 1000, 1500, 2500]
    f, e = os.path.splitext(my_image_path)
    for value in image_width_values:
        new_string = '{}_{}{}'.format(f, value, image_format)
        print(new_string)
        outfile = new_string
        if my_image_path != outfile:
            size = (value, value)
            try:
                with Image.open(my_image_path) as im:
                    im.thumbnail(size)
                    im.save(outfile)
            except IOError:
                print("cannot convert", image_format)


def open_folder(my_folder_path, image_format):
    for file in os.listdir(my_folder_path):
        open_image(my_folder_path + '/' + file, image_format)


if __name__ == '__main__':
    folder_path = '/home/efrain/Pictures/Work/TestSet'
    image_path = '/home/efrain/Pictures/Work/TestSet/DSC_9114.JPG'
    open_image(image_path, '.jpg')
    # open_folder(folder_path, '.jpg')
