from flask import Blueprint

loans_bp = Blueprint('loans_bp', __name__)

from . import routes