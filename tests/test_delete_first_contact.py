# -*- coding: utf-8 -*-

from model.contact import Contact

def test_delete_first_contact(app):
    app.open_home_page()
    if app.contact.count == 0:
        app.contact.create(Contact("First name test", "Last name test", "Address test", "0123456789"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
