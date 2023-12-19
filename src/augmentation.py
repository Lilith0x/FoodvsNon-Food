import os
import pathlib
from os.path import isfile, join, isdir
from PIL import Image, ImageFilter

BASE_DIR = pathlib.Path(__file__).parent.parent
IMAGES_DIRNAME = 'data/raw/training'
IMAGES_DIR = BASE_DIR.joinpath(IMAGES_DIRNAME)
AUG_IMAGES_DIR = IMAGES_DIR


def blur_image(path_orig, path_dest):
    OriImage = Image.open(path_orig)
    blurImage = OriImage.filter(ImageFilter.BLUR)
    blurImage.save(path_dest)


def blur_images(counter=250):
    for directory in os.listdir(IMAGES_DIR):
        path_to_directory = str(join(IMAGES_DIR, directory))
        c: int = 0

        if isdir(path_to_directory):
            for image in os.listdir(path_to_directory):
                if c == counter:
                    break
                path_to_image = join(path_to_directory, image)
                if isfile(path_to_image):
                    aug_filename = 'aug_' + str(image)
                    orig_filepath = join(path_to_directory, str(image))
                    aug_filepath = join(path_to_directory, aug_filename)
                    blur_image(orig_filepath, aug_filepath)
                    c += 1


def make_augmentation():
    blur_images()


if __name__ == "__main__":
    make_augmentation()
