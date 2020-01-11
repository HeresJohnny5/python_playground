# run file providing 2 arguments: file to open and new file to save
# when opening the file provided from the first argument, loop through the images converting them from jpg to png before saving them to the newly created file provided by the second argument

import argparse
import os
from PIL import Image

# CREATE FUNCTION
parser = argparse.ArgumentParser(
    description='Open a file, convert images from JPG format to PNG and save into a new file!')

parser.add_argument('--o', default='./pokedex',
                    help='This is the file to be opened which contains jpg file format images to be converted to png.')
parser.add_argument('--n', default='./converted',
                    help='This is the file to be saved which contains images that have already been converted from jpg file format images to png.')

args = parser.parse_args()
file_open = args.o
new_file = args.n
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

print(converted_images)

# Image.open('./pokedex/bulbasaur.jpg').show()

# try:
#     im1 = Image.open('./pokedex/bulbasaur.jpg')
#     im1.show()
# except NameError:
#     print('Image name does not exist:')
# except FileNotFoundError:
#     print('File nout found:')

# im = Image.open('./pokedex/bulbasaur.jpg')
# im.save('bulbasaur.png')
