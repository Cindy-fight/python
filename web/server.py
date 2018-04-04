from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8006, application)
print('Serving HTTP on port 8006...')

httpd.serve_forever()
