# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path ="C:\geckodriver\geckodriver.exe")
        self.wd.implicitly_wait(30)
    
    def test_add_new_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        self.login(wd, "admin", "secret")
        self.create_contact(wd, Contact("First name", "Last name", "Address", "1234567890"))

    def create_contact(self, wd, contact):
        wd.find_element_by_xpath("//a[contains(text(),'add new')]").click()
        wd.find_element_by_xpath("//input[@name='firstname']").clear()
        wd.find_element_by_xpath("//input[@name='firstname']").send_keys(contact.firstname)
        wd.find_element_by_xpath("//input[@name='lastname']").clear()
        wd.find_element_by_xpath("//input[@name='lastname']").send_keys(contact.lastname)
        wd.find_element_by_xpath("//textarea[@name='address']").clear()
        wd.find_element_by_xpath("//textarea[@name='address']").send_keys(contact.address)
        wd.find_element_by_xpath("//input[@name='home']").clear()
        wd.find_element_by_xpath("//input[@name='home']").send_keys(contact.home_phone)
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
