from flask import Flask

from .config import Config

def create_app(config=None):
	app = Flask(__name__)

	# load config
	if config is None:
		config = Config()
	app.config.from_object(config)

	# database
	from .models import db
	db.init_app(app)
	app.db = db

	# views

	return app
