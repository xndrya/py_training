# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from data.add_group import constant as testdata
# from data.add_group import testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_create_new_group(app, group):
    app.open_home_page()
    app.group.open_groups_page()
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
