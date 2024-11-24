from bs4 import BeautifulSoup
import requests
import pandas as pd

file = 'sent.xlsx'

url = 'https://lesmeh.edu35.ru/images/rasp/Raspisanie/hg.htm'

response = requests.get(url).content
l1, l2, l3 = [], [], []

s = BeautifulSoup(response, 'lxml')
dat = s.find('table', class_='inf')
data = dat.find_all('tr')

for i in data:
    group = i.find_all('td', class_='hd')

for j in group:
    if j.find('a', class_='hd'):
        l1.append(j.find('a', class_='hd').text)

for j in data:
    if j.find('td', class_='ur'):
        l3.append(j.find('td', class_='hd').text)
        l2.append(j.find('td', class_='ur').find('a', class_='z1').text)
    
    elif j.find('td', class_='nul'):
        l2.append('Пар нет')
        l3.append(j.find('td', class_='hd').text)