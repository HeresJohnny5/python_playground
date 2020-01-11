# run file providing 2 arguments: file to open and new file to save
# when opening the file provided from the first argument, loop through the images converting them from jpg to png before saving them to the newly created file provided by the second argument

import argparse

parser = argparse.ArgumentParser(
    description='Open a file, convert images from JPG format to PNG and save into a new file!')

parser.add_argument('--o', default='./pokedex',
                    help='This is the file to be opened which contains jpg file format images to be converted to png.')
parser.add_argument('--n', default='./converted',
                    help='This is the file to be saved which contains images that have already been converted from jpg file format images to png.')

args = parser.parse_args()
file_open = args.o
new_file = args.n
print(file_open)
print(new_file)
