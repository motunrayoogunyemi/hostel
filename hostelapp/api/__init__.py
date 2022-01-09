from flask import Blueprint
apiobj = Blueprint('bpapi', __name__,url_prefix='/hostel/api/v1.0')

from . import apiroutes