# pip install selenium
# document에 별개의 virtual machine recommendation
# chrome driver 필요 https://sites.google.com/a/chromium.org/chromedriver/home
# latest stable release 설치

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
# print(chrome_browser) # 브라우저 켜짐

