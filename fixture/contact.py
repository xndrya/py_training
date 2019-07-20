import re
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact_in_group(self, id_group, id_contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact(id_contact)
        wd.implicitly_wait(3)
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(id_group)
        wd.find_element_by_name("add").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'add new')]").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//*[@name='update'])[1]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//*[@name='update'])[2]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def edit_first(self, contact):
        self.edit_contact_by_index(0, contact)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//*[@name='selected[]']")[index].click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_from_group(self, id_group, id_contact):
        wd = self.app.wd
        self.go_to_contacts_in_group_page(id_group)
        self.select_contact(id_contact)
        wd.find_element_by_name("remove").click()

    def go_to_contacts_in_group_page(self, id):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/?group=%s" % id
                and len(wd.find_element_by_name("remove")) > 0):
            wd.get("http://localhost/addressbook/?group=%s" % id)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def fill_contact_form(self, contact):
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
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                data = element.find_elements_by_tag_name("td")
                first_n = data[2].text
                last_n = data[1].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = data[3].text
                emails = data[4].text
                phones = data[5].text
                self.contact_cache.append(Contact(id=id, firstname=first_n, lastname=last_n, address=address,
                                                  phones=phones,
                                                  emails=emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_xpath("//tr[@name='entry']/td/input[@value='%s']/../.." % id)
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, home_phone=home_phone,
                       email1=email1, email2=email2, email3=email3, mobile=mobile, workphone=workphone, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile=mobile, workphone=workphone, phone2=phone2)

    def select_contact(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()