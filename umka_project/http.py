import socket
import datetime
import httplib
import Cookie

import server_logger
import tcp

class HTTPRequest:
    def __init__(self, method, url, protocol_version, headers, content):
        self.method = method
        self.url = url
        self.protocol_version = protocol_version
        self.headers = headers
        self.content = content
    

class HTTPResponse:
    def __init__(self, status, headers, content):
        self.status = status
        self.headers = headers
        self.content = content
        self.set_common_headers()
        self.cookies = ''

    def set_common_headers(self):
        self.headers['Content-Length'] = len(self.content)
        self.headers['Date'] = datetime.datetime.now()

    @staticmethod
    def redirect(target_url):
        response = HTTPResponse(301, dict(), "")
        response.headers['Location'] = target_url
        return response

    @staticmethod
    def ok(content):
        return HTTPResponse(200, dict(), content)

    def set_cookies(self, user_cookies):
        self.cookies = Cookie.SimpleCookie(user_cookies).output()




class HTTPServer(tcp.TCPServer):
    def __init__(self, handler = lambda data: data):
        self.request_handler = handler

    def handle(self, data):
        if self.is_full_request(data):
            request = self.parse_request(data)
            response = self.request_handler(request)
            return self.write_response(response)
        

    def parse_request(self, data):        
        head, body = data.split('\r\n\r\n')
        head_lines = head.split('\n')
        starting_line = head_lines[0]
        method, url, protocol_version = starting_line.split(' ')

        headers = dict()
        for line in head_lines[1 : ]:
            item = line.split(': ')
            headers[item[0]] = item[1]

        h = HTTPRequest(method, url, protocol_version, headers, body)
        return h

    def write_response(self, response):
        data = "HTTP/1.1 {} {}\n".format(response.status, httplib.responses[response.status])
        for k, v in response.headers.items():
            data += '{}: {}\n'.format(k, v)
        if response.cookies:
            data += response.cookies
        data += "\n\n"
        data += response.content
        tcp.logger.info('write_response: {}'.format(data.replace('\n', '\\n')))
        return data

    def is_full_request(self, data):
        return '\r\n\r\n' in data
