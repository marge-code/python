import socket
import requests
import httplib


r1 = requests.get('http://localhost:5000/login/marge', data = 'qwe')
print r1

