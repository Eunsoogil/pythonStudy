# png가 웹에서는 더 좋다?
# python JPGtoPNGconverter.py pokedex/ convert/

import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{filename}.png', 'png')
    print(f'{clean_name} complete')
