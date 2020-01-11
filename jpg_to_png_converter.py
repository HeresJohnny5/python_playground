# run file providing 2 arguments: file to open and new file to save
# when opening the file provided from the first argument, loop through the images converting them from jpg to png before saving them to the newly created file provided by the second argument

import argparse
import os
from PIL import Image


def user_input():
    parser = argparse.ArgumentParser(
        description='Open a file, convert images from JPG format to PNG and save into a new file!')

    parser.add_argument('--o', default='./pokedex',
                        help='This is the directory to be opened which contains jpg file format images to be converted to png.')
    parser.add_argument('--n', default='./converted/',
                        help='This is the directory to be saved which contains images that have already been converted from jpg file format images to png.')

    args = parser.parse_args()
    directory_open = args.o
    new_directory = args.n

    return {'old_dir': directory_open, 'new_dir': new_directory}


def pulled_jpg_images(old_dir):
    images = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(old_dir):
        for image in f:
            if '.jpg' in image:
                images.append(image)

    return images


def convert_jpg_to_png(images):
    converted_images = []

    for image in images:
        updated_image = image.replace('jpg', 'png')
        converted_images.append(updated_image)

    return converted_images


def create_directory():
    if not os.path.exists(directories['new_dir']):
        os.makedirs(directories['new_dir'])


def save_png_files_to_new_dir(png_images):
    for image in png_images:
        complete_path = os.path.join(directories['new_dir'], image)
        im = open(complete_path, 'w+')


directories = user_input()
jpg_images = pulled_jpg_images(directories['old_dir'])
png_images = convert_jpg_to_png(jpg_images)
create_directory()
save_png_files_to_new_dir(png_images)
