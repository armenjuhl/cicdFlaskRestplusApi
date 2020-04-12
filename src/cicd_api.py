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


class BaseCiCdClass(object):
    def __init__(self, name):
        self.id = int
        self.name = name

    def update(self, data):
        if data.get('id'):
            self.id = data.get('id')
        if data.get('name'):
            self.name = data.get('name')


class ProjectClass(BaseCiCdClass):
    def __init__(self, name):
        super().__init__(name)


class StageClass(BaseCiCdClass):
    def __init__(self, name, project_pk):
        super().__init__(name)
        self.project_id = project_pk


class ActivityClass(BaseCiCdClass):
    def __init__(self, name, project_pk, stage_pk):
        super().__init__(name)
        self.project_id = project_pk
        self.stage_id = stage_pk


class CiCdAbstractDAO(object):
    def __init__(self):
        self.counter = int
        self.store = list()

    def get(self, obj_id):
        for this_item in self.store:
            if this_item.id == obj_id:
                return this_item
        api.abort(404, f"Instance {obj_id} doesn't exist")

    def update(self, obj_id, data):
        this_item = self.get(obj_id)
        this_item.update(data)
        return this_item

    def delete(self, obj_id):
        this_item = self.get(obj_id)
        self.store.remove(this_item)


class ProjectDAO(CiCdAbstractDAO):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def create(self, data):
        new_project = ProjectClass(data.get('name'))
        new_project.id = self.counter = self.counter + 1
        self.store.append(new_project)
        return new_project


class StageDAO(CiCdAbstractDAO):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def create(self, project_pk, data):
        if projectDAO.get(project_pk):
            new_stage = StageClass(project_pk=project_pk, name=data.get('name'))
            new_stage.id = self.counter = self.counter + 1
            new_stage.project_id = project_pk
            self.store.append(new_stage)
            return new_stage


class ActivityDAO(CiCdAbstractDAO):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def get(self, project_pk, stage_pk):
        results = list()
        for this_item in self.store:
            if this_item['project_pk'] == project_pk and this_item['stage_pk'] == stage_pk:
                results.append(this_item)
        return this_item

        api.abort(404, f"Instance {stage_pk} doesn't exist")

    def create(self, project_pk, stage_pk, data):
        this_item = data
        this_item['id'] = self.counter = self.counter + 1
        this_item['project_pk'] = project_pk
        this_item['stage_pk'] = stage_pk
        self.store.append(this_item)
        return this_item

    def update(self, project_pk, stage_pk, data):
        this_item = self.get(id)
        this_item.update(data)
        return this_item

    def delete(self, project_pk, stage_pk):
        this_item = self.get(id)
        self.store.remove(this_item)


projectDAO = ProjectDAO()
projectDAO.create({'name': 'ajuhl-project-1'})
projectDAO.create({'name': 'ajuhl-project-2'})
projectDAO.create({'name': 'ajuhl-project-3'})
projectDAO.create({'name': 'ajuhl-project-4'})
projectDAO.create({'name': 'ajuhl-project-5'})

stageDAO = StageDAO()
stageDAO.create(1, {'name': 'project-1-dev'})
stageDAO.create(1, {'name': 'project-1-test'})
stageDAO.create(2, {'name': 'project-2-testing'})
stageDAO.create(3, {'name': 'project-3-staging'})
stageDAO.create(4, {'name': 'project-4-production'})

activityDAO = ActivityDAO()
activityDAO.create(1, 1, {'name': 'push-to-remote'})
activityDAO.create(1, 2, {'name': 'push-to-master'})
activityDAO.create(2, 3, {'name': 'pull-request'})
activityDAO.create(3, 4, {'name': 'merge-request'})

# Projects
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
        return projectDAO.get(project_pk)

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
        return projectDAO.update(project_pk, api.payload)


# Stages
@ns.route('/projects/<int:project_pk>/stages')
class StageList(Resource):
    '''Shows a list of all stages for a given project, and lets you POST to add new stages'''
    @ns.doc('list_stages')
    @ns.response(404, 'Stage not found')
    @ns.marshal_list_with(stage)
    def get(self, project_pk):
        '''List all stages under given project unique identifier'''
        payload = list()
        for this_stage in stageDAO.store:
            if this_stage.project_id == project_pk:
                payload.append(this_stage)
        if bool(payload) is True:
            return payload, 200
        api.abort(404, f"Instance {project_pk} doesn't exist")

    @ns.doc('create_stage')
    @ns.expect(stage)
    @ns.marshal_with(stage, code=201)
    def post(self, project_pk):
        '''Create a new stage'''
        return stageDAO.create(project_pk, api.payload), 201


