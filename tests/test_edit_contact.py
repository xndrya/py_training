# -*- coding: utf-8 -*-

from random import *
from model.contact import Contact

def test_edit_some_contact(app, db, check_ui):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test1"))
    with pytest.allure.step('Получение списка контактов'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Выбираем рандомный контакт'):
        id = random.choice(old_contacts).id
    contact_old = db.get_contact_by_id(id)
    old_contacts.remove(contact_old)
    contact_new = Contact(firstname="Test2", id=id)
    with pytest.allure.step('Изменяем информацию контакта'):
        app.contact.edit_contact_by_id(id, contact_new)
    old_contacts.append(contact_new)
    assert len(old_contacts) == app.contact.count()
    with pytest.allure.step('Получение нового списка контактов'):
        new_contacts = app.contact.get_contact_list()
    with pytest.allure.step('Проверяем соответствие списков'):
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact_cl):
            return Contact(id=contact_cl.id, firstname=contact_cl.firstname.strip())
        assert sorted(list(map(clean, new_contacts)), key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)
