import requests

sess = requests.Session()
st_codes = []
for x in range(1, 101):
    url = f"https://parsinger.ru/3.3/4/{x}.html"
    response = sess.get(url=url)
    st_codes.append(response.status_code)

print(f"Первая доступная страница: {st_codes.index(200)+1}.html\n"
      f"Последняя доступная страница: {len(st_codes)-st_codes[::-1].index(200)}.html")
