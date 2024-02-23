import requests

response = requests.get(url='https://parsinger.ru/3.4/1/json_weather.json')
list = response.json()
min_ = 100
ans = ''
for el in range(len(list)):
    if int(list[el]['Температура воздуха'].split('°')[0]) < min_:
        min_ = int(list[el]['Температура воздуха'].split('°')[0])
        ans = list[el]['Дата']

print(ans)