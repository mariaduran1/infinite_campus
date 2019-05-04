import unittest
from selenium import webdriver
from values.Webdriver import Driver
from values import strings
from values.functions import Search
import HtmlTestRunner


class Test_Find_Google(unittest.TestCase):
    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.url)

    def test_search_campus(self):
        search_result = Search()
        search_result.search_campus()
        search_result.first_result_view_open()
        


        
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = "./report"))

