from model.contact import Contact

def test_contact_fields_to_db(app, db):
    if len(db.get_contact_list()) == 0:
        contact = Contact(
            firstname="John",
            lastname="Doe",
            home_phone="555555",
            mobile="79852589636",
            workphone="5555555",
            phone2="5555555",
            email1="john@jdoe.com",
            email2="john2@jdoe.com",
            email3="test3@djangostars.com",
            address="Address",
        )
        app.contact.create(contact)
    list_contacts = app.contact.get_contact_list()
    for contact in list_contacts:
        assert contact.firstname == db.get_contact_by_id(contact.id).firstname
        assert contact.lastname == db.get_contact_by_id(contact.id).lastname
        assert contact.address == db.get_contact_by_id(contact.id).address
        assert contact.emails == merge_emails(db.get_contact_by_id(contact.id))
        assert contact.phones == merge_phones(db.get_contact_by_id(contact.id))

def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email1, contact.email2, contact.email3])))

def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.home_phone, contact.mobile, contact.workphone, contact.phone2])))