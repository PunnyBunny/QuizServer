from server import app
import sys
if __name__ == '__main__':
    print("Server running...")
    app.run('0.0.0.0', int(sys.argv[1]), ssl_context='adhoc')

