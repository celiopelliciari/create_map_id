from PIL import Image
from functions import *


text_file = open("count_id.txt", "w")

with Image.open("colored_world_map.bmp", "r") as image_file:
    height = image_file.height
    width = image_file.width
    pixels = image_file.load()

    for i in range(width):
        for j in range(height):
            if check(pixels[i, j]):
                count_id = generate_str_pixel_and_id_number(pixels[i, j])
                text_file.write(count_id)

text_file.close()
