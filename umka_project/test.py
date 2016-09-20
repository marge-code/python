import http

import tcp
import uuid

from html import to_html
from http import HTTPResponse
from app import WebApplication

def reverse_string(http_request):
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
    return html.html_form.format(user_data)


#s = http.HTTPServer(reverse_string)
#s.run()


def index_url_handler(request):
    return http.HTTPResponse.ok(to_html("Hello, world!"))

def reverse(request):
    return http.HTTPResponse.ok(request.content[::-1])

def login(request):
    name = request.url[len('/login/'):]
    response =  http.HTTPResponse.redirect('/home')
    #response = http.HTTPResponse.ok('')
    response.set_cookies({'username': name})
    return response

def home(request):
    if request.cookies:
        name = request.cookies['username']
    else:
        name = 'user'
    return http.HTTPResponse.ok(to_html('Home, sweet home, {}'.format(name)))

app = WebApplication()

app.register_url_handler('/index', index_url_handler)
app.register_url_handler('/reverse', reverse)
app.register_url_handler('/login/.*', login)
app.register_url_handler('/home', home)
app.run()
