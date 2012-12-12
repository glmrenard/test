#!/usr/bin/env python
from pymongo import Connection

connection=Connection()
db=connection['test']

post={"author": "Guillaume","Note": "31"}
posts=db.posts
posts.insert(post)

for truc in posts.find():
	print truc
