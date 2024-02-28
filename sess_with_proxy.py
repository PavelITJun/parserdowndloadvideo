import requests

url = "https://httpbin.org/ip"
proxies = {
    'http': 'socks5://8ZYk5H:XfMpg7@10.10.36.159:8000',
    'https': 'socks5://Kx4Jcj:h4Ch0N@10.10.51.205:8000',
}

# Создаем сессию
session = requests.Session()

# Устанавливаем прокси для сессии
session.proxies.update(proxies)

# Делаем запрос
response = session.get(url)

print(response.text)