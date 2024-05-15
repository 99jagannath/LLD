# it is a structural design pattern
# it helps to distribute data among multiple objects
# design text editor & game
#Things to consider:-
# 1. Memory is limited
# 2. Data is shared between multiple objects
#   a. Intrinsic data :- Shared among objects and once created cannot change
#   b. Extrinsic data :- Changes based on client inputs and varies from object to object

# how it solves the issue?

# 1. Remove all the extrinsic data and keep only intrinsic data and object is called flyweight object
# 2. Fly weight class can be immutable
# 3. Extrinsic data can be passed in method parameter 
# 4. Once the flyweight object is created it is stored in cache and can used latter

from RobotFactory import RobotFactory


for  i in range(500):

  hrobot = RobotFactory.getRobot('humanoid')
  hrobot.display(i, i + 1)

  trobot = RobotFactory.getRobot('tree')
  trobot.display(i - 1, i)
