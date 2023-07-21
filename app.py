from flask import Flask
from flask.blueprints import Blueprint
from server.routes import core as CoreRouter

app = Flask(__name__)

api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api_blueprint.register_blueprint(CoreRouter.core_blue_print)
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run(debug=True)