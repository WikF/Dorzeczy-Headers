from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import datetime


url = 'https://dorzeczy.pl/'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

filename = "dorzeczy.csv"
f = open(filename, "w")


headers = "Title | Time\n"

f.write(headers)

page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("a",{"class":"news-title"})
for i in containers:
    title = (i.span.text)
    time = str(datetime.datetime.now())
    f.write(title + " | " + time + "\n")
f.close()

print(f)
