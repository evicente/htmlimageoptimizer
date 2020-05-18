#!/usr/bin/env python3
import sys
import pathlib
import transformimage


def main():
    # TODO - Clean up and eliminate redundant code
    get_version()
    path_type()

def path_type():
    output_directory = set_output_directory()
    image_format = get_image_format()
    image_path = get_image_path()
    print(f"Images will be saved on folder: {output_directory}")
    print(f"In the format: {image_format}")
    print(f"Image location: {image_path}")

    if pathlib.Path(image_path).is_file():
        transformimage.transform_image(image_path, output_directory, image_format)
    elif pathlib.Path(image_path).is_dir():
        for file in pathlib.Path(image_path).iterdir():
            transformimage.transform_image(file, output_directory, image_format)
    else:
        print("Please verify the image path")

def get_version():
    if sys.version_info[0] != 3 and sys.version_info[1] < 6:
        raise Exception("Program requires Python 3.6 or greater")
        

def set_output_directory():
    output_directory = pathlib.Path.home().joinpath('Pictures', 'Optimizer')
    if not output_directory.exists():
        print(f'Creating output folder at location: {output_directory}')
        pathlib.Path.mkdir(output_directory)
    else:
        print(f'Output directory already exist at location: {output_directory}')
    return output_directory


def get_image_path():
    usr_path = pathlib.Path(input(f'Please enter image source path:'))
    if not usr_path.exists():
        print(f"Path does not exist.")
    else:
        return usr_path


def get_image_format():
    # TODO - change the selection from tuple to dictionary
    image_formats = (".jpg", ".gif", ".png")
    for i, v in enumerate(image_formats):
        print(f'{i + 1}. {v}')
    image_format = input(f'Please type image format: ')  
    if image_format not in image_formats:
        print(f'Wrong selection')
    else:
        return image_format


if __name__ == "__main__":
    main()
