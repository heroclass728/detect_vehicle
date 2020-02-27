from vehicle_detection.main_detection import MainDetection
from vehicle_detection.video_detection import get_vehicle_image_video
from settings import VIDEO


if __name__ == '__main__':

    if VIDEO:
        get_vehicle_image_video()
    else:
        MainDetection().main_detect()
