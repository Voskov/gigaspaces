import pika


class RabbitQueueManager:
    def __init__(self, host, queue_name):
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, message):
        print("sending message <{}>".format(message))
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=self.queue_name,    # I'm not really sure what it does
                body=message
            )
        except Exception as ex:
            print("couldn't send the message because:")
            print(ex)
        else:
            print("sent message successfully")
        finally:
            self.connection.close()     # TODO - Should I close it here?

    def poll_messages(self):
        print "polling messages from <{}> queue".format(self.queue_name)
        self.channel.basic_consume(self.queue_callback,
                                   queue=self.queue_name,
                                   no_ack=True)
        self.channel.start_consuming()

    def queue_callback(self, ch, method, properties, body):
        # return body
        print "got message:"
        print body