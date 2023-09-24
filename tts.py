from gtts import gTTS
import os
from time import sleep
import sys

tts = gTTS(text='ТОЧИК БАЧА ПУТИН ПАЖАЛУСТА ПАМАГАЕТ ВСЕМ ТАДЖИК БЕДНЫЙ НУ НЕ КТО НЕ ПАМАГАЕТ НА ТАДЖИК ДЕНГИ НЕТУ ДЛЯ КУПИТЬ ПРАДУКТААААААА', lang='en')
tts.save("song.mp3")
file = '/storage/emulated/0/documents/pydroid3/song.mp3'