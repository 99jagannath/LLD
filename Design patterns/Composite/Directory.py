
from Filesystem import FileSystem

class Directory(FileSystem):

    def __init__(self, name) -> None:
        self.name = name
        self.fileSystemList = []

    def AddFileSystem(self, fileSystem):
        self.fileSystemList.append(fileSystem)

    def getFileSystem(self):
        return self.fileSystemList
    
    def ls(self):
        for fileSystem in self.fileSystemList:
            fileSystem.ls()