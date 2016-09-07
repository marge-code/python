import http
import tcp
import uuid

def reverse_string(http_request):
    if 'Cookie' in http_request.headers:
        cookies = parse_cookies(http_request.headers['Cookie'])  
        name = cookies['name']
        content = '<!DOCTYPE html>'
        content += '<p>'
        content += 'Hello, {}!\n'.format(name) + http_request.content[::-1]
        content += '</p>'
        content += '</html>'
        response =  http.HTTPResponse.ok(content)
        response.set_cookies({'name': 'User-' + str(uuid.uuid4())})
    else:
        name = 'Username'
        content = 'Hello, {}!\n'.format(name) + http_request.content[::-1]
        response =  http.HTTPResponse.ok(content)
        tcp.logger.info('Set Cookies')
        response.set_cookies({'name': 'User-Davie'})
    return response

def parse_cookies(line):
    cookies = dict()
    items = line.split('; ')
    for item in items:
        key, value = item.split('=')
        cookies[key] = value
    return cookies

s = http.HTTPServer(reverse_string)
s.run()
