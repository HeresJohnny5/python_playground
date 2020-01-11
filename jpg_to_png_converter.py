# run file providing 2 arguments: file to open and new file to save
# when opening the file provided from the first argument, loop through the images converting them from jpg to png before saving them to the newly created file provided by the second argument

import argparse
import os
from PIL import Image

# CREATE FUNCTION
parser = argparse.ArgumentParser(
    description='Open a file, convert images from JPG format to PNG and save into a new file!')

parser.add_argument('--o', default='./pokedex',
                    help='This is the directory to be opened which contains jpg file format images to be converted to png.')
parser.add_argument('--n', default='./converted/',
                    help='This is the directory to be saved which contains images that have already been converted from jpg file format images to png.')

args = parser.parse_args()
file_open = args.o
new_directory = args.n
# print('file_open: {}'.format(file_open))
# print('new_file: {}'.format(new_file))

path = './pokedex/'

# CREATE FUNCTION
images = []
# r=root, d=directories, f = files
for r, d, f in os.walk(file_open):
    for image in f:
        if '.jpg' in image:
            images.append(image)

# CREATE FUNCTION
converted_images = []
for image in images:
    updated_image = image.replace('jpg', 'png')
    converted_images.append(updated_image)

# CREATE FUNCTION
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# CREATE FUNCTION
# complete_path = os.path.join('./converted', converted_images[0])
# file1 = open(complete_path, 'w')

for image in converted_images:
    complete_path = os.path.join(new_directory, image)
    im = open(complete_path, 'w+')
