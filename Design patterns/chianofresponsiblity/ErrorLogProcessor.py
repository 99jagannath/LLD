from LogProcessor import LogProcessor

class ErrorLogProcessor(LogProcessor):

    def __init__(self, logProcessor) -> None:
        super().__init__(logProcessor)

    def log(self, loglevel, message):
        if loglevel == LogProcessor.ERROR:
            print("[Error] " + message)
        else:
            super().log(loglevel, message)