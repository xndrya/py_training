from model.contact import Contact

class ContactHelper:

    def __init__(self,app):
        self.app=app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'add new')]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_first(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//*[@name='update'])[1]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@name='selected[]']").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                first_n = element.find_element_by_xpath("//tr[@name='entry']//td[3]").text
                last_n = element.find_element_by_xpath("//tr[@name='entry']//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                contact_cache.append(Contact(firstname=first_n, lastname=last_n, id=id))
        return list(contact_cache)