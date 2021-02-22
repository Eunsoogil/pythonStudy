# 어지간한 메이저 웹사이트뒤에 /robots.txt 치면 crawling 정책 표시
# chrome plugin web scraper > scraping가능한 부분들 보여줌 혹은 no-code scraping
# beautiful soup 사용 pip3 install beautifulsoup4
# request library 필요 pip3 install requests
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')  # html 받아옴
print(res)
print(res.text)
