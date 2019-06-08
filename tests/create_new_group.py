# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_untitled_test_case(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.open_groups_page()
    app.create_group(Group("New group", "This is a new group in this Address Book", "This is a comment"))
    app.return_to_groups_page()
    app.session.logout()