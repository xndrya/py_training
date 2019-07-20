# -*- coding: utf-8 -*-

from random import randrange
from model.group import Group

def test_edit_some_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count == 0:
        app.group.create(Group(group_name="test", group_header="test header", group_footer="test_footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_group_by_id(index, Group("Edited group", "This is the edited group in this Address Book", "This is the edited comment"))
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert len(old_groups) == len(new_groups)
