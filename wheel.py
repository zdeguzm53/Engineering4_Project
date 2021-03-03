import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 100)
p.start(5)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.OUT)
GPIO.setwarnings(False)

while True:
  if GPIO.input(10) == GPIO.HIGH
         print("switch on")
         GPIO.output(11, GPIO.HIGH)

  p.ChangeDutyCycle(2.5)
  time.sleep(5)
  p.ChangeDutyCycle(11.5) # may need to be adjusted
  time.sleep(5)
  p.ChangeDutyCycle(20.5)
  time.sleep(5)
  p.ChangeDutyCycle(11.5) # may need to be adjusted

GPIO.cleanup()
