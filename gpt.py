from selenium import webdriver
from selenium.webdriver.common.by import By

# Selenium WebDriver로 브라우저 열기
driver = webdriver.Chrome()

# 직업 페이지 URL
url = 'https://namu.wiki/w/Project%20Zomboid/%EC%A7%81%EC%97%85'

# 페이지 열기
driver.get(url)

# 스크립트 실행하여 화면의 높이 가져오기
get_screen_height = driver.execute_script("return window.screen.height")

# 직업 정보 가져오기
job_elements = driver.find_elements(By.CSS_SELECTOR, ".LO99Tgas")
for job_element in job_elements:
    print(job_element.text)

# 브라우저 닫기
driver.quit()






