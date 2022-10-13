import os
from app.app import app, db

#db.create_all()
#insert_admin()
#insert_types()

# Para Heroku
port = os.environ["PORT"]

app.run(debug=True , host="0.0.0.0", port = int(port))