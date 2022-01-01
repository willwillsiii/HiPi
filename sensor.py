#!/usr/bin/python3
import RPi.GPIO as GPIO
from tts_player import make_tts
from pygame import mixer

GPIO.setmode(GPIO.BOARD)
mixer.init()
mixer.music.load(make_tts("I'm Motion Detected!"))
try:
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print("Ready!")
    while True:
        GPIO.wait_for_edge(16, GPIO.RISING)
        mixer.music.play()
        print("Movement Detected!")
        GPIO.wait_for_edge(16, GPIO.FALLING)
        print("Ready!")
except KeyboardInterrupt:
    print("\nClosing ...")
finally:
    GPIO.cleanup()

