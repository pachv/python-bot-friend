import requests
from bs4 import BeautifulSoup

weather_messages = [
    "какая погода",
    "погода",
    "какая сегодня погода"
]

debug = False

def get_current_weather():
    #weathertabs
    html = requests.get("https://pogoda.mail.ru/prognoz/voronezh/24hours/").text

    soup = BeautifulSoup(html,"lxml").find("span",{"class":"p-forecast__temperature-value"})

    return soup.text

if debug:
    print(get_current_weather())