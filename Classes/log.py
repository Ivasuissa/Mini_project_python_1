import logging


class Logger:
    def add_to_log(self, msg):
         logging.basicConfig(filename='my.log', level=logging.INFO,
                            format='%(asctime)s : %(levelname)s : %(message)s',
                             datefmt = "%Y-%m-%d-%H-%M-%S")
         logging.info(msg)





