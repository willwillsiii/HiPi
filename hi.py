from gtts import gTTS
from pygame import mixer

try:
    while True:
        line = input("TTS: ")
        fn = 'tmp'
        fp = ''.join(["lines/", fn, '.mp3'])
        tts = gTTS(text=line, lang='en')
        tts.save(fp)
        mixer.init()
        mixer.music.load(fp)
        mixer.music.play()
        while mixer.music.get_busy():
            pass
except KeyboardInterrupt:
    print("\nClosing ...")

