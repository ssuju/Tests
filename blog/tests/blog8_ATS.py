import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_delete_admin(self):
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
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/td/input").click()
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/label/select/option[2]").click()
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[1]/button").click()
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[4]").click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


