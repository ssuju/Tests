# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class ServiceAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_service_add(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        driver.find_element_by_link_text("Services").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Delete'])[5]/following::span[1]").click()
        driver.find_element_by_id("id_cust_name").click()
        Select(driver.find_element_by_id("id_cust_name")).select_by_visible_text("Barbara York")
        driver.find_element_by_id("id_service_category").click()
        driver.find_element_by_id("id_service_category").clear()
        driver.find_element_by_id("id_service_category").send_keys("Dish Washer")
        driver.find_element_by_id("id_description").click()
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("Adding York to wash dishes.")
        driver.find_element_by_id("id_location").click()
        driver.find_element_by_id("id_location").clear()
        driver.find_element_by_id("id_location").send_keys("Scott Hall")
        driver.find_element_by_id("id_setup_time").click()
        driver.find_element_by_id("id_service_charge").click()
        driver.find_element_by_id("id_service_charge").clear()
        driver.find_element_by_id("id_service_charge").send_keys("400.50")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[7]/following::button[1]").click()

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
