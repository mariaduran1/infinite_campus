from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from values import strings
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

class Search():


    
    def search_campus(self):
        driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
        driver.get("https://www.google.com/") 
        search_box_google = driver.find_element_by_name("q")
        search_box_google.send_keys(strings.search)
        search_box_google.submit()

    def first_result_view_open(self,timeout=10):
        driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
        driver.get("https://www.google.com/") 
        search_box_google = driver.find_element_by_name("q")
        search_box_google.send_keys(strings.search)
        search_box_google.submit()
        
        result = driver.find_element_by_css_selector(".LC20lb")
        result.click()
        driver.get("https://www.infinitecampus.com/company/careers")
        time.sleep(5)
        driver.save_screenshot('screen_shot2.png') 
        view_open = driver.find_element_by_css_selector(".button.info.large")
        view_open.click()
        time.sleep(10)
        driver.save_screenshot('screenshot3.png')
        
    

