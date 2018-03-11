import functionset
import speech_recognition as sr
from gtts import gTTS
import os
import random


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
res=r.recognize_google(audio)
print("You said: " + res)

if 'weather' in res or 'temperature' in res or 'climate' in res or 'how hot' in res or 'how cold' in res:
    res=functionset.genkeyw(res)
    res=res-{'temperature', 'climate', 'weather', 'hot', 'cold', 'hi', 'hello'}
    res=str(res)
    functionset.sayweather(res)
elif 'price' in res or 'rate' in res or 'how much' in res or 'cost' in res or 'costs' in res:
    res=functionset.genkeyw(res)
    res=res-{'cost', 'costs', 'rate', 'price', 'much', 'flipkart', 'amazon'}
    res=str(res)
    functionset.priceof(res)
elif 'news' in res or 'happening' in res or 'happenings' in res or 'going on' in res:
    functionset.saynews()
elif res=='hello' or res=='hi' or res=='hello buddy' or res=='hi buddy':
    option2=['hi','hello dear', 'hello', 'namaste', 'namaskaar']
    opt=option2[random.randint(0,4)]
    tts = gTTS(text=opt, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
    print(opt)
elif 'how do you do' in res:
    tts = gTTS(text='how do you do?', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'what' in res and 'you' in res and ('doing' in res or 'feeling' in res):
    option1=['i am always intrested to learn new thing. would you like to hear to an intresting fact?','just having a laugh. would you like to listen to a joke?','i am bored.wondering what to do']
    opt=option1[random.randint(0,2)]
    tts = gTTS(text=opt, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'how are you' in res:
    tts = gTTS(text='i am great. thanks for asking' or 'i am having a great day. thanks for asking', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'I' in res and ('bored' in res or 'bore' in res):
    tts = gTTS(text='here are the things i can do for you. play a game ,tell a joke, tell the news,and i can ask some riddles too', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'what' in res and 'can' in res and 'you' in res and 'do' in res:
    tts = gTTS(text='here are the things i can do for you. i can set alarms, remainder, create a shopping list or a to-do list for you, help chat with your friend, tell stories, play music , tell you the weather conditions, search for the prices of goods on flipkart, play a game ,tell a joke, tell the news,and i can ask some riddles too',lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif ('who' in res or 'why' in res)and 'made' in res and 'you' in res:
    tts = gTTS(text='i was made by the alasya group as a part of their ITWS2 software project ',lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'introduce' in res or 'introduction' in res:
    tts = gTTS(text='hello! i am the voice assistant created by alasya group. you can call me "buddy". i can speak in 19 different languages ,but "dont" ask me to do it now!. here are the things i can do. i can set alarms, remainder, create a shopping list or a to-do list for you, help chat with your friend, tell stories, play music , tell you the weather conditions, search for the prices of goods on flipkart, play a game ,tell a joke, tell the news,and i can ask some riddles too ',lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif ('how old' in res and 'you' in res) or ('your age' in res and ('what is' in res or "what's" in res)) or ('when' in res and 'you' in res and 'born' in res):
    tts = gTTS(text='technically ,as i dont have intelligence , i was never born and do not have an age', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif res=='Hey buddy' or res=='Hey' or res=='buddy':
    tts = gTTS(text='hey! hi. what can i do for you?  ', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'language' in res and 'you' in res and 'speak' in res:
    tts = gTTS(text='English for now', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'you' in res and 'like' in res and 'what' in res:
    option1=['I like talking with you','i am always interested in learning new things','Serving you gives me a great pleasure']
    opt=option1[random.randint(0,2)]
    tts = gTTS(text=opt, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'who' in res and 'are' in res and 'you' in res:
    tts = gTTS(text='i am buddy! the voice assistant designed by alasya team', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
elif 'where' in res and 'are' in res and 'you' in res:
    tts = gTTS(text='i am here! right in your computer.', lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")
else:
    tts = gTTS(text="sorry! i cannot do that", lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")