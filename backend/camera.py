import cv2
import numpy as np


class VideoCamera(object):
    face_cascade_path = './cascades/haarcascade_frontalface_default.xml'

    def __init__(self):
        self.video = cv2.VideoCapture(0)

        # Opencvのカメラをセットします。(0)はノートパソコンならば組み込まれているカメラ

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        frame = self._resize_image(frame)
        frame = self._detect_face(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def _resize_image(self, image):
        (height, width, color) = np.shape(image)
        width = int(width / 4)
        height = int(height / 4)
        image = cv2.resize(image, (width, height))
        return image

    def _detect_face(self, frame):
        cascade = cv2.CascadeClassifier(self.face_cascade_path)
        faces = cascade.detectMultiScale(frame)

        if faces !=[]:
            for x, y, w, h in faces:
                end_x = x + w
                end_y = y + h
                color = (0, 0, 255)
                thickness = 1
                cv2.rectangle(frame, (x, y), (end_x, end_y), color, thickness)


        return frame
