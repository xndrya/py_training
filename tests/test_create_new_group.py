# -*- coding: utf-8 -*-

from model.group import Group

def test_create_new_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    app.group.create(Group("New group", "This is a new group in this Address Book", "This is a comment"))
    app.group.return_to_groups_page()
    app.session.logout()