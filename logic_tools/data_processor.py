import time


class DataProcessor:
    def __init__(self):
        pass

    @classmethod
    def process_data(cls, data):
        ### This is great, but it runs all the methods within
        # return {'time': cls._process_time(),
        #         'ping': cls._process_ping()
        #         }.get(data, "What was that?!")

        if data == "ping":
            return cls._process_ping()
        elif data == "time":
            return cls._process_time()
        ### Add new commands here
        else:
            return "What was that?"

    ### Implements new methods for commands here

    @staticmethod
    def _process_ping():
        print "processing ping"
        return "pong"

    @staticmethod
    def _process_time():
        print "processing time"
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
