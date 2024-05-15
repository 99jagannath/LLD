from paymentFlow import paymentFlow

class PayToFriend(paymentFlow):

  def validate_request(self):
    print("Validating request to  pay friend")

  def debit_money(self):
    print("Debiting money for the transaction")

  def credit_money(self):
    print('Crediting money to friend')