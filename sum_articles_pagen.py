import requests
from requests.sessions import Session
from bs4 import BeautifulSoup
import lxml

base_url = 'https://parsinger.ru/html/'
base_url_elem = 'https://parsinger.ru/html/index3_page_'
sess = requests.Session()
response = sess.get('https://parsinger.ru/html/index3_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')
len_ = len(soup.find('div', class_='pagen').find_all('a'))
glob_ans = 0


def sum_of_page(list_of_href):
    ans = 0
    for el in list_of_href:
        micro_url = el.find('a')['href']
        url = f'{base_url}{micro_url}'
        response = sess.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        ans += int(soup.find('p', class_='article').text.split(' ')[1])
    return ans


for elem in range(len_):
    url = f'{base_url_elem}{elem+1}.html'
    response = sess.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    list_of_href = soup.find_all('div', class_='sale_button')
    glob_ans += sum_of_page(list_of_href)

print(glob_ans)



