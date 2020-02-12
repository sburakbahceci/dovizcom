import requests
from bs4 import BeautifulSoup

url="https://kur.doviz.com"

response=requests.get(url)

html_icerik=response.content

soup=BeautifulSoup(html_icerik,"html.parser")

print(soup.find_all("td"))