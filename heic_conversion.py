import logging
import re
import os
from os.path import isfile, join
from wand.image import Image
from penguin_py import penguin

logger = logging.getLogger(__name__)

# TODO: make this extensible for PNG/HEIC to JPG
# TODO: clean up duplicate/undry code
# TODO: add cli args?
# TODO: optimize

FILE_TYPES_INPUT = (".heic", ".png")
FILE_TYPE_OUTPUT = ".jpg"


@penguin(verbose=True, foreground="green")
def main():
    input_path = "./input"
    output_path = "./output"

    # TODO: clean this up
    files = [
        f
        for f in os.listdir(input_path)
        if isfile(join(input_path, f))
        and f != __file__
        and str(f).lower().endswith(FILE_TYPES_INPUT)
    ]

    num_files = len(files)
    logger.info(f"# of files: {str(num_files)}")

    os.mkdir(os.path.join(output_path))

    # TODO: separate this for loop in its own function
    for count, file_name in enumerate(files):
        source_file = f"{input_path}/{file_name}"
        img = Image(filename=source_file)
        img.format = "jpg"

        if ".HEIC" in file_name:
            # new_file_name = os.path.join(output_path, file_name.replace(".HEIC", ".JPG"))
            new_file_name = re.compile(re.escape(".heic"), re.IGNORECASE).sub(".jpg", file_name)
            # full_new_file_name = os.path.join(output_path, new_file_name)
        elif ".PNG" in file_name:
            # new_file_name = os.path.join(output_path, file_name.replace(".PNG", ".JPG"))
            new_file_name = re.compile(re.escape(".png"), re.IGNORECASE).sub(".jpg", file_name)
        
        full_new_file_name = os.path.join(output_path, new_file_name)
        img.save(filename=full_new_file_name)
        img.close()
        # TODO: use logger instead of print statements
        logger.info(f"Saved: {file_name}. {str((count) * 100 / num_files)}%")


if __name__ == "__main__":
    main()
