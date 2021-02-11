import sys
from flask import Flask, Response
from image_processor import ImageProcessor

app = Flask(__name__)
camera = "0"

def relay():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + t.get_image() + b'\r\n')

@app.route('/image.jpg')
def image():
    return Response(t.get_image(), mimetype='image/jpg')

@app.route('/video/mjpg.cgi')
def video():
    return Response(relay(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        camera = sys.argv[1]

    t = ImageProcessor(camera)    

    app.run(host='0.0.0.0', port=8080)
    print("exiting")
    t.close()