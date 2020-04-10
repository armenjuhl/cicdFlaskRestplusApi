from flask import Flask, request
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='CiCd API',
          description='An internal CI/CD API',
          )

ns = api.namespace('api', description='CiCd operations')

project = api.model('Project', {
    'id': fields.Integer(readonly=True, description='The project unique identifier'),
    'name': fields.String(required=True, description='The name of the project')
})

stage = api.model('Stage', {
    'id': fields.Integer(readonly=True, description='The stage class object unique identifier'),
    'name': fields.String(required=True, description='The name of the stage')
})

activity = api.model('Activity', {
    'id': fields.Integer(readonly=True, description='The stage class object unique identifier'),
    'name': fields.String(required=True, description='The name of the stage')
})


class CiCdAbstractDAO(object):
    def __init__(self):
        self.counter = 0
        self.class_store = list()

    def get(self, id):
        for this_item in self.class_store:
            if this_item['id'] == id:
                return this_item
        api.abort(404, f"Project {id} doesn't exist")

    def create(self, data):
        this_item = data
        this_item['id'] = self.counter = self.counter + 1
        self.class_store.append(this_item)
        return this_item

    def update(self, id, data):
        this_item = self.get(id)
        this_item.update(data)
        return this_item

    def delete(self, id):
        this_item = self.get(id)
        self.class_store.remove(this_item)


class ProjectDAO(CiCdAbstractDAO):
    def __init__(self):
        super().__init__()

    def get(self, id):
        for this_item in self.class_store:
            if this_item['id'] == id:
                return this_item
        api.abort(404, f"Project {id} doesn't exist")

    def create(self, data):
        this_item = data
        this_item['id'] = self.counter = self.counter + 1
        self.class_store.append(this_item)
        return this_item

    def update(self, id, data):
        this_item = self.get(id)
        this_item.update(data)
        return this_item

    def delete(self, id):
        this_item = self.get(id)
        self.class_store.remove(this_item)


# class StageDAO(ProjectDAO):
#     def __init__(self, id):
#         super().__init__()
#         self.stage_store = list()
#         self.project_name = StageDAO.getProject(id)
#
#     def get(self, id):
#         for this_item in self.stage_store:
#             if this_item['id'] == id:
#                 return this_item
#         api.abort(404, f"Project {id} doesn't exist")
#
#     def create(self, data):
#         this_item = data
#         this_item['id'] = self.counter = self.counter + 1
#         self.stage_store.append(this_item)
#         return this_item
#
#     def update(self, id, data):
#         this_item = self.get(id)
#         this_item.update(data)
#         return this_item
#
#     def delete(self, id):
#         this_item = self.get(id)
#         self.stage_store.remove(this_item)
#
#
# class ActivityDAO(StageDAO):
#     def __init__(self):
#         super().__init__()
#         self.activity_store = list()
#
#     def get_stage(self, id):
#         for this_item in self.stage_store:
#             if this_item['id'] == id:
#                 return this_item
#         api.abort(404, f"Project {id} doesn't exist")
#
#     def get(self, id):
#         for this_item in self.activity_store:
#             if this_item['id'] == id:
#                 return this_item
#         api.abort(404, f"Project {id} doesn't exist")
#
#     def create(self, data):
#         this_item = data
#         this_item['id'] = self.counter = self.counter + 1
#         self.activity_store.append(this_item)
#         return this_item
#
#     def update(self, id, data):
#         this_item = self.get(id)
#         this_item.update(data)
#         return this_item
#
#     def delete(self, id):
#         this_item = self.get(id)
#         self.activity_store.remove(this_item)
#
#
projectDAO = ProjectDAO()
projectDAO.create({'name': 'ajuhl-project'})
projectDAO.create({'name': 'ajuhl-project-2'})


# Projects
@ns.route('/projects')
class ProjectList(Resource):
    '''Shows a list of all projects, and lets you POST to add new projects'''
    @ns.doc('list_projects')
    @ns.marshal_list_with(project)
    def get(self):
        '''List all projects'''
        return projectDAO.class_store

    @ns.doc('create_project')
    @ns.expect(project)
    @ns.marshal_with(project, code=201)
    def post(self):
        '''Create a new project'''
        return projectDAO.create(api.payload), 201


@ns.route('/projects/<int:project_pk>')
@ns.response(404, 'Project not found')
@ns.param('project_pk', 'The unique project identifier')
class Project(Resource):
    '''Show a single project item'''
    @ns.doc('get_project')
    @ns.marshal_with(project)
    def get(self, project_pk):
        '''Fetch a given resource'''
        print(project_pk)
        return projectDAO.get(project_pk)

    @ns.doc('delete_project')
    @ns.response(204, 'Project deleted')
    def delete(self, project_pk):
        '''Delete a project given its unique identifier'''
        projectDAO.delete(project_pk)
        return '', 204

    @ns.expect(project)
    @ns.marshal_with(project)
    def put(self, project_pk):
        '''Update a project given its identifier'''
        return projectDAO.update(project_pk, api.payload)


# stageDAO = StageDAO()
# stageDAO.create({'name': 'dev'})
# stageDAO.create({'testing': 'dev'})
# stageDAO.create({'staging': 'dev'})
# stageDAO.create({'production': 'dev'})


# # Stages
# @ns.route('/projects/<int:project_pk>stages')
# class StageList(Resource):
#     '''Shows a list of all stages, and lets you POST to add new stages'''
#     @ns.doc('list_stages')
#     @ns.marshal_list_with(stage)
#     def get(self):
#         '''List all stages'''
#         return stageDAO.class_store
#
#     @ns.doc('create_stage')
#     @ns.expect(stage)
#     @ns.marshal_with(stage, code=201)
#     def post(self):
#         '''Create a new stage'''
#         return stageDAO.create(api.payload), 201
#
#
# @ns.route('/projects/<int:project_pk>/stages/<int:stage_pk>')
# @ns.response(404, 'Stage not found')
# @ns.param('id', 'The unique project identifier')
# class Stage(Resource):
#     '''Show a single project item'''
#     @ns.doc('get_stage')
#     @ns.marshal_with(project)
#     def get(self, id):
#         '''Fetch a given resource'''
#         return stageDAO.get(id)
#
#     @ns.doc('delete_stage')
#     @ns.response(204, 'Stage deleted')
#     def delete(self, id):
#         '''Delete a stage given its unique identifier'''
#         stageDAO.delete(id)
#         return '', 204
#
#     @ns.expect(stage)
#     @ns.marshal_with(stage)
#     def put(self, id):
#         '''Update a stage given its identifier'''
#         return stageDAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)

