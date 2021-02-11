import cv2
import time

class ImageProcessor():
 
    def __init__(self, video_source):

        if video_source.isnumeric():
            video_source = int(video_source)

        self.cap = cv2.VideoCapture(video_source)
    
    def get_image(self):
        ret, img = self.cap.read()
        ret, buffer = cv2.imencode('.jpg', img)
        return buffer.tobytes()

    def close(self):
        self.cap.release()