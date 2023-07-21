#import logging
from flask import Flask
from flask.blueprints import Blueprint
from server.routes import core as CoreRouter
import mongoengine
import logging
import configparser


app = Flask(__name__)


#routes
api_blueprint = Blueprint('api', __name__, url_prefix='/api')
api_blueprint.register_blueprint(CoreRouter.core_blue_print)
app.register_blueprint(api_blueprint)


def init():
    try:
        config = configparser.ConfigParser()
        config.read('config.ini')

        app.env_config = config

        mongo_db = mongoengine.connect(
        db=config.get('MONGO_DB','DB'),
        username=config.get('MONGO_DB','USERNAME'),
        password=config.get('MONGO_DB','PASSWORD'),
        host=config.get('MONGO_DB','HOST'),
        )

        app.mongo_db = mongo_db

    except Exception as e:
        logging.error('[app][init][error] ',str(e))


try:
    mongo_db = mongoengine.connect(
    db='test',
    username='user',
    password='12345',
    host='mongodb://admin:qwehost/production'
    )

except Exception as e:
    logging.error("[Error][init_mongo][error]"+str(e))
    pass



if __name__ == '__main__':
    init()
    app.run(debug=True)