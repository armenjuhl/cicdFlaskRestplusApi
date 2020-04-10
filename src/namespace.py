from src.app import api


ns = api.namespace('cicd', description='CiCd operations')
ns.add_route()