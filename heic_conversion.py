import logging
import re
import os
from os.path import isfile, join
from wand.image import Image
from penguin_py import penguin

import constants
import helpers


logger = logging.getLogger(__name__)

# TODO: abstract this out into separate functions
# TODO: clean up duplicate/undry code
# TODO: add cli args?
# TODO: optimize with parallelism



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


@penguin(verbose=True, foreground="green")
def main():
    files = [f for f in os.listdir(constants.INPUT_PATH) if isfile(join(constants.INPUT_PATH, f))]

    num_files = len(files)
    logger.info(f"# of files: {str(num_files)}")

    if not os.path.exists(constants.OUTPUT_PATH):
        os.mkdir(os.path.join(constants.OUTPUT_PATH))

    # TODO: separate this for loop in its own function
    for count, file_name in enumerate(files):
        if f".{constants.FILE_TYPE_OUTPUT}" in file_name.lower():
            # If the file is already the desired output_type, just move the file
            helpers.image_move(file_name)
        else:
            # If the file is **not** already the desired output_type, convert the file
            image_conversion(file_name)

        percent_progress = "{0:.2f}".format((count + 1) * 100 / num_files)
        logger.info(f"Saved: {file_name}. Progress at: {percent_progress}%")


if __name__ == "__main__":
    main()
