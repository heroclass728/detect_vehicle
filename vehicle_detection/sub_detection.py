import cv2
import os

from settings import VEHICLE_LABEL, CUR_DIR, OUTPUT_DIR, IMAGE_MAX_HEIGHT, IMAGE_MAX_WIDTH


class SubDetection:

    def __init__(self):

        self.model_path = os.path.join(CUR_DIR, 'utils', 'frcnn_inception_v2.pb')
        self.graph_path = os.path.join(CUR_DIR, 'utils', 'frcnn_inception_v2_graph.pbtxt')
        self.output_dir = OUTPUT_DIR

    def detect_cars_image(self, frame, idx):

        cvNet = cv2.dnn.readNetFromTensorflow(self.model_path, self.graph_path)

        frame_height = frame.shape[0]
        frame_width = frame.shape[1]
        cvNet.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True, crop=False))
        cvOut = cvNet.forward()

        index = idx
        for detection in cvOut[0, 0, :, :]:

            score = float(detection[2])
            label = int(detection[1])
            if label in VEHICLE_LABEL and score > 0.3:

                left = int(detection[3] * frame_width)
                top = int(detection[4] * frame_height)
                right = int(detection[5] * frame_width)
                bottom = int(detection[6] * frame_height)

                vehicle_img = frame[top:bottom, left:right]
                vehicle_image_width = vehicle_img.shape[1]
                vehicle_image_height = vehicle_img.shape[0]

                if vehicle_image_width > IMAGE_MAX_WIDTH or vehicle_image_height > IMAGE_MAX_HEIGHT:

                    resize_ratio = 1
                    if vehicle_image_width > IMAGE_MAX_WIDTH:

                        resize_ratio = IMAGE_MAX_WIDTH / vehicle_image_width
                    elif vehicle_image_height > IMAGE_MAX_HEIGHT:

                        resize_ratio = IMAGE_MAX_HEIGHT / vehicle_image_height

                    resized_vehicle_image = cv2.resize(vehicle_img, None, fx=resize_ratio, fy=resize_ratio,
                                                       interpolation=cv2.INTER_CUBIC)
                else:

                    resized_vehicle_image = vehicle_img

                vehicle_img_path = os.path.join(self.output_dir, 'image_{}.jpg'.format(index))
                cv2.imwrite(vehicle_img_path, resized_vehicle_image)
                print("Saved {}".format(vehicle_img_path))
                index += 1

        return index
