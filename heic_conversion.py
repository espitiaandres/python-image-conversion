import logging
import re
import os
from os.path import isfile, join
from wand.image import Image
from penguin_py import penguin
import shutil


logger = logging.getLogger(__name__)

# TODO: clean up duplicate/undry code
# TODO: add cli args?
# TODO: optimize with parallelism

INPUT_PATH = "./input"
OUTPUT_PATH = "./output"
FILE_TYPES_INPUT = (".heic", ".png")
FILE_TYPE_OUTPUT = "jpg"


@penguin(foreground="blue")
def image_move(file_name):
    source_file = f"{INPUT_PATH}/{file_name}"
    target_file = f"{OUTPUT_PATH}/{file_name}"
    shutil.move(source_file, target_file)
    return


@penguin(foreground="blue")
def image_conversion(file_name):
    source_file = f"{INPUT_PATH}/{file_name}"
    img = Image(filename=source_file)
    img.format = FILE_TYPE_OUTPUT

    if ".HEIC" in file_name:
        new_file_name = re.compile(re.escape(".heic"), re.IGNORECASE).sub(
            f".{FILE_TYPE_OUTPUT}", file_name
        )
    elif ".PNG" in file_name:
        new_file_name = re.compile(re.escape(".png"), re.IGNORECASE).sub(
            f".{FILE_TYPE_OUTPUT}", file_name
        )

    full_new_file_name = os.path.join(OUTPUT_PATH, new_file_name)
    img.save(filename=full_new_file_name)
    img.close()
    return


@penguin(verbose=True, foreground="green")
def main():
    files = [f for f in os.listdir(INPUT_PATH) if isfile(join(INPUT_PATH, f))]

    num_files = len(files)
    logger.info(f"# of files: {str(num_files)}")

    if not os.path.exists(OUTPUT_PATH):
        os.mkdir(os.path.join(OUTPUT_PATH))

    # TODO: separate this for loop in its own function
    for count, file_name in enumerate(files):
        if f".{FILE_TYPE_OUTPUT}" in file_name.lower():
            # If the file is already the desired output_type, just move the file
            image_move(file_name)
        else:
            # If the file is **not** already the desired output_type, convert the file
            image_conversion(file_name)

        percent_progress = "{0:.2f}".format((count + 1) * 100 / num_files)
        logger.info(f"Saved: {file_name}. Progress at: {percent_progress}%")


if __name__ == "__main__":
    main()
