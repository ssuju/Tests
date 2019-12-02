import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class foodservices_product(unittest.TestCase):

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

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[1]/li[4]/a").click()

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        elem = driver.find_element_by_id("id_cust_name")
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/div/input").click()
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("selenium test")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("this is a selenium test")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("2")
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys("10")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()

        driver.get("http://ssuju.pythonanywhere.com/product_list")
        time.sleep(5)
        assert "Added new Product"

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[7]/a").click()
        elem = driver.find_element_by_id("id_product")
        elem.send_keys("Edit")
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys("Edit Description")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        driver.get("http://ssuju.pythonanywhere.com/product_list")
        time.sleep(5)
        assert "Edited Product"

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        alert = driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        driver.get("http://ssuju.pythonanywhere.com/product_list")
        time.sleep(5)
        assert "Deleted Product"


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()