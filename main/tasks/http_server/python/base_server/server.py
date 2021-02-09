#!/usr/bin/env python
import http.server

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/server':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
        else:
            self.send_error(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=Handler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
