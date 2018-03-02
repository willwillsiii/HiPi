from gtts import gTTS

def play_tts(line, mixer):
    fp = make_tts(line)
    play_audio(fp, mixer)

def make_tts(line):
    fn = 'tmp'
    audio_dir = 'audio/'
    fp = ''.join([audio_dir, fn, '.mp3'])
    tts = gTTS(text=line, lang='en')
    tts.save(fp)
    return fp

def play_audio(fp, mixer):
    mixer.music.load(fp)
    mixer.music.play()
    while mixer.music.get_busy():
        pass

