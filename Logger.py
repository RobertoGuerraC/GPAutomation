import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename='C:/Users/rguerra/desktop/automatizacion/example.log', level=logging.DEBUG,
                    format=LOG_FORMAT, filemode='w')


logger = logging.getLogger()

