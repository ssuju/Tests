import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class foodservices_services(unittest.TestCase):

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

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[3]/a").click()

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        elem = driver.find_element_by_id("id_cust_name")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/div/input").click()
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("selenium test")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("this is a selenium test")
        elem = driver.find_element_by_id("id_location")
        elem.send_keys("1001 selenium address ")
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("10")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()

        driver.get("http://ssuju.pythonanywhere.com/service_list")
        time.sleep(3)
        assert "New service added."

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("hello. this is working.")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        driver.get("http://ssuju.pythonanywhere.com/service_list")
        time.sleep(5)
        assert "Service Edited"

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a").click()
        alert = driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        driver.get("http://ssuju.pythonanywhere.com/service_list")
        time.sleep(5)
        assert "Service Deleted"


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()