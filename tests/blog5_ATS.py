import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class edit_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_edit_post(self):
        user = "ssuju"
        pwd = "sapkota1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[5]/h2/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/p[2]/textarea").click()
        elem = driver.find_element_by_id("id_text")
        elem.send_keys(" This is the new edited post. It works!!")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(3)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)