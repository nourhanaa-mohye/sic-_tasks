from gpiozero import Servo
import Adafruit_DHT
import logging
import datetime
import time
sensor = Adafruit_DHT.DHT11
pin = 4
servo = Servo(27)
now = datetime.datetime.now()
logging.basicConfig(filename="time-pub.log",
                                format='%(asctime)s %(message)s', 
                                filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
print("d")
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity>
    if temperature > 30:
        print("run")
if temperature > 30:
        print("run")
        servo.max()
        logger.info(f"{now} ,{humidity},{ temperature} \n") 
    else:
        servo.min()
        print("stop")
        logger.info(f"{now}  \n") 
