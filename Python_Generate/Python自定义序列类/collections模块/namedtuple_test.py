#! -*- encoding=utf-8 -*-
from collections import namedtuple

User = namedtuple("User", ["name", "age", "height"])
user = User(name="fzk", age=27, height=166)
print(user)
