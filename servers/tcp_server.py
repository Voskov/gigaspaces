import socket


class TcpServer:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (host, port)
        self.sock.bind(self.server_address)

    def serve(self, logic):
        """

        :param logic:
        :return:
        """
        print 'starting up on %s port %s' % self.server_address
        self.sock.listen(1)
        while True:
            print 'waiting for a connection'
            connection, client_address = self.sock.accept()
            try:
                print 'connection from', client_address

                while True:
                    data = connection.recv(4096)
                    print 'received <%s>' % data
                    if data:
                        msg = logic(data)
                        connection.sendall(msg)
                    else:
                        break
            except: # TODO - print exception
                print "something went wrong with the server"
            else:
                "response was sent successfully"
            finally:
                connection.close()
