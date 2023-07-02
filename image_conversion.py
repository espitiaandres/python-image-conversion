import logging
import os
from os.path import isfile, join

from penguin_py import penguin

import constants
import helpers
from multiprocessing import Pool, cpu_count

logger = logging.getLogger(__name__)



@penguin(verbose=True, foreground="green")
def main():
    files = [
        f
        for f in os.listdir(constants.INPUT_PATH)
        if isfile(join(constants.INPUT_PATH, f))
    ]

    num_files = len(files)
    logger.info(f"# of files: {str(num_files)}")

    if not os.path.exists(constants.OUTPUT_PATH):
        os.mkdir(os.path.join(constants.OUTPUT_PATH))

    files_with_desired_output_type = []
    files_without_desired_output_type = []

    for file_name in files:
        if f".{constants.FILE_TYPE_OUTPUT}" in file_name.lower():
            files_with_desired_output_type.append(file_name)
        else:
            files_without_desired_output_type.append(file_name)
    
    with Pool(cpu_count()) as p:
        p.map(helpers.image_copy, files_with_desired_output_type)
        p.map(helpers.image_convert_to_target, files_without_desired_output_type)






    return


if __name__ == "__main__":
    main()
