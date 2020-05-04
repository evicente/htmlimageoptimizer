#!/usr/bin/env python3
import image_functions
import os
import argparse


# image_path = '/home/efrain/Pictures/Work/TestSet/DSC_9114.JPG'


def arg_parser():
    parser = argparse.ArgumentParser(prog="HTML Image Optimizer", description="HTML Image Optimizer")
    parser.add_argument('-g', '--gui', action='store_true',
                        help="Pass the '-g' flag to start in gui mode.")
    args = parser.parse_args()
    if args.gui:
        print("GUI mode selected.")


def main():
    arg_parser()
    application_menu()
    usr_selection()


def image_type():
    selection_menu = {'1': '.jpg', '2': '.gif', '3': '.png'}
    print('Please select image extension')
    print('1.{}\n2.{}\n3.{}'.format(selection_menu['1'],
                                    selection_menu['2'],
                                    selection_menu['3']))
    selection = input('Selection: ')
    if selection in selection_menu.keys():
        return selection_menu[selection]


def get_image_options():
    path = input('Please enter image path:')
    if not os.path.exists(path):
        print('Invalid file folder or image path.')
    else:
        image_functions.open_image(path, image_type())


def get_folder_options():
    path = input('Please enter folder path:')
    if not os.path.exists(path):
        print('Invalid folder or image path.')
    else:
        image_functions.open_image(path, image_type())


def usr_selection():
    while True:
        try:
            usr_input = int(input('SELECTION:'))
            if usr_input == 1:
                get_image_options()
                application_menu()
            elif usr_input == 2:
                print('You want to use bulk transform')
                get_folder_options()
                application_menu()
            elif usr_input == 3:
                print('You want to ')
            elif usr_input == 4:
                print('Closing Web Image Manager')
                break
            else:
                print('Invalid selection')
                application_menu()
        except ValueError:
            print('Invalid input')
            application_menu()


def application_menu():
    print('Welcome to Image Manager for Web')
    print('Please make a selection:')
    main_menu = '''
    1. Transform single image
    2. Bulk transform
    3. Help
    4. Exit
    '''
    print(main_menu)


if __name__ == '__main__':
    main()
