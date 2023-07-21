from crypt import methods
from flask.blueprints import Blueprint;
from ..controllers import core as CoreController
from flask import json

core_blue_print = Blueprint('core', __name__, url_prefix='/core')

@core_blue_print.route('/ping',methods=['GET'])
def ping():
    res = CoreController.ping()
    return json.jsonify({
        "message": res
    }), 200