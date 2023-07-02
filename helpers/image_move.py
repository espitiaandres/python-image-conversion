import shutil

import constants as c
from penguin_py import penguin


@penguin(foreground="yellow")
def image_copy(file_name: str):
    """
    For files that are already of the specified output file type, just move these from 
    the INPUT_PATH to the OUTPUT_PATH

    Args:
        file_name (str): _description_
    """

    source_file = f"{c.INPUT_PATH}/{file_name}"
    target_file = f"{c.OUTPUT_PATH}/{file_name}"
    shutil.copyfile(source_file, target_file)

    return
