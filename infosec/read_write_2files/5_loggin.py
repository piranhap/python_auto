import logging # python has a logging library :D

# configure first! don't skip
filename = 'example.log'

logging.basicConfig(filename=filename, filemode='a', level=logging.INFO, format="%(levelname)s - %(message)s") # logging.INFO means that is the minimal level that will be get logged


# test
logging.info('This is an example log entry')


# DEBUG, INFO, WARNING, ERROR, CRITICAL - Different levels 
# To use it in actual code you put it on the exception

try:
    pass
except:
    logging.error('Invalid number tried')
