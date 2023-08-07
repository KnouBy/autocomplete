from http.server import HTTPServer
from request_handler import RequestHandler

HOSTNAME = 'localhost'
PORT = 8080

if __name__ == "__main__":
    webServer = HTTPServer((HOSTNAME, PORT), RequestHandler)
    print(f'Server started http://{HOSTNAME}:{PORT}')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
