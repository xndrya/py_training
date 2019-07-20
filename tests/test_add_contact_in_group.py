from model.group import Group
from model.contact import Contact
import random

def test_add_contact_in_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(group_name="Group1"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Firstname"))
    id_group = random.choice(db.get_group_list()).id
    id_contact = random.choice(db.get_contact_list()).id
    app.contact.add_contact_in_group(id_group, id_contact)
    assert db.get_contact_by_id(id_contact) in orm.get_contacts_in_group(Group(id=id_group))