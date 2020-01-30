import os
import glob

from settings import INPUT_DIR
from vehicle_detection.sub_detection import SubDetection


class MainDetection:

    def __init__(self):

        self.input_dir = INPUT_DIR
        self.sub_detection = SubDetection()

    def main_detect(self):

        vehicle_image_paths = glob.glob(os.path.join(self.input_dir, "*.jpg"))

        for vehicle_image_path in vehicle_image_paths:

            self.sub_detection.detect_cars_image(frame_path=vehicle_image_path)
