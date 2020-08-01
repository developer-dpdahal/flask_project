from flask import Flask

app = Flask(__name__)

from flaskproject.routes import routes
