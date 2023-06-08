import os
from os.path import isfile, join
from wand.image import Image
from penguin_py import penguin

# TODO: make this extensible for PNG/HEIC to JPG
# TODO: clean up duplicate/undry code
# TODO: add cli args?
# TODO: optimize

FILE_TYPES_INPUT = (".heic", ".png")
FILE_TYPE_OUTPUT = ".jpg"


@penguin(verbose=True, foreground="green")
def main():
    mypath = "./"

    # TODO: clean this up
    files = [
        f
        for f in os.listdir(mypath)
        if isfile(join(mypath, f))
        and f != "heic_conversion.py"
        and str(f).lower().endswith((".heic", ".png"))
    ]

    num_files = len(files)
    print(f"# of files:{str(num_files)}")

    os.mkdir(os.path.join(mypath, "JPG"))

    # TODO: separate this for loop in its own function
    for count, file in enumerate(files):
        source_file = f"{mypath}/{file}"
        img = Image(filename=source_file)
        img.format = "jpg"

        if ".HEIC" in file:
            new_file_name = mypath + "/JPG/" + file.replace(".HEIC", ".JPG")
        elif ".PNG" in file:
            new_file_name = mypath + "/JPG/" + file.replace(".PNG", ".JPG")

        img.save(filename=new_file_name)
        img.close()
        # TODO: use logger instead of print statements
        print("saved: " + file, "- ", str((count + 1) * 100 / num_files) + "%")


if __name__ == "__main__":
    main()
