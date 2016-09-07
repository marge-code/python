import socket
import time
import datetime
import httplib

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

    @staticmethod
    def redirect(target_url):
        pass

    @staticmethod
    def ok(content):
        headers = dict()
        headers['Content-Length'] = len(content)
        headers['Date'] = datetime.datetime.now()
        #headers['Set-Cookie'] = 'name=User-Davie'
        return HTTPResponse(200, headers, content)

    def set_cookies(self, cookies):
        cookies_items = ['{}={}'.format(k, v) for k, v in cookies.items()]
        self.headers['Set-Cookie'] = '; '.join(cookies_items)



class HTTPServer(tcp.TCPServer):
    def __init__(self, handler):
        self.request_handler = handler

    def handle(self, data):
        '''
        if self.is_full_request(data):
            request = self.parse_request(data)
            response = self.request_handler(request)
            return self.write_response(response)
        '''
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
        data += "\n\n"
        data += response.content
        return data

    def is_full_request(self, data):
        lines = data.split('\n')
        return '' in lines



def reverse_string(http_request):
    response =  HTTPResponse.ok(content = http_request.content[::-1])

    if 'Cookie' in http_request.headers:
        cookies = parse_cookies(http_request.headers['Cookie'])  
        name = cookies['name']
    else:
        name = 'Username'
        tcp.logger.info('Set Cookies')
        response.set_cookies({'name': 'User-Davie', 'id': '123123'})

    response.content = 'Hello, {}!\n'.format(name) + response.content
    return response

def parse_cookies(line):
    cookies = dict()
    items = line.split('; ')
    for item in items:
        key, value = item.split('=')
        cookies[key] = value
    return cookies


s = HTTPServer(reverse_string)
s.run()

