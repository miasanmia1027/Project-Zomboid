from bs4 import BeautifulSoup
import requests
import urllib.request
import os

# 웹사이트에서 HTML을 가져옵니다.
url = "https://namu.wiki/w/Project%20Zomboid/%EB%AC%B4%EB%93%A4"  # 크롤링하려는 웹사이트 URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 이미지 태그를 찾아 이미지 URL을 가져옵니다.
img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]

# 상대 경로를 절대 경로로 변환합니다.
urls = [urllib.parse.urljoin(url, img_url) for img_url in urls]

# "images"라는 디렉토리가 없으면 생성합니다.
if not os.path.exists('images'):
    os.makedirs('images')

# 이미지를 다운로드합니다.
for i, img_url in enumerate(urls):
    try:
        response = requests.get(img_url)
        with open(os.path.join("images", f"image_{i}.jpg"), "wb") as img_file:
            img_file.write(response.content)
    except Exception as e:
        print(f"An error occurred while downloading {img_url}: {e}")
        


#이거는 이미지를 다운로드 한것
