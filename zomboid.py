#직업
#주소=https://namu.wiki/w/Project%20Zomboid/%EC%A7%81%EC%97%85
#1번= 직업 이름
#2번=간단한 설명을 내가 요약하기
#3번장단점을 하이라이트 된 부분만 가져오기+설명이 이걸로 부족한경우 약간의 설명으로 추가
#4번=옆의 사진그자체를 가져오거나 정보를 추출하기
#특성
#주소=https://namu.wiki/w/Project%20Zomboid/%EC%8A%A4%ED%82%AC
#1번=조선부 특성을 머저 가져오기
#2번=긍정적특것 크롤링
#3번=부정적특성 클롤링
#4번=직업전용특성
#5번=확실하지 않운 미사용 틋성 크롤링
#무들
#주소=https://namu.wiki/w/Project%20Zomboid/%EB%AC%B4%EB%93%A4
#1번=여기는 이름,진행도,추가효과,설명 정도만 크롤링
#아이템
#총기류 · 근접무기 · 식량과 요리 · 의복, 차량과 정비 · 건축과 가구
#여기는 다 한 다음에 생각


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
