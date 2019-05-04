from selenium import webdriver
from values import strings

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome('C:\dev1\week5\chromedriver.exe')

        

    def navigate(self, url):
        self.driver.get(url)
        

    def close(self):
        self.driver.quit()
