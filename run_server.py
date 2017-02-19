import argparse
from servers.server import Server
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    parser.parse_args()
    args = parser.parse_args()
    host = 'localhost'
    try:
        server = Server(host, args.port)
        server.serve()
    except Exception as ex:
        print("couldn't start the server because:")
        print(ex)
