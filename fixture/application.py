from selenium import webdriver
from fixture.session import SessionHelper
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path ="C:\geckodriver\geckodriver.exe")
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    def create_group(self, group):
        wd = self.wd
        # new group creation
        wd.find_element_by_xpath("//input[@name='new']").click()
        # fill group form
        wd.find_element_by_xpath("//input[@name='group_name']").clear()
        wd.find_element_by_xpath("//input[@name='group_name']").send_keys(group.group_name)
        wd.find_element_by_xpath("//textarea[@name='group_header']").clear()
        wd.find_element_by_xpath("//textarea[@name='group_header']").send_keys(group.group_header)
        wd.find_element_by_xpath("//textarea[@name='group_footer']").clear()
        wd.find_element_by_xpath("//textarea[@name='group_footer']").send_keys(group.group_footer)
        # submit form
        wd.find_element_by_xpath("//input[@name='submit']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[contains(text(),'groups')]").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def create_contact(self, contact):
        wd = self.wd
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

    def destroy(self):
        self.wd.quit()