import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

        # Opencvのカメラをセットします。(0)はノートパソコンならば組み込まれているカメラ

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image = self.resize_image(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def resize_image(self, image):
        (height, width,color) = np.shape(image)
        width = int(width/4)
        height = int(height/4)
        image = cv2.resize(image,(width,height))
        return image

