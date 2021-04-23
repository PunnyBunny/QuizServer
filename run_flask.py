import sys

from server import app


def main():
    if len(sys.argv) != 2:
        print("Usage: python run_flask.py [port number]")
        return
    print("Server starting...")
    port = int(sys.argv[1])
    print('Server running...')
    app.run('0.0.0.0', port=port, ssl_context='adhoc')


if __name__ == '__main__':
    main()
