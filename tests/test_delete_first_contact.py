# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    app.open_home_page()
    # app.session.login(username="admin", password="secret")
    if app.contact.count == 0:
        app.contact.create(Contact("First name test", "Last name test", "Address test", "0123456789"))
    app.contact.delete_first_contact()
    # app.session.logout()
