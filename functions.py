from constants import *


county_list = []


def check(pixel):
    if pixel != WATER_BLUE and pixel != BLACK:
        if pixel not in county_list:
            county_list.append(pixel)
            return True


class IdNumber:
    id = 10000


def generate_str_pixel_and_id_number(pixel):
    # Assign a str value to pixel variable
    p = str(pixel)
    # Assign a str value to id
    n = str(IdNumber.id)
    # Put 'p' and 'n' in a str variable
    str_pixel_and_id_number = p + " = " + n + "\n"
    IdNumber.id += 1
    return str_pixel_and_id_number
