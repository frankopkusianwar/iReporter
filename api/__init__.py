from flask import Flask
from api.views import views


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(views.bp)