class ContactHelper:

    def __init__(self,app):
        self.app=app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'add new')]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def edit_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//*[@name='update'])[1]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@name='selected[]']").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def fill_contact_form(self,contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name='firstname']").clear()
        wd.find_element_by_xpath("//input[@name='firstname']").send_keys(contact.firstname)
        wd.find_element_by_xpath("//input[@name='lastname']").clear()
        wd.find_element_by_xpath("//input[@name='lastname']").send_keys(contact.lastname)
        wd.find_element_by_xpath("//textarea[@name='address']").clear()
        wd.find_element_by_xpath("//textarea[@name='address']").send_keys(contact.address)
        wd.find_element_by_xpath("//input[@name='home']").clear()
        wd.find_element_by_xpath("//input[@name='home']").send_keys(contact.home_phone)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//*[@name='selected[]']"))
