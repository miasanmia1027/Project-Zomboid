# import webdriver 
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time



# create webdriver object 
driver = webdriver.Chrome() 
  
# get google.co.in 
driver.get("https://namu.wiki/w/Project%20Zomboid/%EB%AC%B4%EB%93%A4") 

#element = driver.find_element(By.ID, "_3mcaeaj8")

#element.send_keys("Arrays")     여기 검색창에 다가 Arrays를 치게 하는것




get_screen_height=driver.execute_script("return window.screen.height;")

what_i_want=[]

i=1
while True:
    i+=1

    time.sleep(0.2)

    driver.execute_script(f"window.scrollTo(0, {get_screen_height * i});")
    
    all_of_bodt_hight= driver.execute_script("return document.body.scrollHeight;")

    content = driver.find_element(By.CLASS_NAME, '_3mcaeaj8')



    if content is None:
        print("없어")
    else:
        what_i_want.append(content)
        
    if all_of_bodt_hight<=get_screen_height * i:
        break
    
for _ in range(len(what_i_want)):
    text=what_i_want[_]
    print(text)




