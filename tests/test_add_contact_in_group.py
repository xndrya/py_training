from model.group import Group
from model.contact import Contact
import random

def test_add_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="Group1"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Firstname"))
    with pytest.allure.step('Сравниваем список контактов'):
        contact_list = db.get_contact_list()
    with pytest.allure.step('Выбираем группу'):
    	id_group = random.choice(db.get_group_list()).id
    with pytest.allure.step('Выбираем контакт'):
    	id_contact = random.choice(db.get_contact_list()).id
    with pytest.allure.step('Добавляем контакт в группу'):
    	app.contact.add_contact_in_group(id_group, id_contact)
    assert db.get_contact_by_id(id_contact) in orm.get_contacts_in_group(Group(id=id_group))