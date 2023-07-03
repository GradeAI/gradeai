from flask import Blueprint

blueprint = Blueprint("my_blueprint", __name__)

from .ocr import *
from .query import *
from .upload import *
