This code was written on a windows machine and wasn't tested on a linux
It SHOULD work, but I don't know it dor sure.

The server is started by running run_server.py using python
and appending a desired port for the server to listen to
e.g.
python run_server.py 9090

The client call is performed by running client_call.py using python
and appending the host address, the port and the message:
python client_call.py <host> <port> <message>
e.g.
python client_call.py localhost 9090 time
the supported messages are 'time' which returns the current server time
and 'ping' which returns a 'pong' message

I wasn't sure whether the RabbitMQ exercise should have been implemented into the TCP server exercise or not
So I wrote it as a similar separated system

To send a message into a rabbit queue, run send_to_queue.py using python
With a host, queue_name and message parameters:
python send_to_queue.py <host> <queue_name> <message>
e.g.:
python send_to_queue.py localhost giga vo

To poll the rabbit queue run poll_queue.py using python
With a host and queue_name parameters:
python poll_queue.py <host> <queue_name>
e.g.
python poll_queue.py localhost giga