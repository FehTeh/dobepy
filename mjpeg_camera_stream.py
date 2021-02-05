import sys
from flask import Flask, Response
from mjpeg.server import MJPEGResponse
from image_processor_task import ImageProcessorTask

app = Flask(__name__)
camera = 0

def relay():
    while True:
        yield t.get_image()

@app.route('/image.jpg')
def image():
    return Response(t.get_image(),  mimetype='image/jpg')

@app.route('/video/mjpg.cgi')
def video():
    return MJPEGResponse(relay())

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        camera = sys.argv[1]
         
    t = ImageProcessorTask(camera)
    t.start()

    app.run(host='0.0.0.0', port=8080)
    print("exiting")
    t.join()