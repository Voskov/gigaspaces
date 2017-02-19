from servers.tcp_client import TcpClient

class Client:
    def __init__(self, host, port):
        self.tcp_client = TcpClient(host, port)

    def send_message(self, msg):
        self.tcp_client.send_message(msg)
        # Change

if __name__ == '__main__':
    pass