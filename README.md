# Dobepy (Doorbell made with Python)
Doorbell interface and API made with python (Work In Progress)

## Getting Started

To run: `python3 dobe.py --console`

Now the video is available at: `http://localhost:8080/video/mjpg.cgi`

And there is also another endpoint that returns a static image: `http://localhost:8080/image.jpg`

To change the configuration go to the dobe.ini

### Dependencies

First, you'll need to install the dependencies via 'pip3'

`pip3 install -r requirements.txt`

### Curiosity

To add it go to home-assistant configuration.yml and add this:

```yml
camera:
  - platform: mjpeg
    name: <NAME>
    still_image_url: http://<IP>:<PORT>/image.jpg
    mjpeg_url: http://<IP>:<PORT>/video/mjpg.cgi
```
