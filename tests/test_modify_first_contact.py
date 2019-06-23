# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_new_contact(app):
    app.open_home_page()
    if app.contact.count == 0:
        app.contact.create(Contact("First name test", "Last name test", "Address test", "0123456789"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first(Contact("First name modified", "Last name modified", "Address modified", "9876543210"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
