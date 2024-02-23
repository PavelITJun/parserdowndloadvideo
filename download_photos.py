import requests

base_url='https://parsinger.ru/img_download/img/ready/'
save_dir = "C:/Users/PC/Desktop/parser/photosparser/"
sess = requests.Session()
for i in range(1, 161):
    url = f'{base_url}{i}.png'
    file_dir = f'{save_dir}{i}.png'
    with open(file_dir, 'wb') as f:
        response = sess.get(url=url)
        f.write(response.content)
