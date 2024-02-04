import requests
from bs4 import BeautifulSoup

# 1. 웹에서 데이터 가져오기 : 영남대 컴퓨터공학과 공지사항 사이트
raw = requests.get("https://cse.yu.ac.kr/cse/community/notice.do")

# 2. 웹사이트의 HTML 소스코드 Parsing
html = BeautifulSoup(raw.text, "html.parser")
container = html.select("div.b-title-box")

title =[]
for con in container:
    t = con.select_one("a > span").text.strip()
    title.append(t)
print(title)