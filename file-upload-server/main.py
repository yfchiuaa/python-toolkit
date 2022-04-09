from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

hostname = "localhost"
port = 3000


class FileUploadServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        h = open("./index.html", "rb")
        self.wfile.write(h.read())

    def do_POST(self):
        if self.path == '/upload':
            self._set_headers()
            h = open("./index.html", "rb")
            self.wfile.write(h.read())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    server = HTTPServer((hostname, port), FileUploadServer)
    print(f"Server started at http://{hostname}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    logging.info("Stopping server...")
