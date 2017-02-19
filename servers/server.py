from servers.tcp_server import TcpServer
from logic_tools.data_processor import DataProcessor

class Server:
    def __init__(self, host, port):
        self.server = TcpServer(host, port)

    def serve(self):
        m = DataProcessor().process_data
        self.server.serve(m)
