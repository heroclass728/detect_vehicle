import cv2
import os
import glob

from settings import INPUT_DIR
from vehicle_detection.sub_detection import SubDetection


def get_vehicle_image_video():

    sub_detection = SubDetection()
    video_paths = glob.glob(os.path.join(INPUT_DIR, "*.mp4"))

    index = 0
    for video_path in video_paths:

        cap = cv2.VideoCapture(video_path)

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            index = sub_detection.detect_cars_image(frame=frame, idx=index)
            # Our operations on the frame come here

            # Display the resulting frame

        # When everything done, release the capture
        cap.release()
