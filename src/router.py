from controllers.auto_complete_controller import AutoCompleteController
from responses.auto_complete_response import AutoCompleteResponse
from middlewares.auto_complete_verificator import AutoCompleteVerificator


class Router:
    __routes = {
        "/autocomplete": {
            "controller": AutoCompleteController,
            "middlewares": [AutoCompleteVerificator],
            "response": AutoCompleteResponse
        }
    }

    @staticmethod
    def get_controller(route_key):
        return Router.__routes.get(route_key).get("controller")

    @staticmethod
    def get_middlewares(route_key):
        return Router.__routes.get(route_key).get("middlewares")

    @staticmethod
    def get_reponse_handler(route_key):
        return Router.__routes.get(route_key).get("response")

    @staticmethod
    def get_route_list():
        return Router.__routes.keys()
