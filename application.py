from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path ="C:\geckodriver\geckodriver.exe")
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[contains(@href, '#')]").click()

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

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()