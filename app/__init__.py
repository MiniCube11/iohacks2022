from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'auth.login'

from app.views import main, auth, events
app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(events.bp, url_prefix="/events")

from app import models

if __name__ == '__main__':
    app.run()
