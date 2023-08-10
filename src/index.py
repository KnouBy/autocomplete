import os
import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

from http.server import HTTPServer
from services.request_handler import RequestHandler

HOSTNAME = os.environ.get("HOSTNAME") \
    if os.environ.get("HOSTNAME") is not None else 'localhost'
PORT = int(os.environ.get("PORT")) \
    if os.environ.get("PORT") is not None else 8080

if __name__ == "__main__":
    webServer = HTTPServer((HOSTNAME, PORT), RequestHandler)
    logging.debug("Server started http://%s:%s", HOSTNAME, PORT)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    logging.debug("Server stopped.")
