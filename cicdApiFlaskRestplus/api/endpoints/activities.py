# from flask_restplus import Resource
#
# from cicdApiFlaskRestplus.api.endpoints import activities_ns as ns
# from cicdApiFlaskRestplus.app import api
# from cicdApiFlaskRestplus.initialize import activityDAO
# from cicdApiFlaskRestplus.models.models import activity
#
#
# @ns.route('/projects/<int:project_pk>/stages/<int:stage_pk>/activities')
# @ns.param('stage_pk', 'The unique stage identifier')
# @ns.param('project_pk', 'The unique project identifier')
# class ActivityList(Resource):
#     '''Shows a list of all activities for a given activity, and lets you POST to add new activities'''
#     @ns.doc('list_activities')
#     @ns.marshal_list_with(activity)
#     def get(self, project_pk, stage_pk):
#         '''List all activities under given project unique identifier'''
#         payload = list()
#         for this_activity in activityDAO.store:
#             if this_activity.project_id == project_pk and this_activity.stage_id == stage_pk:
#                 payload.append(this_activity)
#         return payload
#
#     @ns.doc('create_activity')
#     @ns.expect(activity)
#     @ns.marshal_with(activity, code=201)
#     def post(self, project_pk, stage_pk):
#         '''Create a new activity'''
#         return activityDAO.create(project_pk=project_pk, stage_pk=stage_pk, data=api.payload), 201
#
#
# @ns.route('/projects/<int:project_pk>/stages/<int:stage_pk>/activities/<int:activity_pk>')
# @ns.response(404, 'Activity not found')
# @ns.param('activity_pk', 'The unique activity identifier')
# @ns.param('stage_pk', 'The unique stage identifier')
# @ns.param('project_pk', 'The unique project identifier')
# class Activity(Resource):
#     '''Show a single activity for given project and activity unique identifiers'''
#     @ns.doc('get_activity')
#     @ns.marshal_with(activity)
#     def get(self, stage_pk, project_pk, activity_pk):
#         '''Fetch a single activity for given project, activity and activity unique identifier'''
#         this_activity = activityDAO.get(activity_pk)
#         if this_activity and this_activity.stage_id == stage_pk and this_activity.project_id == project_pk \
#                 and this_activity.id == activity_pk:
#             return this_activity
#         return 404
#
#     @ns.doc('delete_stage')
#     @ns.response(204, 'Stage deleted')
#     def delete(self, stage_pk, project_pk, activity_pk):
#         '''Delete an activity given its unique identifier'''
#         for this_activity in activityDAO.store:
#             if activityDAO.get(activity_pk) and this_activity.project_id == project_pk \
#                     and this_activity.stage_id == stage_pk:
#                 activityDAO.delete(activity_pk)
#                 return 204
#         return 404
#
#     @ns.expect(activity)
#     @ns.response(204, 'Activity updated')
#     @ns.marshal_with(activity)
#     def put(self, project_pk, stage_pk, activity_pk):
#         '''Update an activity given its identifier'''
#         for this_activity in activityDAO.store:
#             if this_activity.project_id == project_pk and this_activity.id == stage_pk \
#                     and this_activity.id == activity_pk:
#                 activityDAO.update(obj_id=activity_pk, data=api.payload)
#                 return 204
#         return 404
