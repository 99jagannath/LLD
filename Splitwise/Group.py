

class Group:

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.members = []
        self.expenseController = ExpenseController()

    def crateExpense(self, id, description, amount, splitDetails, splitType, PaidBy):
        