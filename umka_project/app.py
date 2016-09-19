import http

def index_url_handler(data):
    return 'hello world'

def reverse(data):
    return data[::-1]

class App(http.HTTPServer):
    def __init__(self):
        self.init_handlers()

    def init_handlers(self):
        self.handlers = dict()
        self.handlers['/index'] = index_url_handler
        self.handlers['/reverse'] = reverse

    def handle(self, data):
        http_request = self.parse_request(data)
        handler = self.handlers[http_request.url]
        content = handler(http_request.content)
        response = http.HTTPResponse.ok(content)
        return self.write_response(response)

app = App()
app.run()
