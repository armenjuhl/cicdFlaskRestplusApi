from flask import Flask
from flask_restplus import Api
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='CiCd API',
          description='An internal CI/CD API',
          )


if __name__ == '__main__':
    app.run(debug=True)
