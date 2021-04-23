import sys

from gevent.pywsgi import WSGIServer

from server import app


def main():
    print("Server starting...")
    if len(sys.argv) != 2:
        print("Usage: python run.py [port number]")
        return
    port = int(sys.argv[1])
    http_server = WSGIServer(('0.0.0.0', port), app.wsgi_app, ssl_context='adhoc')
    print("Server running...")
    http_server.serve_forever()


if __name__ == '__main__':
    main()
