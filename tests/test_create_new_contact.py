# -*- coding: utf-8 -*-

from model.contact import Contact

def test_create_new_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact("First name", "Last name", "Address", "1234567890")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)