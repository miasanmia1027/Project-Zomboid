import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹 드라이버를 초기화합니다.
driver = webdriver.Chrome()

# 웹 페이지를 로드합니다.
driver.get('https://namu.wiki/w/Project%20Zomboid/%EC%95%84%EC%9D%B4%ED%85%9C/%EC%B4%9D%EA%B8%B0%EB%A5%98')

# 캡처하려는 요소를 찾습니다.
elements = driver.find_elements(By.CLASS_NAME, 'qp+Pt+zH')

# "gun_img"라는 디렉토리가 없으면 생성합니다.
if not os.path.exists('gun_img'):
    os.makedirs('gun_img')

# 각 요소의 스크린샷을 찍습니다.
for i, element in enumerate(elements):
    if element.is_displayed() and element.size['width'] > 0 and element.size['height'] > 0:  # 웹 요소가 보이고, 크기가 0이 아닌지 확인합니다.
        element.screenshot(os.path.join("gun_img", f"img_{i}.png"))

# 웹 드라이버를 종료합니다.
driver.quit()