from flask_restplus import Resource

from cicdApiFlaskRestplus.app import projects_ns as ns
from cicdApiFlaskRestplus.initialize import projectDAO
from cicdApiFlaskRestplus.models.models import project
# from cicdApiFlaskRestplus.api.endpoints import projects_ns as ns

# ns = api.namespace('projects', description='CiCd operations')


@ns.route('/projects')
class ProjectList(Resource):
    '''Shows a list of all projects, and lets you POST to add new projects'''
    @ns.doc('list_projects')
    @ns.marshal_list_with(project)
    def get(self):
        '''List all projects'''
        return projectDAO.store

    @ns.doc('create_project')
    @ns.expect(project)
    @ns.marshal_with(project, code=201)
    def post(self):
        '''Create a new project'''
        return projectDAO.create(data=api.payload), 201


@ns.route('/projects/<int:project_pk>')
@ns.response(404, 'Project not found')
@ns.param('project_pk', 'The unique project identifier')
class Project(Resource):
    '''Show a single project item'''
    @ns.doc('get_project')
    @ns.marshal_with(project)
    def get(self, project_pk):
        '''Fetch a given resource'''
        return projectDAO.get(obj_id=project_pk)

    @ns.doc('delete_project')
    @ns.response(204, 'Project deleted')
    def delete(self, project_pk):
        '''Delete a project given its unique identifier'''
        try:
            projectDAO.delete(project_pk)
            return 'Success', 204
        except NameError:
            return 'Project not found', 404

    @ns.expect(project)
    @ns.marshal_with(project)
    def put(self, project_pk):
        '''Update a project given its identifier'''
        return projectDAO.update(obj_id=project_pk, data=api.payload)
