# -*- coding: utf-8 -*-

import random
from model.group import Group

def test_delete_some_group(app, db, check_ui):
    app.open_home_page()
    app.group.open_groups_page()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="XGroupX"))
    old_groups = db.get_group_list()
    with pytest.allure.step('Выбираем группу'):
        group = random.choice(old_groups)
    with pytest.allure.step('Удаляем выбранную группу'):
        app.group.delete_group_by_id(group.id)
    with pytest.allure.step('Проверяем отсутствие удаленной группы из списка'):
        assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        def clean(group_cl):
            return Group(id = group_cl.id, group_name = group_cl.name.strip())
        assert sorted(list(map(clean, new_groups)), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)