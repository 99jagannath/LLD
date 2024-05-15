from HumanoidRobot import HumanoidRobot
from TreeRobot import TreeRobot

class  RobotFactory:

  def __init__(self):
    self.robot_map = {}

  def getRobot(self, type):

    if type in self.robot_map:
      return self.robot_map[type]
    
    if type == 'humanoid':
      return HumanoidRobot(type, 'HUMAN genes')
    
    else:
      return TreeRobot(type, 'Tree genes')