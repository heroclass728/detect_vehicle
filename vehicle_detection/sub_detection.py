import cv2
import os

from settings import VEHICLE_LABEL, CUR_DIR, OUTPUT_DIR


class SubDetection:

    def __init__(self):

        self.model_path = os.path.join(CUR_DIR, 'utils', 'frcnn_inception_v2.pb')
        self.graph_path = os.path.join(CUR_DIR, 'utils', 'frcnn_inception_v2_graph.pbtxt')
        self.output_dir = OUTPUT_DIR

    def detect_cars_image(self, frame_path):

        cvNet = cv2.dnn.readNetFromTensorflow(self.model_path, self.graph_path)

        frame = cv2.imread(frame_path)
        frame_height = frame.shape[0]
        frame_width = frame.shape[1]
        cvNet.setInput(cv2.dnn.blobFromImage(frame, size=(300, 300), swapRB=True, crop=False))
        cvOut = cvNet.forward()

        index = 0
        for detection in cvOut[0, 0, :, :]:

            score = float(detection[2])
            label = int(detection[1])
            if label in VEHICLE_LABEL and score > 0.3:

                left = detection[3] * frame_width
                top = detection[4] * frame_height
                right = detection[5] * frame_width
                bottom = detection[6] * frame_height

                vehicle_img = frame[top:bottom, left:right]
                vehicle_img_path = os.path.join(self.output_dir, 'image_{}.jpg'.format(index))
                cv2.imwrite(vehicle_img_path, vehicle_img)
                index += 1

        return
