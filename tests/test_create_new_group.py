# -*- coding: utf-8 -*-

from model.group import Group

def test_create_new_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    group = Group("New group", "This is a new group in this Address Book", "This is a comment")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    app.group.return_to_groups_page()
