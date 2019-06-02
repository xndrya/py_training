# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path ="C:\geckodriver\geckodriver.exe")
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_xpath("//a[contains(@href, '#')]").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    def create_group(self, wd):
        # new group creation
        wd.find_element_by_xpath("//input[@name='new']").click()
        # fill group form
        wd.find_element_by_xpath("//input[@name='group_name']").clear()
        wd.find_element_by_xpath("//input[@name='group_name']").send_keys("New group")
        wd.find_element_by_xpath("//textarea[@name='group_header']").clear()
        wd.find_element_by_xpath("//textarea[@name='group_header']").send_keys("This is a new group in this Address Book")
        wd.find_element_by_xpath("//textarea[@name='group_footer']").clear()
        wd.find_element_by_xpath("//textarea[@name='group_footer']").send_keys("This is a comment")
        # submit form
        wd.find_element_by_xpath("//input[@name='submit']").click()

    def open_groups_page(self, wd):
        wd.find_element_by_xpath("//a[contains(text(),'groups')]").click()

    def login(self, wd):
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys("admin")
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()