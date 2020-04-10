from flask_restplus import Resource, fields
from src.namespace import ns
from src.app import api

project = api.model('Project', {
    'id': fields.Integer(readonly=True, description='The project unique identifier'),
    'name': fields.String(required=True, description='The name of the project')
})

stage = ns.model('Stage', {
    'id': fields.Integer(readonly=True, description='The stage class object unique identifier'),
    'name': fields.String(required=True, description='The name of the stage')
})

activity = ns.model('Activity', {
    'id': fields.Integer(readonly=True, description='The stage class object unique identifier'),
    'name': fields.String(required=True, description='The name of the stage')
})


class ProjectDAO(object):
    def __init__(self):
        self.counter = 0
        self.projects = list()

    def get(self, id):
        for this_project in self.projects:
            if this_project['id'] == id:
                return this_project
        api.abort(404, "Project {} doesn't exist".format(id))

    def create(self, data):
        new_project = data
        new_project['id'] = self.counter = self.counter + 1
        self.projects.append(new_project)
        print('new project created ', new_project, type(new_project), 'all ', self.projects)
        return new_project

    def update(self, id, data):
        this_project = self.get(id)
        this_project.update(data)
        print('successfully updated project ', self.projects)
        return project

    def delete(self, id):
        this_project = self.get(id)
        self.projects.remove(this_project)
        print('successfuly removed project ', self.projects)


ProjectDAO = ProjectDAO()
ProjectDAO.create({'name': 'Test project'})


@ns.route('/projects')
class ProjectsResource(Resource):
    '''Shows a list of all projects'''

    # @ns.expect(project)
    @ns.doc('list_projects')
    @ns.marshal_list_with(project)
    def get(self):
        '''List all projects'''
        return ProjectDAO.projects

#     @ns.doc('create_todo')
#     @ns.expect(todo)
#     @ns.marshal_with(todo, code=201)
#     def post(self):
#         '''Create a new task'''
#         return DAO.create(api.payload), 201
#
#
# @ns.route('/<int:id>')
# @ns.response(404, 'Todo not found')
# @ns.param('id', 'The task identifier')
# class Todo(Resource):
#     '''Show a single todo item and lets you delete them'''
#
#     @ns.doc('get_todo')
#     @ns.marshal_with(todo)
#     def get(self, id):
#         '''Fetch a given resource'''
#         return DAO.get(id)
#
#     @ns.doc('delete_todo')
#     @ns.response(204, 'Todo deleted')
#     def delete(self, id):
#         '''Delete a task given its identifier'''
#         DAO.delete(id)
#         return '', 204
#
#     @ns.expect(todo)
#     @ns.marshal_with(todo)
#     def put(self, id):
#         '''Update a task given its identifier'''
#         # parser = reqparse.RequestParser()
#         # parser.add_argument('id', type=int, help='todo id')
#         return DAO.update(id, api.payload)
