import os
import requests

url = "https://parsinger.ru/video_downloads/videoplayback.mp4"
response = requests.get(url=url, stream=True)
with open("file.mp4", 'wb') as file:
    for piece in response.iter_content(chunk_size=100000):
        file.write(piece)
file_size = os.path.getsize(filename="file.mp4")
print(round(file_size/1000000))