import requests
from requests.sessions import Session
from bs4 import BeautifulSoup
import lxml

base_url = 'https://parsinger.ru/html/'
sess = requests.Session()
response = sess.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')
len_of_pages = len(soup.find('div', class_='pagen').find_all('a'))
glob_ans = 0


def sum_of_page(list_of_href):
    ans = 0
    for el in list_of_href:
        micro_url = el.find('a')['href']
        url = f'{base_url}{micro_url}'
        response = sess.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        ans += int(soup.find('span', id='price').text.split(' ')[0]) *\
               int(soup.find('span', id='in_stock').text.split(': ')[1])
    return ans


def sum_of_cat(base_url_elem):
    global len_of_pages, glob_ans
    for elem in range(len_of_pages):
        url = f'{base_url_elem}{elem + 1}.html'
        response = sess.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        list_of_href = soup.find_all('div', class_='sale_button')
        glob_ans += sum_of_page(list_of_href)


for el in range(len(soup.find('div', class_='nav_menu').find_all('a'))):
    base_url_elem = f'https://parsinger.ru/html/index{el+1}_page_'
    sum_of_cat(base_url_elem)

print(glob_ans)
