#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
from time import asctime
from routers import routes


class CustomRequestHandler(BaseHTTPRequestHandler):
    """Custom Request Handler for this simple web-server"""

    def _set_headers(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        # for default / route
        headers = {
            'status_code': 200,
            'content_type': 'text/html; charset=utf-8'
        }
        content = None
        with open('./index.html', 'r') as fp:
            content = fp.read()

        # for test purposes
        print 'PAAAAAAATH:', self.path

        if self.path in routes.ROOTS:
            # return index page (see above)
            pass
        elif any(self.path.startswith(key)
                 for key in routes.ROUTER['GET'].iterkeys()):
            headers['content_type'] = 'application/json'
            content = routes.api_get(headers, self.path)
        else:
            # return 404
            headers['status_code'] = 404
            with open('./404.html', 'r') as fp:
                content = fp.read()

        self._set_headers(**headers)
        self.wfile.write(content)

    def do_POST(self):
        headers = {
            'status_code': 200,
            'content_type': 'application/json'
        }
        content = None
        if any(self.path.startswith(key)
               for key in routes.ROUTER['POST'].iterkeys()):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            content = routes.api_post(headers, self.path, post_data)
        else:
            headers['status_code'] = 404
            content = json.dumps({'status': 'ERROR'})

        self._set_headers(**headers)
        self.wfile.write(content)


def run(server_class=HTTPServer, handler_class=CustomRequestHandler, port=80):
    from configuration.loadcfg import CFG
    server_conf = CFG['server_address']
    server_address = (server_conf['host'],
                      server_conf['port'])
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd... %s' % asctime()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print 'Stopping httpd... %s' % asctime()

if __name__ == '__main__':
    run()
