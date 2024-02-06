from selenium import webdriver
from bs4 import BeautifulSoup

# 1. 웹 드라이버 초기화 및 웹사이트 열기
driver = webdriver.Chrome('c:\\users\\ghkdt\\appdata\\local\\programs\\python\\python312\\lib\\site-packages\\chromedriver.exe')

driver.get("https://cse.yu.ac.kr/cse/community/notice.do")

# 2. 웹사이트의 HTML 소스코드 Parsing
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
container = soup.select("div.b-title-box")

title =[]
links = []
for con in container:
    t = con.select_one("a > span").text.strip()
    link = con.select_one("a")['href']
    
    title.append(t)
    links.append('https://cse.yu.ac.kr' + link)

# 각 공지사항의 내용도 파싱
for i in range(len(links)):
    # 공지사항의 URL로 이동
    driver.get(links[i])

    # HTML 소스코드 파싱
    html_content = driver.page_source
    soup_content = BeautifulSoup(html_content, "html.parser")

    # 내용 파싱
    content = soup_content.select_one("div.b-arti").text.strip()

    # 제목, URL, 내용 출력
    print('제목:', title[i])
    print('URL:', links[i])
    print('내용:', content)
    print('\n')

# 3. 웹 드라이버 종료
driver.quit()
