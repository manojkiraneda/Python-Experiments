from textblob import TextBlob
from gtts import gTTS
from pygame import mixer
import time
print(" 1.Hindi \n 2.Dutch \n 3.French \n 4.Gernman \n 5.Greek \n 6.Tamil")
language = int(raw_input("Enter a Language for Translation :"))
if language == 1:
    lan = 'hi'
elif language == 2:
    lan = 'nl'
elif language == 3:
    lan = 'fr'
elif language == 4:
    lan = 'de'
elif language == 5:
    lan = 'el'
else:
    lan = 'ta'

text_l = str(raw_input("Enter the String : "))
blob = TextBlob(text_l)
n_text = blob.translate(to=lan)
print n_text
tts = gTTS(text=text_l,lang=lan)
tts.save("hello.mp3")
time.sleep(5)
mixer.init()
mixer.music.load('/home/whoami/PycharmProjects/python_exp/hello.mp3')
mixer.music.play()
nothing = raw_input()

