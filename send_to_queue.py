import argparse
from queue_tools.queue_manager import QueueManager


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str)
    parser.add_argument('queue_name', type=str)
    parser.add_argument('message', type=str)
    args = parser.parse_args()
    try:
        queue = QueueManager(args.host, args.queue_name)
        queue.send_message(args.message)
    except Exception as ex:
        print("couldn't send message <{}> to queue <{}> because:").format(args.message, args.queue_name)
        print(ex)

