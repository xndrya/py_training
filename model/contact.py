from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home_phone=None, mobile=None,
                 workphone=None, phone2=None, email1=None, email2=None, email3=None, id=None, phones=None, emails=None):
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
        self.home_phone=home_phone
        self.mobile = mobile
        self.workphone = workphone
        self.phone2 = phone2
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.phones = phones
        self.emails = emails

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname, )

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
