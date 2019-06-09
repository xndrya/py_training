class SessionHelper:

    def __init__(self,app):
        self.app=app

    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, '#')]").click()
        wd.find_element_by_name("user")