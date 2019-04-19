import os
from flask import Flask, Blueprint
from app.api.restplus import api
from app.api.endpoints.message import ns as REST_backend_namespace
from app.api.endpoints.message import mongo


app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('DB')
app.config['RESTPLUS_MASK_SWAGGER'] = False
blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(REST_backend_namespace)
app.register_blueprint(blueprint)


mongo.init_app(app)

