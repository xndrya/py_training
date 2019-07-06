# -*- coding: utf-8 -*-
from model.group import Group

def test_create_new_group(app, data_groups):
    group = data_groups
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
