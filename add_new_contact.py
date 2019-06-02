# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path ="C:\geckodriver\geckodriver.exe")
        self.wd.implicitly_wait(30)
    
    def test_add_new_contact(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")
        # login
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys("admin")
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # create contact
        wd.find_element_by_xpath("//a[contains(text(),'add new')]").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("First name")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Last name")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Address")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("1234567890")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
