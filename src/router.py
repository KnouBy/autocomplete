from controllers.auto_complete_controller import AutoCompleteController
from responses.auto_complete_response import AutoCompleteResponse
from middlewares.auto_complete_verificator import AutoCompleteVerificator


class Router:
    _routes = {
        "/autocomplete": {
            "controller": AutoCompleteController,
            "middlewares": [AutoCompleteVerificator],
            "response": AutoCompleteResponse
        }
    }

    @staticmethod
    def get_controller(routeKey):
        return Router._routes.get(routeKey).get("controller")

    @staticmethod
    def get_middlewares(routeKey):
        return Router._routes.get(routeKey).get("middlewares")

    @staticmethod
    def get_reponse_handler(routeKey):
        return Router._routes.get(routeKey).get("response")

    @staticmethod
    def get_route_list():
        return Router._routes.keys()
