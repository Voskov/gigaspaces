from queue_tools.rabbit_queue_manager import RabbitQueueManager


class QueueManager(object):
    def __init__(self, host, queue_name):
        self.rabbit_queue = RabbitQueueManager(host, queue_name)

    def send_message(self, message):
        self.rabbit_queue.send_message(message)

    def poll_messages(self):
        self.rabbit_queue.poll_messages()
