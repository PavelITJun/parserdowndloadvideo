import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get(url='https://parsinger.ru/4.1/1/index6.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
sibling = soup.find(attrs={"id": "section3"})
print(sibling)
