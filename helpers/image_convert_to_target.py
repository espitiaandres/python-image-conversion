import os
import re

import constants
from penguin_py import penguin
from wand.image import Image


@penguin(foreground="blue")
def image_convert_to_target(file_name: str):
    """
    Convert a given image to the specified output file type in constants.py

    Args:
        file_name (str): Name of the file to convert
    """

    source_file = f"{constants.INPUT_PATH}/{file_name}"

    img = Image(filename=source_file)

    img.format = constants.OUTPUT_FILE_TYPE

    file_extension = file_name.split(".")[1]

    new_file_name = re.compile(re.escape(file_extension), re.IGNORECASE).sub(
        f".{constants.OUTPUT_FILE_TYPE}", file_name
    )

    full_new_file_name = os.path.join(constants.OUTPUT_PATH, new_file_name)
    img.save(filename=full_new_file_name)
    img.close()

    return
