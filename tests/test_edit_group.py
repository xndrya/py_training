# -*- coding: utf-8 -*-
import random
from model.group import Group

def test_edit_some_group(app, db, check_ui):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(group_name="GroupX"))
    old_groups = db.get_group_list()
    id = random.choice(old_groups).id
    group_old_data = db.get_group_by_id(id)
    old_groups.remove(group_old_data)
    group_new = Group(group_name="GroupX", id=id)
    app.group.edit_group_by_id(id, group_new)
    old_groups.append(group_new)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group_cl):
            return Group(id=group_cl.id, group_name=group_cl.name.strip())
        assert sorted(list(map(clean, new_groups)), key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
