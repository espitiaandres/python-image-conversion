import constants as c
from penguin_py import penguin
import shutil


@penguin(foreground="blue")
def image_move(file_name):
    source_file = f"{c.INPUT_PATH}/{file_name}"
    target_file = f"{c.OUTPUT_PATH}/{file_name}"
    shutil.move(source_file, target_file)
    return