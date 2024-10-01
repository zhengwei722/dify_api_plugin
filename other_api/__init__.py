from flask import Blueprint

from libs.external_api import ExternalApi

bp = Blueprint("other_api", __name__, url_prefix="/v2")
api = ExternalApi(bp)
version = 1.0

from . import index
from .other import other
