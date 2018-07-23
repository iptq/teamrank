from flask_migrate import Migrate

from teamrank import create_app

app = create_app()
migrate = Migrate(app, app.db)