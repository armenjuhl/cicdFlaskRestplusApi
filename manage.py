import os
# import pytest
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from app.app import api

from app.main import create_app
from app.namespace import ns

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()


app = Flask(__name__)

db = SQLAlchemy()

# logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
# logging.config.fileConfig(logging_conf_path)
# log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = 'localhost:5000'
    # flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    # flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    flask_app.config['RESTPLUS_VALIDATE'] = True
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = False
    flask_app.config['ERROR_404_HELP'] = False


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(ns)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    # log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)


if __name__ == "__main__":
    main()
