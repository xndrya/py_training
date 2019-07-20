from model.group import Group

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
        self.fill_form(group)
        # submit form
        wd.find_element_by_xpath("//input[@name='submit']").click()
        self.open_groups_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.select_group_by_id(id)
        wd.find_element_by_xpath("//*[@name='delete']").click()
        self.open_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.select_group_by_id(id)
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        self.open_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//*[@name='selected[]']")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id ).click()

    def edit_group_by_index(self, index, group):
        wd = self.app.wd
        self.select_group_by_index(index)
        wd.find_element_by_xpath("//*[@name='edit']").click()
        self.fill_form(group)
        wd.find_element_by_xpath("//*[@name='update']").click()
        self.open_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.select_group_by_id(id)
        wd.find_element_by_xpath("//*[@name='edit']").click()
        self.fill_form(group)
        wd.find_element_by_xpath("//*[@name='update']").click()
        self.open_groups_page()
        self.group_cache = None

    def edit_first_group(self, group):
        self.edit_group_by_index(0, group)

    def fill_form(self,group):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='group_name']").clear()
        wd.find_element_by_xpath("//input[@name='group_name']").send_keys(group.group_name)
        wd.find_element_by_xpath("//textarea[@name='group_header']").clear()
        wd.find_element_by_xpath("//textarea[@name='group_header']").send_keys(group.group_header)
        wd.find_element_by_xpath("//textarea[@name='group_footer']").clear()
        wd.find_element_by_xpath("//textarea[@name='group_footer']").send_keys(group.group_footer)

    def open_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_xpath("//input[@name='new']"))>0:
            return
        wd.find_element_by_xpath("//a[contains(text(),'groups')]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//*[@name='selected[]']"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(group_name=text, id = id))
        return list(self.group_cache)
