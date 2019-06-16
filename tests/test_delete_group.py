# -*- coding: utf-8 -*-
from model.group import Group
def test_delete_first_group(app):
    # app.open_home_page()
    # app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    if app.group.count == 0:
        app.group.create(Group(group_name="test", group_header="test header", group_footer="test_footer"))
    app.group.delete_first_group()
    app.group.return_to_groups_page()
    # app.session.logout()
