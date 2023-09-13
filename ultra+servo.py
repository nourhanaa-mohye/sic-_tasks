#liberraies

from gpiozero import DistanceSensor ,LED ,Servo ,Buzzer
from time import sleep

 #pins
 ultrasonic = DistanceSensor(echo=21 ,trigger =20)
 servo= Servo(22)
 led_alarm =LED(23)
 alarm = Buzzer(24)

#loop
 while True:

#condtion
    if ultrasonic.distance *100 >50:
        servo.min()
    elif ultrasonic.distance *100 <50:
        servo.max ()
     elif ultrasonic.distance * 100  <20:
        alarm.on()
        led_alarm.on()
    sleep(2)



    sleep(2)
