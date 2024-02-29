import requests
from bs4 import BeautifulSoup
import lxml
from requests.sessions import Session

sess = requests.Session()
base_url = 'https://parsinger.ru/html/index3_page_' #1.html
response = sess.get("https://parsinger.ru/html/index3_page_1.html")
soup = BeautifulSoup(response.text, 'lxml')
ans = []
len_ = len(soup.find('div', class_='pagen').find_all('a'))
for el in range(len_):
    url = f'{base_url}{el+1}.html'
    helplist = []
    response = sess.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for i in soup.select('.name_item'):
        helplist.append(i.text)
    ans.append(helplist)
with open('output.txt', 'w', encoding='utf-8') as file:
    print(ans, file=file)