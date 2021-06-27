import selenium
from selenium import webdriver
import time

URL = 'https://www.starbucks.co.kr/store/store_map.do'

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(url=URL)

time.sleep(5)
driver.find_element_by_css_selector('.btn_find_store').click() # 매장찾기 버튼
time.sleep(2)
driver.find_element_by_css_selector('.loca_search').click() # 지역검색 버튼

sidos = driver.find_elements_by_css_selector('.sido_arae_box li')


def back_to_sido():
    driver.find_element_by_css_selector('.btn_find_store').click() # 매장찾기 버튼
    time.sleep(0.5)
    driver.find_element_by_css_selector('.loca_search').click() 

for i in range(len(sidos)):
    sidos[i].click()
    time.sleep(0.3)
    gugun_count = len(driver.find_elements_by_css_selector('.gugun_arae_box li'))
    
    for j in range(1,gugun_count):
        time.sleep(1.5)
        gugun = driver.find_elements_by_css_selector('.gugun_arae_box li')[j]
        gugun.click()
        time.sleep(2)
        gugunName = driver.find_element_by_css_selector('.gugunSelectName').text
        storeCount = driver.find_element_by_css_selector('.en.t_006633.sidoSetResult').text
        print("\""+storeCount+"\"")
        print(str(gugunName)+"의 스타벅스수 : "+str(storeCount))
        try:
            alert = driver.swich_to_alert()
            print(alert.accept())
        except:
            pass

        back_to_sido()
        sidos = driver.find_elements_by_css_selector('.sido_arae_box li')
        sidos[i].click()
