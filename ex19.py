import requests
from bs4 import BeautifulSoup

URL = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
req = requests.get(URL)
soup = BeautifulSoup(req.content, 'html5lib')
h2Data = soup.findAll('p')

for i in h2Data:
  print(i.text)