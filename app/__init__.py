from flask import Flask

app = Flask(__name__)

from blueprint import blueprint
app.register_blueprint(blueprint.blueprint_one)