@ns.route('/projects/<int:project_pk>/stages/<int:stage_pk>')
@ns.response(404, 'Stage not found')
@ns.param('stage_pk', 'The unique stage identifier')
@ns.param('project_pk', 'The unique project identifier')
class Stage(Resource):
    '''Show a single stage for given project unique identifier'''
    @ns.doc('get_stage')
    @ns.marshal_with(stage)
    def get(self, stage_pk, project_pk):
        '''Fetch a single stage for given stage unique identifier'''
        for this_stage in stageDAO.store:
            if this_stage.id == stage_pk and this_stage.project_id == project_pk:
                return this_stage
        api.abort(404, f"Stage {stage_pk} in project {project_pk} doesn't exist")

    @ns.doc('delete_stage')
    @ns.response(204, 'Stage deleted')
    def delete(self, stage_pk, project_pk):
        '''Delete a stage given its unique identifier'''
        for this_stage in stageDAO.store:
            if this_stage.id == stage_pk and this_stage.project_id == project_pk:
                stageDAO.delete(stage_pk)
                return 204
        return 404

    @ns.expect(stage)
    @ns.response(204, 'Stage updated')
    @ns.marshal_with(stage)
    def put(self, stage_pk, project_pk):
        '''Update a stage given its identifier'''
        for this_stage in stageDAO.store:
            if this_stage.id == stage_pk and this_stage.project_id == project_pk:
                stageDAO.update(stage_pk, api.payload)
                return 204
        api.abort(404, f"Stage {stage_pk} in project {project_pk} doesn't exist")


# Activity
@ns.route('/projects/<int:project_pk>/stages/<int:stage_pk>/activities')
@ns.param('stage_pk', 'The unique stage identifier')
@ns.param('project_pk', 'The unique project identifier')
class ActivityList(Resource):
    '''Shows a list of all activities for a given stage, and lets you POST to add new activities'''
    @ns.doc('list_activities')
    @ns.marshal_list_with(activity)
    def get(self):
        '''List all activities under given project unique identifier'''
        payload = list()
        for this_activity in activityDAO.store:
            if this_activity.project_id == project_pk and this_activity.stage_id == stage_pk:
                payload.append(this_activity)
        return payload
        return activityDAO.store

    @ns.doc('create_activity')
    @ns.expect(activity)
    @ns.marshal_with(stage, code=201)
    def post(self, project_pk, stage_pk):
        '''Create a new activity'''
        payload = {'name': api.payload['name'], 'project_pk': project_pk, 'stage_pk': stage_pk}
        return activityDAO.create(payload), 201


@ns.route('/projects/<int:project_pk>/stages/<int:stage_pk>/activities/<int:activity_pk>')
@ns.response(404, 'Activity not found')
@ns.param('stage_pk', 'The unique stage identifier')
@ns.param('project_pk', 'The unique project identifier')
@ns.param('activity_pk', 'The unique activity identifier')
class Activity(Resource):
    '''Show a single activity for given project unique identifier'''
    @ns.doc('get_activity')
    @ns.marshal_with(activity)
    def get(self, stage_pk, project_pk, activity_pk):
        '''Fetch a single acitivty for given activity unique identifier'''
        for this_activity in activityDAO.store:
            if this_activity['id'] == activity_pk and stage_pk and this_activity['project_id'] == project_pk and this_activity['id'] \
                    == activity_pk:
                return this_activity
        return 404

    @ns.doc('delete_stage')
    @ns.response(204, 'Stage deleted')
    def delete(self, stage_pk, project_pk):
        '''Delete a stage given its unique identifier'''
        for this_stage in stageDAO.store:
            if this_stage['id'] == stage_pk and this_stage['project_id'] == project_pk:
                stageDAO.delete(stage_pk)
                return 204
        return 404

    @ns.expect(stage)
    @ns.response(204, 'Stage updated')
    @ns.marshal_with(stage)
    def put(self, stage_pk, project_pk):
        '''Update a stage given its identifier'''
        for this_stage in stageDAO.store:
            if this_stage['id'] == stage_pk and this_stage['project_id'] == project_pk:
                stageDAO.update(this_stage, api.payload)
                return 204
        return 404


if __name__ == '__main__':
    app.run(debug=True)

