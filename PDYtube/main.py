import logging

a = 3
b = 0

try:
    a / b
except Exception as e:
    logging.exception("Exception occured")