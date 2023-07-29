import requests
from bs4 import BeautifulSoup

debug = False

def translate_english_to_russian(phrase):
    url = "https://www.translate.ru/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9/" + phrase
    html = requests.get(url).text
    soup = BeautifulSoup(html,"lxml").find_all('span',{"class":"sayWord"})
    
    return soup[1:]

def traslate_russian_to_english(phrase):
    url = "https://www.translate.ru/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9/" + phrase
    html = requests.get(url).text
    soup = BeautifulSoup(html,"lxml").find_all('span',{"class":"sayWord"})
    
    return soup[1:]

if debug:
    res = traslate_russian_to_english("как дела")
    for item in res:
        print(item.text)