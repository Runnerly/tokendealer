from flask import request, current_app
from flakon import JsonBlueprint
import jwt


home = JsonBlueprint('home', __name__)


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
    token = request.json['token']
    return jwt.decode(token, key)
