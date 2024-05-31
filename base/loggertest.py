import logging

# logging.debug('Debug message')
# logging.info('Info message')
# logging.warning('Warning message')
# logging.error('Error message')
# logging.critical('Critical message')

#### output to console ####
# WARNING:root:Warning message
# ERROR:root:Error message
# CRITICAL:root:Critical message

print('--------------------------------------------------------------------------------------')



# logging.basicConfig(level=logging.DEBUG)
# logging.debug('Debug message')
# logging.info('Info message')

#### output to console ####
# DEBUG:root:Debug message
# INFO:root:Info message

print('--------------------------------------------------------------------------------------')
# logging.basicConfig(filename='my_log.log', filemode='w', format='%(asctime)s - %(message)s')
# logging.warning('warning message')

#### in file my_file.log ####
# 2023-11-09 08:47:19,606 - Warning message



print('--------------------------------------------------------------------------------------')

logger = logging.getLogger('my_logger')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
console_handler.setFormatter(console_formatter)

file_handler = logging.FileHandler(filename='my_log.log', mode='w')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning('Warning message')
logger.critical('Critical message')

#### console output ####
# WARNING:my_logger:Warning message
# CRITICAL:my_logger:Critical message

#### my_log.log file output ####
# 2023-11-09 09:12:48,919 - CRITICAL - Critical message



print('--------------------------------------------------------------------------------------')