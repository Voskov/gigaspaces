import argparse
from servers.client import Client

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('port', type=int)
    parser.add_argument('request', type=str)
    args = parser.parse_args()
    try:
        client = Client(args.host, args.port)
        client.send_message(args.request)
    except Exception as ex:
        print("Couldn't make the client call because:")
        print(ex)