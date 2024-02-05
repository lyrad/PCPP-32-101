import logging
import sys

## Basic config.
# Only one call (a second would not overwrite config)...
# ! If not called basic loggers (no handler) use some "last resort" handler, with random levels (setlevel not working).
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
# logging.basicConfig(level=logging.ERROR, filename='prod.log', filemode='a')

## Creating a basic logger.
hello_logger = logging.getLogger('hello')  # Root logger: logger = logging.getLogger().
# hello_world_logger is a child of hello handler.
hello_world_logger = logging.getLogger('hello.world')
# Recommended, create logger per module (__name__: module name).
recommended_logger = logging.getLogger(__name__)

# Log levels (Default: warning), NOTSET: 0.
hello_logger.critical('Your CRITICAL value 50 message')
hello_logger.error('Your ERROR value 40 message')
hello_logger.warning('Your WARNING value 30 message')
hello_logger.info('Your INFO value 20 message')
hello_logger.debug('Your DEBUG value 10 message')
# NOTSET: seen as a log level priority value 0, but can't log a message at this level (default value...).

# Setting level.
recommended_logger.setLevel(logging.INFO)
recommended_logger.info('setLevel INFO value 20 message')
recommended_logger.debug('setLevel DEBUG value 10 message')


## Handlers, Formatter, Filters
# FileHandler with formatter
# default format: "%(levelname)s:%(name)s:%(message)s"
FileFormatter = logging.Formatter('%(name)s:%(module)s:%(levelname)s:%(asctime)s:%(message)s')
FileHandler = logging.FileHandler('prodFileHandler.log', mode='w')
FileHandler.setFormatter(FileFormatter)
FileHandler.setLevel(logging.CRITICAL)

filehandler_logger = logging.getLogger('filehandler')
filehandler_logger.addHandler(FileHandler)

# ! Not working properly when basicconfig called (displaying stuff in console...).
filehandler_logger.critical('FileHandler CRITICAL message')
filehandler_logger.error('FileHandler ERROR message')
filehandler_logger.warning('FileHandler WARNING message')
filehandler_logger.info('FileHandler INFO message')
filehandler_logger.debug('FileHandler DEBUG message')


# StreamHandler with filter
class TestFilter(logging.Filter):
    # Extends logging.Filter, filter method return true/false for log it or not.
    def filter(self, record):
        return True


StreamHandler = logging.StreamHandler(sys.stderr)
StreamHandler.setLevel(logging.INFO)
streamfilter_logger = logging.getLogger('streamfilter')
streamfilter_logger.addHandler(StreamHandler)
streamfilter_logger.addFilter(TestFilter())

# ! Not working properly when basicconfig called (displaying stuff in console...).
# In fact interact with basic config... when called basic will overlap stream halndler, when not a defaut stream handler is added.....
streamfilter_logger.critical('StreamHandlerFilter CRITICAL')
streamfilter_logger.error('StreamHandlerFilter ERROR')
streamfilter_logger.warning('StreamHandlerFilter WARNING')
streamfilter_logger.info('StreamHandlerFilter INFO')
streamfilter_logger.debug('StreamHandlerFilter DEBUG')


# Also: NullHandler, WatchedFileHandler, BaseRotatingHandler, RotatingFileHandler, TimedRotatingFileHandler,
# SocketHandler, DatagramHandler, SysLogHandler, SMTPHandler, MemoryHandler, HTTPHandler, QueueHandler, QueueListener
