import os
from flask import Flask
from app.database import db
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.posts.views.ps_views import posts
    app.register_blueprint(posts)

    return app
