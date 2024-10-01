from flask_restful import Resource

from configs import dify_config
from controllers.other_api import api,version


class IndexApiV2(Resource):
    def get(self):
        return {
            "welcome": "Dify other OpenAPI plugin",
            "api_version": "v2",
            "server_version": version,
        }


api.add_resource(IndexApiV2, "/")