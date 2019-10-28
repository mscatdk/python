import logging
import logging.config

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger('__app__')

v='demo'

logger.debug('debug message')
logger.info('info message with value: %s', v)
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')