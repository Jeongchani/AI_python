#[쿠팡]-[검색어]-[노트북] 1페이지 결과 상품이름, 상품가격
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

keyword='노트북'
url=f'https://www.gmarket.co.kr/n/search?keyword={keyword}'
browser.get(url)


browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(5)

from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')

items = soup.find_all('div', attrs={'class':'box__item-container'})
print(len(items))

browser.quit()
print('프로그램종료!')