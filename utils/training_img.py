import glob
import os
import ntpath
import shutil

from settings import CUR_DIR, OUTPUT_DIR
from utils.folder_file_managment import make_directory_if_not_exists


def collect_training_images():

    train_data_output_dir = os.path.join(CUR_DIR, 'training_dataset', 'images')
    make_directory_if_not_exists(dir_path=train_data_output_dir)
    # delete_files_in_folder(folder=output_dir)

    training_image_paths = glob.glob(os.path.join(train_data_output_dir, "*.jpg"))
    if not training_image_paths:
        image_index = 0
    else:
        indexes = []
        for training_image_path in training_image_paths:

            file_parent_path, file_name = ntpath.split(training_image_path)
            base_name, extension = os.path.splitext(file_name)
            index = int(base_name[base_name.rfind("_") + 1:])
            indexes.append(index)
        image_index = max(indexes)

    image_paths = glob.glob(os.path.join(OUTPUT_DIR, 'image3', '*.jpg'))
    for image_path in image_paths:

        image_index += 1
        file_parent_path, file_name = ntpath.split(image_path)
        base_name, extension = os.path.splitext(file_name)
        new_file_name = base_name[:base_name.rfind("_")] + "_" + str(image_index) + extension
        new_file_path = os.path.join(train_data_output_dir, new_file_name)
        shutil.copy(image_path, new_file_path)



if __name__ == '__main__':

    collect_training_images()
