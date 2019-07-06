import random
import string
import os.path
import json
import getopt
import sys
from model.group import Group

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        if int(a)<1:
            n = 1
        else:
            n = int(a)-1
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group("", "", "")] + [
    Group(random_string("name",10), random_string("header",20), random_string("footer",20)) for i in range(n)
]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file_path, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
