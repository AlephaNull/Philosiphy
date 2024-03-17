import random 
from bs4 import BeautifulSoup
from pyfiglet import Figlet
import requests 

f = Figlet(font="small")
page = requests.get("https://www.goodreads.com/quotes/tag/philosophy")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text;

quotes = soup.select("div.quoteText")

quote = []
for elem in quotes:
    quote.append(elem.text)


final = random.choice(quote)
print(f.renderText(final))
