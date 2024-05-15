
class BalanceSheet:

    def __init__(self, totalExpense, totalPayment, totalOwe, totalGetBack) -> None:
        self.totalExpense = totalExpense
        self.totalPayment = totalPayment
        self.totalOwe = totalOwe
        self.totalGetBack = totalGetBack
        self.userVsBalance = {}