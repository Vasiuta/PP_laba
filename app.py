import os
import connexion
from database import *
from flask_bcrypt import Bcrypt
from functools import wraps
from flask import jsonify, request
from flask_jwt import jwt


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token, app.app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = db.query(Users).get(data['id'])
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)

    return decorator


db = SessionFactory()

abs_file_path = os.path.join(os.path.dirname(__file__))
app = connexion.FlaskApp(
    __name__, specification_dir=abs_file_path, options={"swagger_ui": True, "serve_spec": True}
)
app.app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
bcrypt = Bcrypt(app.app)

app.add_api("swagger.yaml", strict_validation=True)

flask_app = app.app
