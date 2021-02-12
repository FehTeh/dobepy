import cv2
import threading
import wsgiserver
from flask import Flask, Response
from dobe_config import *

class Dobe_API():
    def __init__(self):
        config = Dobe_Config()
        self.cap = cv2.VideoCapture(config.video_source)

    def open_door(self):
        print("opening")
    
    def show_screen(self):
        print("showing screen")
    
    def get_video_frame(self):
        _, frame = self.cap.read()
        return frame
    
    def mute(self):
        print("muted")

    def volumeUp(self):
        print("volume up")
    
    def volumeDown(self):
        print("volume down")

class Dobe_API_HTTP():
    def __init__(self, api):
        self.api = api
        self.app = Flask(__name__)
        self.config = Dobe_Config()
        self.app.add_url_rule('/image.jpg', 'image', self.image)
        self.app.add_url_rule('/video/mjpg.cgi', 'video', self.video)
        
        wst = threading.Thread(target=self.start_api)
        wst.daemon = True
        wst.start()

    def start_api(self):
        server = wsgiserver.WSGIServer(self.app, host='0.0.0.0', port=self.config.api_port)
        print("API listening at http://0.0.0.0:" + str(self.config.api_port))
        server.start()

    def image(self):
        ret, buffer = cv2.imencode('.jpg', self.api.get_video_frame())
        return Response(buffer.tobytes(), mimetype='image/jpg')
    
    def video(self):
        def relay():
            while True:
                ret, buffer = cv2.imencode('.jpg', self.api.get_video_frame())
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

        return Response(relay(), mimetype='multipart/x-mixed-replace; boundary=frame')