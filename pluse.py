#무들
#주소=https://namu.wiki/w/Project%20Zomboid/%EB%AC%B4%EB%93%A4
#1번=여기는 이름,진행도,추가효과,설명 정도만 크롤링

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time

# ChromeDriver 경로 설정
chrome_driver_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs.exe'  # 실제 ChromeDriver 경로로 변경하세요


# 웹 드라이버 설정
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 창을 열지 않음
driver = webdriver.Chrome(service=service, options=options)
#webdriver.Chrome이거는 크롬 브라우저를 제어하는 클래스(Chrome 브라우저를 열고, 웹 페이지를 로드하며, 페이지 내의 요소를 찾고, 상호작용)
#service=service->Service 객체는 ChromeDriver 실행 파일의 위치를 지정하고, 추가 설정을 포함할 수 있습니다
#options=options->이를 통해 브라우저의 동작 방식을 설정할 수 있습니다. 예를 들어, headless 모드로 실행하거나 GPU를 비활성화하는 등의 옵션을 지정할 수 있습니다.

# 크롤링할 페이지로 이동
url = 'https://namu.wiki/w/Project%20Zomboid/%EB%AC%B4%EB%93%A4'
driver.get(url)

# 페이지 로딩 대기 (필요 시 조정)
time.sleep(5)

# 특정 요소 찾기
element = driver.find_element(By.CSS_SELECTOR, 'div._3mcaeaj8')

# 요소 위치와 크기 가져오기
location = element.location
size = element.size

# 전체 페이지 스크린샷 찍기
driver.save_screenshot('full_page_screenshot.png')

# 이미지 열기
image = Image.open('full_page_screenshot.png')

# 요소의 위치와 크기에 맞게 이미지 자르기
left = location['682.667']
top = location['204.500']
right = location['682.667'] + size['width']
bottom = location['204.500'] + size['height']

element_screenshot = image.crop((left, top, right, bottom))
element_screenshot.save('element_screenshot.png')

# 드라이버 종료
driver.quit()
