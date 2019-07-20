from model.group import Group
from model.contact import Contact
import random

def test_del_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="Group"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Firstname"))
    id_group_list = []
    id_group_list_with_contacts = []
    groups_list = db.get_group_list()
    for group in groups_list:
        id_group_list.append(group.id)
    for id_group in id_group_list:
        if len(orm.get_contacts_in_group(Group(id=id_group))) != 0:
            id_group_list_with_contacts.append(id_group)
    if len(id_group_list_with_contacts) == 0:
        id_contact = random.choice(db.get_contact_list()).id
        id_group = random.choice(db.get_group_list()).id
        app.contact.add_contact_in_group(id_group, id_contact)
        id_group_list_with_contacts.append(id_group)
    id_group = random.choice(id_group_list_with_contacts)
    id_contact = random.choice(orm.get_contacts_in_group(Group(id=id_group))).id
    app.contact.delete_contact_from_group(contact_from_group(id_group, id_contact))
    assert db.get_contact_by_id(id_contact) not in orm.get_contacts_in_group(Group(id=id_group))