
class Swipe:

  def __init__(self):
    self.users = set()

  def add_user(self, user):
    self.users.add(user)

  def is_swiped(self, user):
    return  user in self.users