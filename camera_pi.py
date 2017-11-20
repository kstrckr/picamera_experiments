from picamera import PiCamera
from time import sleep
from datetime import time 


with PiCamera() as camera:
    camera.rotation = 180
    camera.resolution = (3280, 2464)
    camera.exposure_mode = 'night'

    for i in range(1):
        sleep(0.5)
        shutter_speed_microseconds = camera.exposure_speed
        shutter_speed = time(microsecond=shutter_speed_microseconds) 
        print(shutter_speed.strftime('%S.%f'))
        camera.annotate_text = shutter_speed.strftime('%S.%f') 
        camera.capture('./image%s.jpg' % i)
