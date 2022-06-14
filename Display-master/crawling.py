import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com'

headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"}

response = requests.get(url, headers=headers) #url주소에 있는 html을 가져온다.

html = response.text
soup = BeautifulSoup(html, 'html.parser') # html을 분석할 수 있도록 준비

title=soup.select('#main_content > div.list_body.newsflash_body > ul > li > a')
#제목 가져오기 (ui, li태그의 child는 모두 삭제하고 실행)

for titles in title:
    print(titles.text)
    print(titles['href']) #뉴스링크 출력


