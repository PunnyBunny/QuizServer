from server import app
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app.wsgi_app)
    http_server.serve_forever()
