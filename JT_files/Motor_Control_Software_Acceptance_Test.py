from board import SCL, SDA
import busio
import time
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c_bus = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50
servo0 = servo.Servo(pca.channels[0], min_pulse=900, max_pulse=2100)
servo1 = servo.Servo(pca.channels[1], min_pulse=900, max_pulse=2100)
servo2 = servo.Servo(pca.channels[2], min_pulse=900, max_pulse=2100)
servo3 = servo.Servo(pca.channels[3], min_pulse=900, max_pulse=2100)

angle0 = 45
angle1 = 90
angle2 = 120
angle3 = 180

servo0.angle = angle0
print('Servo 0 is at angle %s'%str(angle0))

servo1.angle = angle1
print('Servo 1 is at angle %s'%str(angle1))

servo2.angle = angle2
print('Servo 2 is at angle %s'%str(angle2))

servo3.angle = angle3
print('Servo 3 is at angle %s'%str(angle3))