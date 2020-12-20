from server import app
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':
    print("Server starting...")
    http_server = WSGIServer(('0.0.0.0', 5000), app.wsgi_app)
    print("Server running...")
    http_server.serve_forever()
