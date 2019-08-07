# -*- coding: utf-8 -*-

from random import *
from model.contact import Contact

def test_delete_some_contact(app, db, check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test", lastname="Test Lastname"))
    with pytest.allure.step('Сравниваем список контактов'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Выбираем контакт'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('Удаляем контакт'):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Проверяем отсутствие удаленного контакта'):
        assert len(old_contacts)-1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact_cl):
            return Contact(id=contact_cl.id, firstname=contact_cl.firstname.strip())
        assert sorted(list(map(clean, new_contacts)), key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)
