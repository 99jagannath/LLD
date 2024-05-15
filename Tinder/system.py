import math
from Match import Match
from Chat import Chat

class System:

  def __init__(self):
    self.users = []
    self.match = {} # uid : list[match]
    self.left_swipes = {} # uid : swipe
    self.right_swipes = {} # uid : swipe
    self.suggestions = {} # uid : users[] This data has to filled by machine learning algo

  def get_suggestions(self, user):
    if not user in self.suggestions:
      return []
    return self.suggestions[user.get_id()]
  
  def add_user(self, user):
    self.users.append(user)

  def update_radius(self, user, radius):
    user.update_radius(radius)
    for new_user in self.users:
      if new_user in self.left_swipes[user.get_id()] or  new_user in self.right_swipes[user.get_id()]:
        continue
      if math.abs(new_user.get_location() - user.get_location()) <= radius:
        self.suggestions[user.get_id()].append(new_user)

  def __create_match(self, user_a, user_b):
    new_match = Match(user_a, user_b)
    self.match[user_a.get_id()].append(new_match)
    self.match[user_b.get_id()].append(new_match)
  
  def delete_match(self,  match_obj):
    self.match[match_obj.user_a.get_id()].remove(match_obj)
    self.match[match_obj.user_b.get_id()].remove(match_obj)

  def right_swipe(self, user, target):
    self.right_swipe[user.get_id()].add(target)
    if user in self.right_swipe[target.get_id()]:
      self.__create_match(user, target)

  def left_swipe(self, user, target):
    self.left_swipe[user.get_id()].add(target)

  def send_message(self, msg, match, sendBy):
    message = Chat(msg, sendBy, Time())
    match.add_message(message)


