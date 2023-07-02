# Image Conversion with Python

Convert all images in a specified directory to a specified file type.

- To specify the directory that has all the images you want to convert, change the `INPUT_PATH` variable in `./constants/constants.py`. This can be anything, as long as it is a valid path 😄.
- To specify the directory that will contain all the **converted** images, change the `OUTPUT_PATH` variables in `./constants/constants.py`. Again this can be anything, as long as it is a valid path 😄.
- To specify the output type of all the **converted** images, change the `OUTPUT_FILE_TYPE` variable in `./constants/constants.py`. This can be any file type supported by the `Wand` pip library and the `ImageMagick` suite, which are detailed here:
  - Wand: https://docs.wand-py.org/en/0.4.5/guide/write.html
  - ImageMagick: https://imagemagick.org/index.php

## Installation

- In your terminal, create a virtual environment (venv) through the following command. Remember to replace the venv's name:
  - `python3 -m venv <NAME_OF_YOUR_VIRTUAL_ENVIRONMENT_HERE>`
- Activate your virtual environment with the following command:
  - `source <NAME_OF_YOUR_VIRTUAL_ENVIRONMENT_HERE>/bin/activate`
- Once your venv is activated, install all the necessary pip packages detailed in `requirements.txt`. You can do this by using this command:
  - `pip install -r requirements.txt`
- Once this command succeeds, specify the necessary parameters in `./constants/constants.py` as detailed above.
- Run the command below. This will start your image conversion!
  - `python image_conversion.py`

## Notes

- This script uses python's multithreading library as a workaround to the GIL. This helps with scalability, given a case where you have hundreds of images (or more) that you want to convert from one file type to another.
- If you have any suggestions on how to make this script better, please add an issue here:
  - https://github.com/espitiaandres/python-image-conversion/issues
