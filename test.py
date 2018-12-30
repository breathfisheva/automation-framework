import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from lucyutils.config import Config, DRIVER_PATH

class TestBaidu(unittest.TestCase):

    URL = Config().get('URL') # 1：从Config中读取url

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe') # 2：从Config中读取path
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 测试')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 测试 2')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

if __name__ == '__main__':
    unittest.main()