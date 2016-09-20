import re

import http
from html import to_html

class WebApplication(http.HTTPServer):
    def __init__(self):
        self.handlers = dict()

    def register_url_handler(self, url, handler):
        self.handlers[url] = handler


    def handle_http_request(self, request):
        for url in self.handlers:
            if re.match(url, request.url):
                handler = self.handlers[url]
                return handler(request)

        return http.HTTPResponse.not_found('<b>Umka project page not found</b>')
