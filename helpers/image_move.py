import shutil

import constants as c
from penguin_py import penguin


@penguin(foreground="blue")
def image_copy(file_name):
    source_file = f"{c.INPUT_PATH}/{file_name}"
    target_file = f"{c.OUTPUT_PATH}/{file_name}"
    shutil.copyfile(source_file, target_file)
    return