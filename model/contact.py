class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home_phone=None, id=None):
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
        self.home_phone=home_phone
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname
