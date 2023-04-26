from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from .routes import proxy_bp
app.register_blueprint(proxy_bp)

