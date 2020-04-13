from flask_restplus import fields

from cicdApiFlaskRestplus.app import api
from cicdApiFlaskRestplus.initialize import projectDAO

project = api.model('Project', {
    'id': fields.Integer(readonly=True, description='The project unique identifier'),
    'name': fields.String(required=True, description='The name of the project')
})

stage = api.model('Stage', {
    'id': fields.Integer(readonly=True, description='The stage class object unique identifier'),
    'name': fields.String(required=True, description='The name of the stage')
})

activity = api.model('Activity', {
    'id': fields.Integer(readonly=True, description='The activity class object unique identifier'),
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
            new_stage = StageClass(name=data.get('name'), project_pk=project_pk)
            new_stage.id = self.counter = self.counter + 1
            new_stage.project_id = project_pk
            self.store.append(new_stage)
            return new_stage


class ActivityDAO(CiCdAbstractDAO):
    def __init__(self):
        super().__init__()
        self.counter = 0

    def create(self, project_pk, stage_pk, data):
        if projectDAO.get(project_pk):
            new_stage = ActivityClass(project_pk=project_pk, stage_pk=stage_pk, name=data.get('name'))
            new_stage.id = self.counter = self.counter + 1
            new_stage.project_id = project_pk
            self.store.append(new_stage)
            return new_stage
