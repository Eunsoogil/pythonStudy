# pip install selenium
# document에 별개의 virtual machine recommendation
# chrome driver 필요 https://sites.google.com/a/chromium.org/chromedriver/home
# latest stable release 설치

from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
# print(chrome_browser) # 브라우저 켜짐

chrome_browser.maximize_window()

#selenium test site
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# print('Selenium Easy Demo' in chrome_browser.title)  # true return
# assert 'Selenium Easy Demo' in chrome_browser.title  # assert : 만약 false return시 에러를 받음
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_button2 = chrome_browser.find_element_by_css_selector('#get-input > .btn')
print(user_button2)
user_message.clear()  # 기존 value를 지움
user_message.send_keys('work')
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'work' in output_message.text

# chrome_browser.close()  #버그가 있는 경우가 있음
chrome_browser.quit()  # 마찬가지로 버그가 있는 경우가 있음

# wait 기능 있음, 너무 빠르면 block 당하므로 일정시간 대기
