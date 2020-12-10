import os
path = os.path.join('server', 'site.db')
if os.path.exists(path):
    os.remove('server/site.db')

from server import db
db.session.remove()
db.drop_all()
db.create_all()
