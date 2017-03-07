import os
from flakon import create_app
from .views import blueprints


_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, 'settings.ini')

app = create_app(blueprints=blueprints, settings=_SETTINGS)

# reading key files
with open(app.config['priv_key']) as f:
    app.config['priv_key'] = f.read()

with open(app.config['pub_key']) as f:
    app.config['pub_key'] = f.read()
