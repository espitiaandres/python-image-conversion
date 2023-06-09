import re
import os

import constants
from penguin_py import penguin
from wand.image import Image


@penguin(foreground="blue")
def image_conversion(file_name):
    source_file = f"{constants.INPUT_PATH}/{file_name}"
    img = Image(filename=source_file)
    img.format = constants.FILE_TYPE_OUTPUT

    if ".HEIC" in file_name:
        new_file_name = re.compile(re.escape(".heic"), re.IGNORECASE).sub(
            f".{constants.FILE_TYPE_OUTPUT}", file_name
        )
    elif ".PNG" in file_name:
        new_file_name = re.compile(re.escape(".png"), re.IGNORECASE).sub(
            f".{constants.FILE_TYPE_OUTPUT}", file_name
        )

    full_new_file_name = os.path.join(constants.OUTPUT_PATH, new_file_name)
    img.save(filename=full_new_file_name)
    img.close()
    return