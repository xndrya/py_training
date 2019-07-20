# -*- coding: utf-8 -*-

import random
from model.group import Group

def test_delete_some_group(app, db, check_ui):
    app.open_home_page()
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="test", group_header="test header", group_footer="test_footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)