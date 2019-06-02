# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_new_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_xpath("//a[contains(text(),'add new')]").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("First name")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Last name")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Address")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("1234567890")
        driver.find_element_by_name("address2").click()
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
