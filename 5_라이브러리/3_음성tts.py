# pip install gtts : 문자를 음성으로 변환해주는 라이브러리 
# pip install playsound==1.2.2 

from gtts import gTTS
from playsound import playsound
import os

# 경로를 현재 .py파일을 실행하는 경로로 이동
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요. 파이썬입니다."
tts = gTTS(text=text, lang='ko')
tts.save(r"hi.mp3")

playsound("hi.mp3")