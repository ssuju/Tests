import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_edit_admin(self):
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
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr/td[2]/a").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_title").clear()
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("Editing text in admin panel")
        elem = driver.find_element_by_id("id_text").clear()
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("Hi! This is working!! Yay!")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()