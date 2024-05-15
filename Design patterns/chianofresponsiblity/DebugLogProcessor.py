
from LogProcessor import LogProcessor

class DebugLogProcessor(LogProcessor):

    def __init__(self, logProcessor) -> None:
        super().__init__(logProcessor)

    def log(self, loglevel, message):

        if loglevel == LogProcessor.DEBUG:
            print("[Debug] " + message)
        else:
            super().log(loglevel, message)