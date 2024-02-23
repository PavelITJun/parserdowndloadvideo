import requests

response = requests.get(url='https://parsinger.ru/3.4/3/dialog.json')
respdict = response.json()
ans = {}


def rec(dic):
    if dic['comments']:
        for el in range(len(dic['comments'])):
            rec(dic['comments'][el])
    if dic['username'] not in ans:
        ans[dic['username']] = 0
    if dic['username'] in ans:
        ans[dic['username']] += 1
    return ans


unsans = rec(respdict)
unsans = dict(sorted(unsans.items(), key=lambda i: (-i[1], i[0])))
print(unsans)