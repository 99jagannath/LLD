from abc import ABC, abstractclassmethod
class InvoiceDao:

    def writeToDb(self):
        pass

    def writeToFile(self):
        pass

# here by adding the method write to file method we are modifying our existing class that might prone to bug
# rather than modifying we should extend our class
    

class InvoiceDao(ABC):

    @abstractclassmethod
    def save(self):
        pass


class DbInvoiceDao(InvoiceDao):

    def save(self):
        print("save to db")


class FileInvoiceDao(InvoiceDao):

    def save(self):
        print("save to file")    
