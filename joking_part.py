import requests
import random
from bs4 import BeautifulSoup

def random_joke()->str:
    req = requests.get("https://anekdotov.net/anekdot/")
    soup = BeautifulSoup(req.text, "html.parser")
    # собирает все теги с кламмои анекдот
    anekdots = soup.find_all('div', class_="anekdot")
    random.shuffle(anekdots)
    return anekdots[random.randrange(len(anekdots))].text

