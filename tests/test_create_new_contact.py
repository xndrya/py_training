# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact("", "", "", "")]+[
    Contact(random_string("name",10), random_string("lastname",20), random_string("address",20), (random.choice(string.digits))*10) for i in range(5)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_new_contact(app, contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)