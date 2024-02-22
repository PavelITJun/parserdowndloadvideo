import requests
from random import choice

ips = ["223.113.80.158:9091", "188.132.222.70:8080", '195.226.122.82:80']
sess = requests.Session()
ans = 0
for el in range(1, 201):
    url = f'https://parsinger.ru/3.3/2/{el}.html'
    ip = choice(ips)
    proxy = {'http': f'http://{ip}',
            'https': f'https://{ip}'}
    try:
        response = sess.head(url=url)
        ans += response.status_code
    except Exception as e:
        continue

print(ans)
