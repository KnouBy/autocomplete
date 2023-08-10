from http.server import BaseHTTPRequestHandler
from router import Router
from services.sanitize_service import SanitizeService


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        sanitized_path = SanitizeService.sanitize_path(self.path)
        route = sanitized_path.get("path")
        sanitized_params = sanitized_path.get("params")
        if not route in Router.get_route_list():
            return self.send_error(400, "Not Found")
        try:
            middlewares = Router.get_middlewares(route)
            sanitized_request = self.request
            for verificator in middlewares:
                sanitized_request, sanitized_params = verificator.verify(
                    sanitized_request, sanitized_params)
            controller = Router.get_controller(route)
            response = controller.get(sanitized_request, sanitized_params)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response.to_bytes())
        except Exception as exception:
            return self.send_error(400, str(exception))
