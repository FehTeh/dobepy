# MJPEG Camera Stream
Stream your webcam over mjpeg protocol

## Getting Started

To run: `python3 mjpeg_camera_stream.py`

Now the video is available at: `http://localhost:8080/video/mjpg.cgi`

And there is also another endpoint that returns a static image: `http://localhost:8080/image.jpg`

This will start using the first webcam found. To change add the camera location or try another number like: 
`python3 mjpeg_camera_stream.py 1`

### Dependencies

First, you'll need to install the dependencies via 'pip3'

`pip3 install -r requirements.txt`

### Curiosity

This project was done to stream a webcam/av-video-receiver to home-assistant. To add it go to home-assistant configuration.yml and add this:

```yml
camera:
  - platform: mjpeg
    name: <NAME>
    still_image_url: http://<IP>:<PORT>/image.jpg
    mjpeg_url: http://<IP>:<PORT>/video/mjpg.cgi
```
