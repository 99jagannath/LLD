
from LogProcessor import LogProcessor

class InfoLogProcessor(LogProcessor):

    def __init__(self, logProcessor) -> None:
        super().__init__(logProcessor)

    def log(self, loglevel, message):
        if loglevel == LogProcessor.INFO:
            print("[Info] " + message)
        else:
            super().log(loglevel, message)