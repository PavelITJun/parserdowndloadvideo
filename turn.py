import requests
from itertools import cycle

# Список прокси
proxies_list = [
    {'http': 'http://223.113.80.158:9091', 'https': 'https://223.113.80.158:9091'},
    {'http': 'http://188.132.222.70:8080', 'https': 'https://188.132.222.70:8080'},
    {'http': 'http://195.226.122.82:80', 'https': 'https://195.226.122.82:80'},
]

proxy_pool = cycle(proxies_list)

url = "http://example.org"

# Создание сессии
session = requests.Session()

for i in range(1, 6):  # Попробуем сделать 5 запросов
    proxy = next(proxy_pool)
    session.proxies.update(proxy)  # Обновление прокси для сессии
    try:
        response = session.get(url, timeout=5)  # Используем сессию для выполнения запроса
        print(f"Request {i}: Success!")
    except requests.exceptions.RequestException as e:
        print(f"Request {i}: Failed, switching proxy. {proxy}")