import random
import string
from model.group import Group

constant = [
    Group(group_name="name_1", group_header="header_1", group_footer="footer_1"),
    Group(group_name="name_2", group_header="header_2", group_footer="footer_2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group("", "", "")]+[
    Group(random_string("name",10), random_string("header",20), random_string("footer",20)) for i in range(5)
]