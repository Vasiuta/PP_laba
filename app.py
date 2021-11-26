import os
import connexion
import database
from flask_bcrypt import Bcrypt

db = database.SessionFactory()

abs_file_path = os.path.join(os.path.dirname(__file__))
app = connexion.FlaskApp(
    __name__, specification_dir=abs_file_path, options={"swagger_ui": True, "serve_spec": True}
)

bcrypt = Bcrypt(app.app)

app.add_api("swagger.yaml", strict_validation=True)

flask_app = app.app
