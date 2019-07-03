import re
from model.contact import Contact
from random import randrange

def test_check_view_to_edit_form_for_contact(app):
    app.open_home_page()
    if app.contact.count == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname", address="address", email1="email1",
                                   email2="email2", email3="email3", home_phone="+555", mobile="(1)111", workphone="2-22",
                                   phone2="44444"))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.emails == merge_emails_like_one_home_page(contact_from_edit_page)
    assert contact_from_home_page.phones == merge_phones_like_one_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_one_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile, contact.workphone, contact.phone2]))))

def merge_emails_like_one_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))
