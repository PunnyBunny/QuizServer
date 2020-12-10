import os
os.remove('server/site.db')

from server import db
db.session.remove()
db.drop_all()
db.create_all()
