# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class CustomersAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_customers_add(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("ssuju")
        driver.find_element_by_id("id_password").click()
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("sapkota1")
        driver.find_element_by_xpath("//input[@value='Log in']").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Customers'])[1]/following::a[1]").click()
        driver.find_element_by_id("id_cust_name").click()
        driver.find_element_by_id("id_cust_name").clear()
        driver.find_element_by_id("id_cust_name").send_keys("Jayden Smith")
        driver.find_element_by_id("id_organization").click()
        driver.find_element_by_id("id_organization").clear()
        driver.find_element_by_id("id_organization").send_keys("Economics")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("sujuta5@hotmail.com")
        driver.find_element_by_id("id_address").clear()
        driver.find_element_by_id("id_address").send_keys("1111 smith rd")
        driver.find_element_by_id("id_city").clear()
        driver.find_element_by_id("id_city").send_keys("Grand Island")
        driver.find_element_by_id("id_state").clear()
        driver.find_element_by_id("id_state").send_keys("NE")
        driver.find_element_by_id("id_zipcode").clear()
        driver.find_element_by_id("id_zipcode").send_keys("68137")
        driver.find_element_by_id("id_phone_number").clear()
        driver.find_element_by_id("id_phone_number").send_keys("4025543022")
        driver.find_element_by_id("id_role").click()
        driver.find_element_by_id("id_role").clear()
        driver.find_element_by_id("id_role").send_keys("Dish Washer")
        driver.find_element_by_id("id_bldgroom").click()
        driver.find_element_by_id("id_bldgroom").clear()
        driver.find_element_by_id("id_bldgroom").send_keys("PKI")
        driver.find_element_by_id("id_account_number").click()
        driver.find_element_by_id("id_account_number").clear()
        driver.find_element_by_id("id_account_number").send_keys("90")
        driver.find_element_by_name("_save").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Crm'])[1]/following::li[1]").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
