from . import handlers
from . import logger
from .log_object import LogObject, ErrorLogObject, SqlLogObject


__version__ = '1.5.3.dev1'
__author__ = 'Ciprian Tarta, Dennis Parker'

log = logger.get_logger()
