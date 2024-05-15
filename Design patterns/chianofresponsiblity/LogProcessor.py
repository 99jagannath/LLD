from abc import ABC

class LogProcessor(ABC):
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, logProcessor) -> None:
        self.nextLogProcessor = logProcessor

    def log(self, loglevel, message):
        if self.nextLogProcessor != None:
            self.nextLogProcessor.log(loglevel, message)