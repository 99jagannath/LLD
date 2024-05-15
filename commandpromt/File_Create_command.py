from command import Command

class FileCreateCmd(Command):

    def __init__(self, kernel) -> None:
        self.kernel = kernel


    def execute(self):
        self.kernel.create_file()