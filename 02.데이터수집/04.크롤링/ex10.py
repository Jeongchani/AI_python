from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re, time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#options.add_argument('headless')

browser = webdriver.Chrome(options=options)
browser.maximize_window()
url='https://www.coffeebeankorea.com/store/store.asp'
browser.get(url)

browser.execute_script("storePop2(31)")
time.sleep(2)
soup = BeautifulSoup(browser.page_source, 'lxml')

#매장이름
name = soup.select('div.store_txt > h2')[0].string
info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
address = list(info[2])[0].string
phone = info[3].string
print('매장이름', name)
print('매장주소', address)
print('매장전화', phone)