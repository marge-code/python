import http
from http import HTTPResponse
import tcp
import uuid

import form

def reverse_string(http_request):
    #response = HTTPResponse.redirect("http://www.google.ru/")
    #response.set_cookies(...)

    if 'Cookie' in http_request.headers:
        cookies = parse_cookies(http_request.headers['Cookie'])  
        name = cookies['name']
        content = generate_content(name, http_request)
        response =  http.HTTPResponse.ok(content)
    else:
        content = generate_content('Username', http_request)
        response =  http.HTTPResponse.ok(content)
        tcp.logger.info('Set Cookies')
        response.set_cookies({'name': 'Davie', 'id': str(uuid.uuid4()), 'fig': 'newton', 'sugar': 'water'})
    return response

def parse_cookies(line):
    cookies = dict()
    items = line.split('; ')
    for item in items:
        key, value = item.split('=')
        cookies[key] = value
    return cookies

def generate_content(name, http_request):
    user_data = 'Hello, {}!\n'.format(name) + http_request.content[::-1]
    return form.content.format(user_data)




s = http.HTTPServer(reverse_string)
s.run()
