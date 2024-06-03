#직업
#주소=https://namu.wiki/w/Project%20Zomboid/%EC%A7%81%EC%97%85
#스킬
#주소=https://namu.wiki/w/Project%20Zomboid/%EC%8A%A4%ED%82%AC
#특성
#주소=https://namu.wiki/w/Project%20Zomboid/%EC%8A%A4%ED%82%AC
#무들
#주소=https://namu.wiki/w/Project%20Zomboid/%EB%AC%B4%EB%93%A4
#아이템
#총기류 · 근접무기 · 식량과 요리 · 의복, 차량과 정비 · 건축과 가구


import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.webdriver.common.by import By
import time

#---------------------------------------------------------------------------------------------------

web=webdriver.Chrome()

url='https://namu.wiki/w/Project%20Zomboid/%EC%A7%81%EC%97%85'

web.get(url)



#BeautifulSoup과 requests를 사용하면 먼저 URL에 요청을 보내서 응답 객체를 얻은 다음, 그 응답 객체의 텍스트 내용을 접근해야 합니다.

get_screen_height=web.execute_script("return window.screen.height;")#이렇게 해서 원도우의 높이를 가져오기

#---------------------------------------------------------------------------------------

titttle_주소=[]
i=1
while True:
    i+=1

    time.sleep(0.5)

    web.execute_script(f"window.scrollTo(0, {get_screen_height * i});")
    
    all_of_bodt_hight= web.execute_script("return document.body.scrollHeight;")#<body>의 길이 즉 전체 길이를 확인하기 위한것

    job_elements = web.find_elements(By.CSS_SELECTOR, "_2It+ncon")

    if job_elements is None:
        print("없어")
    else:
        print(job_elements)
        titttle_주소.append(job_elements)

    if all_of_bodt_hight<=get_screen_height * i:
        break

#--------------------------------------------------------------------------------------------------------

#job_elements = web.find_elements(By.CSS_SELECTOR, ".LO99Tgas")
#for job_element in job_elements:
#e    print(job_element.text)



web.quit()

print("내가 추가했다")

