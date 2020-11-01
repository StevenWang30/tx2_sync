import Jetson.GPIO as GPIO
import time as time          #引用需要用的库
lidar_trigger = 11
camera_trigger = 13
GPIO.setmode(GPIO.BOARD)
# GPIO.setup(lidar_trigger, GPIO.OUT)
# GPIO.setup(camera_trigger, GPIO.OUT)
#
# trig = 0
#
# try:
#     while (True):
#         if trig % 10 == 0:
#             GPIO.output(lidar_trigger, GPIO.HIGH)
#         GPIO.output(camera_trigger, GPIO.HIGH)
#         time.sleep(0.1)
#
#         GPIO.output(lidar_trigger, GPIO.LOW)
#         GPIO.output(camera_trigger, GPIO.LOW)
#
#         trig += 1
# except KeyboardInterrupt:
#     GPIO.cleanup()
#


GPIO.setup(lidar_trigger, GPIO.OUT, initial=GPIO.HIGH)
l_t = GPIO.PWM(lidar_trigger, 50)	# 50Hz
l_t.start(25)	# 25% duty cycle

GPIO.setup(camera_trigger, GPIO.OUT, initial=GPIO.HIGH)
c_t = GPIO.PWM(camera_trigger, 50)	# 50Hz
c_t.start(25)	# 25% duty cycle

print("PWM running. Press CTRL+C to exit.")
try:
    while True:
        # p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0
        time.sleep(1)
finally:
    l_t.stop()
    c_t.stop()
    GPIO.cleanup()
