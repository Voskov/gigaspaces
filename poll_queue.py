import argparse
from queue_tools.queue_manager import QueueManager


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('queue_name', type=str)
    args = parser.parse_args()
    try:
        queue = QueueManager(args.host, args.queue_name)
        queue.poll_messages()
    except Exception as ex:
        print "Could not start polling from <{}> because:".format(args.queue_name)
        print(ex)
