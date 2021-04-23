import sys

from gevent.pywsgi import WSGIServer

from server import app


def main():
    if len(sys.argv) != 2:
        print("Usage: python run.py [port number]")
        return
    port = int(sys.argv[1])
    print("Server starting...")
    http_server = WSGIServer(('0.0.0.0', port), app.wsgi_app)
    print("Server running...")
    http_server.serve_forever()


if __name__ == '__main__':
    main()
