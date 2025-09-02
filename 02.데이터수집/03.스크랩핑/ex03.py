import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')

top5 = soup.find('div', attrs={'class':'aside_area aside_popular'}).tbody
names =top5.find_all('tr')
print(len(names))

for name in names:
   
    name = name.find('a')
    #print(name)

    if name:
        print(name.get_text())