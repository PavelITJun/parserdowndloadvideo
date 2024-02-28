from bs4 import BeautifulSoup
import lxml
import requests
import html5lib

# Пример 1. Передача файла HTML напрямую без использования менеджера контекста
file = open('index.html', encoding='utf-8')
soup = BeautifulSoup(file, 'lxml')
file.close()
print("Анализ файла без использования менеджера контекста:\n", soup)

# Пример 2. Передача файла HTML с использованием менеджера контекста
with open('index.html', 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')
    #print("Анализ файла с использованием менеджера контекста:\n", soup2)