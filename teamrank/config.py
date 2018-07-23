import os
import sys
import logging

class Config(object):
	def __init__(self, database_url=None, redis_url=None):
		# database
		if database_url is None:
			database_url = os.getenv("DATABASE_URL")
			if database_url is None:
				logging.getLogger().critical("No DATABASE_URL specified, aborting...")
				sys.exit(1)
		self.SQLALCHEMY_DATABASE_URI = database_url
		self.SQLALCHEMY_TRACK_MODIFICATIONS = False

		# redis
