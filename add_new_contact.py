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
        self.login(wd, "admin", "secret")
        # create contact
        self.create_contact(wd, "First name", "Last name", "Address", "1234567890")

    def create_contact(self, wd, firstname, lastname, address, home_phone):
        wd.find_element_by_xpath("//a[contains(text(),'add new')]").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(home_phone)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

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
