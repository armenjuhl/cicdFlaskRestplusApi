# from flask_restplus import Resource
#
# from cicdApiFlaskRestplus.app import api
# from cicdApiFlaskRestplus.initialize import stageDAO
# from cicdApiFlaskRestplus.models.models import stage
# from cicdApiFlaskRestplus.api.endpoints import stages_ns as ns
#
#
# @ns.route('/projects/<int:project_pk>/stages')
# class StageList(Resource):
#     '''Shows a list of all stages for a given project, and lets you POST to add new stages'''
#     @ns.doc('list_stages')
#     @ns.response(404, 'Stage not found')
#     @ns.marshal_list_with(stage)
#     def get(self, project_pk):
#         '''List all stages under given project unique identifier'''
#         payload = list()
#         for this_stage in stageDAO.store:
#             if this_stage.project_id == project_pk:
#                 payload.append(this_stage)
#         if bool(payload) is True:
#             return payload, 200
#         api.abort(404, f"Instance {project_pk} doesn't exist")
#
#     @ns.doc('create_stage')
#     @ns.expect(stage)
#     @ns.marshal_with(stage, code=201)
#     def post(self, project_pk):
#         '''Create a new stage'''
#         return stageDAO.create(project_pk=project_pk, data=api.payload), 201
#
#
# @ns.route('/projects/<int:project_pk>/stages/<int:stage_pk>')
# @ns.response(404, 'Stage not found')
# @ns.param('stage_pk', 'The unique stage identifier')
# @ns.param('project_pk', 'The unique project identifier')
# class Stage(Resource):
#     '''Show a single stage for given project unique identifier'''
#     @ns.doc('get_stage')
#     @ns.marshal_with(stage)
#     def get(self, project_pk, stage_pk):
#         '''Fetch a single stage for given stage unique identifier'''
#         this_stage = stageDAO.get(stage_pk)
#         if this_stage and this_stage.project_id == project_pk:
#             return this_stage
#         api.abort(404, f"Stage {stage_pk} in project {project_pk} doesn't exist")
#
#     @ns.doc('delete_stage')
#     @ns.response(204, 'Stage deleted')
#     def delete(self, stage_pk, project_pk):
#         '''Delete a stage given its unique identifier'''
#         for this_stage in stageDAO.store:
#             if this_stage.id == stage_pk and this_stage.project_id == project_pk:
#                 stageDAO.delete(obj_id=stage_pk)
#                 return 204
#         return 404
#
#     @ns.expect(stage)
#     @ns.response(204, 'Stage updated')
#     @ns.marshal_with(stage)
#     def put(self, stage_pk, project_pk):
#         '''Update a stage given its identifier'''
#         for this_stage in stageDAO.store:
#             if this_stage.id == stage_pk and this_stage.project_id == project_pk:
#                 stageDAO.update(obj_id=stage_pk, data=api.payload)
#                 return 204
#         api.abort(404, f"Stage {stage_pk} in project {project_pk} doesn't exist")
