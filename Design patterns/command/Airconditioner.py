
class AirConditioner:

  def __init__(self) -> None:
    self.isOn = False
    self.temp = 27

  def turnOn(self):
    print('Turn on AC')
    self.isOn = True

  def turnOff(self):
    print('Turn off AC')
    self.isOn = False

  def setTemp(self, temp):
    print('Set temp to %s' % temp)
    self.temp = temp