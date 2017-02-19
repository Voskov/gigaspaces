import socket, argparse
# import general_client

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('port', type=int)
parser.add_argument('request', type=str)


class TcpClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)

    def send_message(self, msg):
        try:
            print("sending message: <%s>") % msg
            self.sock.connect(self.server_address)
            self.sock.sendall(msg)
        except:
            print("failed sending the message")
            self.sock.close()
        else:
            print("message was sent successfully")

        data = self.sock.recv(4096)
        if data:
            print 'received:'
            print data
        self.sock.close()