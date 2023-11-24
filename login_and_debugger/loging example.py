import logging

logger =logging.getLogger(__name__)

#create handler
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('app.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# create formatter and add it to the handler
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("this is a warning")
logger.warning("this si an error")