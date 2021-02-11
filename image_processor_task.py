import cv2
import threading
import time

class ImageProcessorTask(threading.Thread):
    die = False
    
    def __init__(self, video_source):
        super(ImageProcessorTask, self).__init__()

        if video_source.isnumeric():
            video_source = int(video_source)

        self.cap = cv2.VideoCapture(video_source)
    
    def run(self,*args,**kwargs):
        while not self.die:
            ret, img = self.cap.read()

            if not ret:
                print('no image from camera')
                time.sleep(1)
                continue

            ret, buffer = cv2.imencode('.jpg', img)
            self.img = buffer.tobytes()
        self.cap.release()
    
    def join(self):
        self.die = True
        super().join()

    def get_image(self):
        return self.img