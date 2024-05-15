
from InfoLogProcessor import InfoLogProcessor
from DebugLogProcessor import DebugLogProcessor
from ErrorLogProcessor import ErrorLogProcessor
from LogProcessor import LogProcessor


class Main:

    def run(self):

        LogProcessor = InfoLogProcessor(DebugLogProcessor(ErrorLogProcessor(None)))
        LogProcessor.log(LogProcessor.INFO, "INFO message")
        LogProcessor.log(LogProcessor.DEBUG, "DEBUG message")
        LogProcessor.log(LogProcessor.ERROR, "ERROR message")

Main().run()