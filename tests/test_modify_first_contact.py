# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_new_contact(app):
    app.open_home_page()
    # app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact("First name modified", "Last name modified", "Address modified", "9876543210"))
    app.session.logout()