## Overview

This project is to detect all the vehicles including car, truck, etc in the images and video stream, crop each vehicle 
from the image or frame and save it to the output directory.

# Project Structure

- input

    There are input images or video frames in it.

- output

    The detected result images are saved with the autoincrement id.

- training_dataset
    
    The image files and xml files extracted from the output directory. When looking at the images in the output 
    directory, there are both clear images and blur images which can not be recognized and be useful for training, so 
    the blur images must be deleted in manually. That's why after doing delete performance, it is necessary to collect 
    the image in the output directory again useful for training.
    
- utils
    
    * file concerned with folder and file manager functionality.
    * model necessary for training (.pb, .pbtxt, .config). The model to be used in this project is frcnn_inception_v2
    * training_img: perform the functionality to copy the useful images from output directory to training_dataset 
    directory.

- vehicle_detection

    The main source to detect the vehicles

- main
    
    The main execution file

- requirements
    
    All the libraries and frameworks for this project.
    
- settings

    Several settings are set.

## Project Installation

- Environment

    Ubuntu 18.04, python 3.6

- Library installation

    In the directory of this project, please execute the following command in terminal.
    ```
        pip3 install -r requirements.txt
    ```
- Download frcnn_inception_v2 pb and pbtxt file from https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md and
make config file from these two files by referencing https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API

## Project Execution

- Please copy the images or video frames for vehicle detection in the input directory.

- In settings, you can set whether you will parse video or image with VIDEO variable.

- In terminal run the following command.

    ```
        python3 main.py
    ``` 
