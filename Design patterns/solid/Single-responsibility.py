# Each class should have only single responsibility

# Each class should have one reason to change

class Invoice:

    def __init__(self) -> None:
        pass

    def  get_total(self):
        pass

    def  display_invoice(self):
        pass

    def write_to_db(self):
        pass

# now we have three reason to change
# break the single class into multiple classes based on the requirement


class Invoice:

    def __init__(self) -> None:
        pass

    def get_total(self):
        pass

class InvoiceDao:

    def __init__(self) -> None:
        pass

    def saveToDb(self):
        pass

class InvoicePrinter:

    def __init__(self) -> None:
        pass

    def printInvoice(self):
        pass
