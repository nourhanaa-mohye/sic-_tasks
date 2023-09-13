#liberraies

from gpiozero import DistanceSensor ,LED ,Servo ,Buzzer
from time import sleep
from picamera import PiCamera

 #pins
 ultrasonic = DistanceSensor(echo=21 ,trigger =20)
 camera = PiCamera()

#loop
 while True:

#condtion
    if ultrasonic.distance *100 >50:
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/image.jpg')
        camera.stop_preview()
    elif ultrasonic.distance *100 <50:
        camera.start_preview()
        for i in range(5):
            sleep(5)
            camera.capture('/home/pi/Desktop/image%s.jpg' % i)
        camera.stop_preview()
     elif ultrasonic.distance * 100  <20:
         camera.start_preview()
         camera.start_recording('/home/pi/Desktop/video.h264')
         sleep(5)
         camera.stop_recording()
         camera.stop_preview()
    sleep(2)



    sleep(2)
