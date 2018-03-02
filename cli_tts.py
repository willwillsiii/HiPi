#!/usr/bin/python3
from tts_player import play_tts
from pygame import mixer

mixer.init()
try:
    while True:
        line = input("TTS: ")
        play_tts(line, mixer)
except KeyboardInterrupt:
    print("\nClosing ...")

