import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹 드라이버를 초기화합니다.
driver = webdriver.Chrome()

# 웹 페이지를 로드합니다.
driver.get('https://namu.wiki/w/Project%20Zomboid/%EB%AC%B4%EB%93%A4')

# 캡처하려는 요소를 찾습니다.
elements = driver.find_elements(By.CLASS_NAME, '_3mcaeaj8')

# "images_1"라는 디렉토리가 없으면 생성합니다.
if not os.path.exists('images_1'):
    os.makedirs('images_1')

# 각 요소의 스크린샷을 찍습니다.
for i, element in enumerate(elements):
    if element.is_displayed() and element.size['width'] > 0 and element.size['height'] > 0:  # 웹 요소가 보이고, 크기가 0이 아닌지 확인합니다.
        element.screenshot(os.path.join("images_1", f"img_{i}.png"))

# 웹 드라이버를 종료합니다.
driver.quit()
