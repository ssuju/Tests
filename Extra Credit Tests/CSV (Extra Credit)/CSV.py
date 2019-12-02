import unittest
import time
import csv

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

class Customer:
    def __init__(self, Cust_name="", Organization="", Role="", Email="", BldgRoom="",
                 Address="", Account_No="", City="", State="", Zipcode="",  Phone_Number=""):
        self.Cust_name = Cust_name
        self.Organization = Organization
        self.Role = Role
        self.Email = Email
        self.BldgRoom = BldgRoom
        self.Address = Address
        self.Account_No = Account_No
        self.City = City
        self.State =State
        self.Zipcode = Zipcode
        self.Phone_Number = Phone_Number

class foodservices_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def readCSV(self):
        customers = []
        with open("customers.csv", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                # convert row to Customer object
                customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                customers.append(customer)
        return customers

    def test_mfs(self):
        user = "ssuju"
        pwd = "sapkota1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://ssuju.pythonanywhere.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(1)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        driver.get("http://ssuju.pythonanywhere.com/admin")
        assert "Logged In"
        time.sleep(3)

        customers = foodservices_ATS().readCSV()
        for i in range(len(customers)):
            customer = customers[i]

            elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a").click()

            elem = driver.find_element_by_id("id_cust_name")
            elem.send_keys(customer.Cust_name)

            elem = driver.find_element_by_id("id_organization")
            elem.send_keys(customer.Organization)

            elem = driver.find_element_by_id("id_role")
            elem.send_keys(customer.Role)

            elem = driver.find_element_by_id("id_email")
            elem.send_keys(customer.Email)

            elem = driver.find_element_by_id("id_bldgroom")
            elem.send_keys(customer.BldgRoom)

            elem = driver.find_element_by_id("id_address")
            elem.send_keys(customer.Address)

            elem = driver.find_element_by_id("id_account_number")
            elem.send_keys(customer.Account_No)

            elem = driver.find_element_by_id("id_city")
            elem.send_keys(customer.City)

            elem = driver.find_element_by_id("id_state")
            elem.send_keys(customer.State)

            elem = driver.find_element_by_id("id_zipcode")
            elem.send_keys(customer.Zipcode)

            elem = driver.find_element_by_id("id_phone_number")
            elem.send_keys(customer.Phone_Number)

            time.sleep(3)

            elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()

            time.sleep(3)

            driver.get("http://ssuju.pythonanywhere.com/admin")

        time.sleep(3)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()