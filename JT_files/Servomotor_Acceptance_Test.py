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

for i in range(180):
    servo0.angle = i
    time.sleep(0.01)
time.sleep(5)
for i in range(180):
    servo0.angle = 180 - i
    time.sleep(0.01)
time.sleep(1)

for i in range(180):
    servo1.angle = i
    time.sleep(0.01)
time.sleep(5)
for i in range(180):
    servo1.angle = 180 - i
    time.sleep(0.01)
time.sleep(1)

for i in range(180):
    servo2.angle = i
    time.sleep(0.01)
time.sleep(5)
for i in range(180):
    servo2.angle = 180 - i
    time.sleep(0.01)
time.sleep(1)

for i in range(180):
    servo3.angle = i
    time.sleep(0.01)
time.sleep(5)
for i in range(180):
    servo3.angle = 180 - i
    time.sleep(0.01)
time.sleep(1)