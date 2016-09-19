import socket
import requests
import httplib

#r = requests.get('http://localhost:5000/')
#print r

#r1 = requests.get('http://localhost:5000/', data = 'qwe')
#print r1
#r2 = requests.get('http://localhost:5000/', data = 'qwe2', cookies = r1.cookies)
#print r2

r3 = requests.get('http://localhost:5000/index', data = 'qwe')
print r3

r4 = requests.get('http://localhost:5000/reverse', data = 'qwe')
print r3