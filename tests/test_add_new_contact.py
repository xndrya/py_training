# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_new_contact(app):
    # app.open_home_page()
    # app.session.login(username="admin", password="secret")
    app.contact.create(Contact("First name", "Last name", "Address", "1234567890"))
    # app.session.logout()