#!/usr/bin/python3
import RPi.GPIO as GPIO
from pygame import mixer

GPIO.setmode(GPIO.BOARD)
mixer.init()
mixer.music.load("lines/tmp.mp3")
try:
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print("Ready!")
    while True:
        GPIO.wait_for_edge(16, GPIO.RISING)
        mixer.music.play()
        print("Movement Detected!")
except KeyboardInterrupt:
    print("\nCloing ...")
finally:
    GPIO.cleanup()

