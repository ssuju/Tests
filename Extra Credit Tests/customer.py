import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class foodservices_customers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "ssuju"
        pwd = "sapkota1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ssuju.pythonanywhere.com/")
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        time.sleep(1)
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://ssuju.pythonanywhere.com/")
        assert "Logged In"

        driver.get("http://ssuju.pythonanywhere.com/customer_list")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a").click()
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("Edit address")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        driver.get("http://ssuju.pythonanywhere.com/customer_list")
        time.sleep(5)
        assert "Edited Customer"

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[13]/a").click()
        alert = driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        driver.get("http://ssuju.pythonanywhere.com/customer_list")
        time.sleep(5)
        assert "Deleted Customer"

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[14]/a").click()
        time.sleep(5)
        assert "Summary of Customer"


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()