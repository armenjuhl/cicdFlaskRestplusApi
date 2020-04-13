from cicdApiFlaskRestplus.models.models import ProjectDAO, StageDAO, ActivityDAO


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
activityDAO.create(1, 1, {'name': 'push-to-remote-project-1-stage-1'})
activityDAO.create(1, 1, {'name': 'push-to-remote-project-1-stage-1'})
activityDAO.create(1, 2, {'name': 'push-to-master-project-1-stage-2'})
activityDAO.create(2, 3, {'name': 'pull-request-project-2-stage-3'})
activityDAO.create(3, 4, {'name': 'merge-request-project-3-stage-4'})
