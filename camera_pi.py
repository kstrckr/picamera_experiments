from picamera import PiCamera
from time import sleep


with PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (3280, 2464)
    camera.exposure_mode = 'night'

    for i in range(5):
        sleep(0.5)
        shutter_speed = camera.shutter_speed
        camera.annotate_text = shutter_speed
        camera.capture('./image%s.jpg' % i)
