from selenium.webdriver.common.by import By
from selenium import webdriver
from values.Webdriver import Driver

driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')
search_box_google = driver.find_element_by_name("q")
results = driver.find_element_by_css_selector(".LC20lb")
first_result = results[0]


