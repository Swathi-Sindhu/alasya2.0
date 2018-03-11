import requests
import re
from gtts import gTTS
import os


def genkeyw(text):
    keygen={'buddy','hey', 'who', 'where', 'with', "what's", 'of', 'for', 'at', 'want', 'to', 'me', 'can', 'what', 'when', 'why', 'is', 'am', 'on', 'it', 'if', 'a', 'an', 'the', 'in','are', 'were', 'now', 'my','how', 'you', 'your', 'i'}
    text=text.split()
    s=set(text)
    s=s-keygen
    print(s)
    return s

def sayweather(address):
    api_key = "AIzaSyC-PM-difZHAVazccuVY0jymsI-sgvugqg"
    api_response = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        print('Latitude:', latitude)
        print('Longitude:', longitude)

    lat = str(latitude) + ',' + str(longitude)
    print(lat)
    lin = "https://weather.com/en-IN/weather/today/l/"
    link = lin + lat
    f = requests.get(link)
    # print(f.text)
    a = f.text
    b = a.find('<span class="styles-xz0ANuUJ__temperature__3Ph8k">')
    # print(b)
    temp = ""
    for i in range(50, 53):
        if f.text[b + i] == '<':
            break
        temp = temp + f.text[b + i]

    output = "the temperature at " + address + "is" + temp + " degree centigrade"
    print(temp + " degree centigrade")

    tts = gTTS(text=output, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")



def saynews():
    link = "https://news.google.com/news/?ned=in&gl=IN&hl=en-IN"
    f = requests.get(link)

    a = f.text
    news = ''
    b = a.find('jsname="NV4Anc" role="heading" aria-level="2"')

    regex = r'jsname="NV4Anc" role="heading" aria-level="2"(.+?)<'
    # line = "President [P] Barack Obama [/P] met Microsoft founder [P] Bill Gates [/P], yesterday."
    newslist = re.findall(regex, a)
    print(newslist)
    newsfin = ''
    for i in range(0, 5):
        newstr = newslist[i].replace(">", "")
        newstr2 = newstr.replace("&#39;", "'")
        newsfin = newsfin + '     ;' + newstr2
    newsfin = 'here are the latest top stories for now  ' + newsfin
    tts = gTTS(text=newsfin, lang='en-us')
    tts.save("hel.mp3")
    os.system("mpg321 hel.mp3")


def priceof(term):
    tabUrl = "https://www.flipkart.com/search?q=";
    link = tabUrl + term
    f = requests.get(link)
    new = 2
    a = f.text
    b = a.find("1vC4OE _2rQ-NK")
    c = a.find("_3wU53n")
    if b == -1:
        b = a.find('1vC4OE"')
        c = a.find("_2cLu-l")
        name = ""
        for i in range(16, 100):
            if f.text[c + i] == '<' or f.text[c + i] == '>' or f.text[c + i] == '"':
                break
            name = name + f.text[c + i]
        price = ""
        for i in range(96, 120):
            if f.text[b + i] == '<' or f.text[b + i] == '>' or f.text[b + i] == '"':
                break
            price = price + f.text[b + i]
        if price == 'refetch':
            output = "NO RESULTS FOUND FOR YOUR QUERY"
            print(output)
            tts = gTTS(text=output, lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
        else:
            output = name + " costs " + price + " rupees"
            print(output)
            tts = gTTS(text=output, lang='en-us')
            tts.save("hel.mp3")
            os.system("mpg321 hel.mp3")
    else:
        name = ""
        for i in range(28, 130):
            if f.text[c + i] == '<' or f.text[c + i] == '>' or f.text[c + i] == '"':
                break
            name = name + f.text[c + i]
        price = ""
        for i in range(104, 120):
            if f.text[b + i] == '<' or f.text[b + i] == '>' or f.text[b + i] == '"':
                break
            price = price + f.text[b + i]
        output = "the price of " + name + " on flipkart is " + price + " rupees"
        print(output)

        tts = gTTS(text=output, lang='en-us')
        tts.save("hel.mp3")
        os.system("mpg321 hel.mp3")









