
import logging


class Logger:
    
    def __init__(self, **kwargs):
        self.set_logger(**kwargs)
        self.warn = self.warning

    def set_logger(self, **kwargs):
        name = kwargs.get('name')
        name = name if name else __name__
        level = kwargs.get('level')
        level = level if level else logging.DEBUG

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        fmt = kwargs.get('format')
        fmt = fmt if fmt else "%(name)s - [%(asctime)s][%(levelname)s] %(message)s"

        formater = logging.Formatter(fmt)

        console_level = kwargs.get('console_level')
        console_level = console_level if console_level else logging.INFO

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(formater)

        filename = kwargs.get('filename')
        filename = filename if filename else __name__ + '.log'
        file_level = kwargs.get('file_level')
        file_level = file_level if file_level else logging.DEBUG

        file_handler = logging.FileHandler(filename)
        file_handler.setLevel(level)
        file_handler.setFormatter(formater)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def log(self, message, level='debug'):
        lvl = level.lower()
        if lvl == 'debug':
            self.logger.debug(message)
        elif lvl == 'info':
            self.logger.info(message)
        elif lvl in ['warn', 'warning']:
            self.logger.warning(message)
        elif lvl == 'error':
            self.logger.error(message)
        elif lvl == 'critical':
            self.logger.critical(message)
        else:
            self.logger.debug(message)

    def debug(self, message):
        self.log(message, level='debug')
    
    def info(self, message):
        self.log(message, level='info')
    
    def warning(self, message):
        self.log(message, level='warning')

    def error(self, message):
        self.log(message, level='error')
    
    def critical(self, message):
        self.log(message, level='critical')
