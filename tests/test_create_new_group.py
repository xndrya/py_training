# -*- coding: utf-8 -*-

from model.group import Group

def test_create_new_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(Group("New group", "This is a new group in this Address Book", "This is a comment"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    app.group.return_to_groups_page()
