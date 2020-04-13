from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from cicdApiFlaskRestplus.api.endpoints.projects import ns as ProjectNs
from flask import Blueprint
from flask_restplus import Api


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='CiCd API',
          description='An internal CI/CD API')

api_bp = Blueprint('api', __name__)
api = Api(api_bp, title="CiCd API", version='1.0')

# Routes
# api.add_resource(ProjectList, 'ProjectsList')
api.add_resource(ProjectNs, 'Projects')
projects_ns = api.namespace('projects', description='CiCd operations')

# api.add_resource(MessageResource, 'Messages')
# api.add_resource(ProfilesResource, 'Profiles')
# api.add_resource(CountMessages, 'UserMessageCount')
# api.add_resource(CountMessagesByChannel, 'UserMessageCountByChannels')
# api.add_resource(UsersResource, 'Users')

# projects_ns = api.namespace('projects', description='CiCd operations')
# stages_ns = api.namespace('projects/<int:project_pk>/stages', description='Stages operations')
# activities_ns = api.namespace('projects/<int:project_pk>/stages/<int:stage_pk>/activities/',
#                               description='Activities operations')

# api.add_resource(name='projects', resource=projects_ns, url='projects')
# api.add_resource(stages_ns, name='stages', url='projects/<int:project_pk>/stages/<int:stage_pk>/activities/')
# api.add_resource(activities_ns, name='activities', url='projects/<int:project_pk>/stages/<int:stage_pk>/activities/')


if __name__ == '__main__':
    app.run(debug=True)
