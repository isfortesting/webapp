from flask import Blueprint

collars = Blueprint('collars', __name__, url_prefix='/')

from . import routes