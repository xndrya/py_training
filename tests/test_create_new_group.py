# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.group import Group

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group("", "", "")]+[
    Group(random_string("name",10), random_string("header",20), random_string("footer",20)) for i in range(5)
]
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_create_new_group(app, group):
    app.open_home_page()
    app.group.open_groups_page()
    # group = Group("New group", "This is a new group in this Address Book", "This is a comment")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
