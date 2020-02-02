import os
import glob
import cv2

from settings import INPUT_DIR
from vehicle_detection.sub_detection import SubDetection


class MainDetection:

    def __init__(self):

        self.input_dir = INPUT_DIR
        self.sub_detection = SubDetection()

    def main_detect(self):

        vehicle_image_paths = glob.glob(os.path.join(self.input_dir, "*.jpg"))
        index = 0
        for vehicle_image_path in vehicle_image_paths:

            frame = cv2.imread(vehicle_image_path)
            index = self.sub_detection.detect_cars_image(frame=frame, idx=index)
