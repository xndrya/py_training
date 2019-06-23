# -*- coding: utf-8 -*-

from model.group import Group

def test_edit_first_group(app):
    app.open_home_page()
    app.group.open_groups_page()
    if app.group.count == 0:
        app.group.create(Group(group_name="test", group_header="test header", group_footer="test_footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group("Edited group", "This is the edited group in this Address Book", "This is the edited comment"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
