from flask import request, current_app
from werkzeug.exceptions import HTTPException
from flakon import JsonBlueprint
from flakon.util import error_handling

import jwt


home = JsonBlueprint('home', __name__)


def _400(desc):
    exc = HTTPException()
    exc.code = 400
    exc.description = desc
    return error_handling(exc)


@home.route('/')
def _root():
    return {'pub_key': current_app.config['pub_key']}


@home.route('/create_token', methods=['POST'])
def create_token():
    key = current_app.config['priv_key']
    data = request.json
    token = jwt.encode(data, key, algorithm='RS512')
    return {'token': token.decode('utf8')}


@home.route('/verify_token', methods=['POST'])
def verify_token():
    key = current_app.config['pub_key']
    try:
        token = request.json['token']
        return jwt.decode(token, key)
    except Exception as e:
        return _400(str(e))
