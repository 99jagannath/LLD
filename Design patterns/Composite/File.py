from Filesystem import FileSystem

class File(FileSystem):

    def __init__(self, name) -> None:
        self.name = name

    def ls(self):
        print("File name is %s" % self.name)

    