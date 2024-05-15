

class Match:

  def __init__(self, id, user_a, user_b):
    self.id = id
    self.user_a = user_a
    self.user_b = user_b
    self.chat = []

  def  add_message(self, message):
    self.chat.append(message)