# Python 3.8.10
# pip 23.2.1
# selenium version 4.11.2 (selenimum 3버전에서는 오류 생김)
# chromedriver Version: 117.0.5938.92 (자기 pc의 크롬 버전에 맞게 설치)
# reference : https://www.youtube.com/watch?v=1b7pXC1-IbE
# selenium version error : https://stackoverflow.com/questions/77111127/how-can-we-download-chromedriver-117
# chromedriver download : https://lsw3210.tistory.com/entry/Selenium-%EC%8B%A4%ED%96%89%EC%8B%9C-Chrome-115-%EB%B2%84%EC%A0%84-%EB%AC%B8%EC%A0%9C-%ED%95%B4%EA%B2%B0
# find_element_by selenium high version(4) error : https://sualchi.tistory.com/13721870
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.common.by import By
import os
from urllib.request import urlretrieve

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q")
word = "가천대"
elem.send_keys(word)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.ID, ".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
count = 1
os.mkdir(word)

for image in images:

    try:
        image.click()
        time.sleep(1.5)
        print(str(count) + '-1')
        imgUrl = driver.find_element(By.XPATH,
                                     "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div["
                                     "2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]").get_attribute(
            "src")
        print(imgUrl)
        print(imgUrl.find('jpg'))
        if (imgUrl.find('jpg') < 0) and (imgUrl.find('jpeg') < 0):
            continue
        if imgUrl.find('costco') > 0:
            continue
        print(imgUrl)
        print(str(count) + '-2')
        opener = urllib.request.build_opener()
        print(opener)
        print(str(count) + '-3')
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        print(opener.addheaders)
        print(str(count) + '-4')
        urllib.request.install_opener(opener)
        print(urllib.request.install_opener(opener))
        print(str(count) + '-5')
        urllib.request.urlretrieve(imgUrl, word + '/' + str(count) + ".jpg")
        print(str(count) + '-6')
        count = count + 1
    except:
        print(str(count) + '-7')
        continue
# 크롤링 중간에 멈추었을때 대비
"""    
    stopPoint = 0
    try:
        if (count<stopPoint):
            image.click()
            count = count + 1
        else :
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,
                                         "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]").get_attribute(
                "src")
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, word + '/' + str(count) + ".jpg")
            count = count + 1
    except :
        pass
    """
driver.close()
