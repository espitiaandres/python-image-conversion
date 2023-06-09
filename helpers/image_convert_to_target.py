import os
import re

import constants
from penguin_py import penguin
from wand.image import Image


@penguin(foreground="blue")
def image_convert_to_target(file_name: str):
    source_file = f"{constants.INPUT_PATH}/{file_name}"

    img = Image(filename=source_file)

    img.format = constants.FILE_TYPE_OUTPUT

    file_extension = file_name.split(".")[1]

    new_file_name = re.compile(re.escape(file_extension), re.IGNORECASE).sub(
        f".{constants.FILE_TYPE_OUTPUT}", file_name
    )

    full_new_file_name = os.path.join(constants.OUTPUT_PATH, new_file_name)
    img.save(filename=full_new_file_name)
    img.close()
    return
