from gtts import gTTS
import os
from time import sleep
import sys

tts = gTTS(text='TEXT', lang='en')
tts.save("song.mp3")
file = 'song.mp3'
