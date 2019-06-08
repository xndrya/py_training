class GroupHelper:

    def __init__(self,app):
        self.app=app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'group page')]").click()

    def create(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'groups')]").click()