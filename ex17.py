import requests
from bs4 import BeautifulSoup

URL = "https://www.nytimes.com/"
req = requests.get(URL)
soup = BeautifulSoup(req.content, 'html5lib')
h2Data = soup.findAll('h2')

for i in h2Data:
  print(i.text)

