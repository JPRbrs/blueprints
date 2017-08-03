from flask import Blueprint

blueprint_one = Blueprint('blueprint_one', __name__)


@blueprint_one.route('/welcome')
def welcome():
    return '<H1>Welcome you!</H1>'
