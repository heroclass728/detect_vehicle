import os


def make_directory_if_not_exists(dir_path):

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    return dir_path
