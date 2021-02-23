# 어지간한 메이저 웹사이트뒤에 /robots.txt 치면 crawling 정책 표시
# chrome plugin web scraper > scraping가능한 부분들 보여줌 혹은 no-code scraping
# beautiful soup 사용 pip3 install beautifulsoup4
# request library 필요 pip3 install requests
import requests
from bs4 import BeautifulSoup
import pprint  # pretty print

res = requests.get('https://news.ycombinator.com/news')  # html 받아옴
# print(res)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find(id='score_26222530'))
# print(soup.select('.score'))  # css 선택자
# print(soup.select('.storylink')[0])
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = votes[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# print(create_custom_hn(links, subtext))
# pprint.pprint(create_custom_hn(links, subtext))


def hackerNewsCrawling():
    cnt = 0
    li = []
    sub = []
    while True:
        url = 'https://news.ycombinator.com/news?p=' + str(cnt)
        req = requests.get(url)  # html 받아옴
        result = BeautifulSoup(req.text, 'html.parser')
        if not result.select('.storylink'):
            break
        li.extend(result.select('.storylink'))
        sub.extend(result.select('.subtext'))
        cnt += 1

    pprint.pprint(create_custom_hn(li, sub))


hackerNewsCrawling()
