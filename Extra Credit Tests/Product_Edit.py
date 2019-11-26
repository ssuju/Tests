# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class ProductEdit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_product_edit(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/home/")
        driver.find_element_by_link_text("Products").click()
        driver.find_element_by_link_text("Edit").click()
        driver.find_element_by_id("id_p_description").click()
        driver.find_element_by_id("id_p_description").click()
        driver.find_element_by_id("id_p_description").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_p_description | ]]
        driver.find_element_by_id("id_p_description").click()
        driver.find_element_by_id("id_p_description").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_p_description | ]]
        driver.find_element_by_id("id_p_description").clear()
        driver.find_element_by_id("id_p_description").send_keys(
            "Full Sheet Cake with the wording: Congratulations Harvey Smith on Your Retirement!! Barbara will send a student assistant to pick up at Scott Hall in Scott Campus.")
        driver.find_element_by_id("id_quantity").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_quantity | ]]
        driver.find_element_by_id("id_quantity").click()
        driver.find_element_by_id("id_quantity").clear()
        driver.find_element_by_id("id_quantity").send_keys("12")
        driver.find_element_by_id("id_charge").click()
        driver.find_element_by_id("id_charge").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=id_charge | ]]
        driver.find_element_by_id("id_charge").click()
        driver.find_element_by_id("id_charge").clear()
        driver.find_element_by_id("id_charge").send_keys("100.00")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Edit Product'])[1]/following::form[1]").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Charge:'])[1]/following::button[1]").click()

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