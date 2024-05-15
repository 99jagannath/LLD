

class Destination:

  def __init__(self, ip):
    self.ip = ip
    self.request_being_served = 0
    self.threshold = 10

  def serve_request(self):
    print("Sending  request to " + str(self.ip))
    if self.request_being_served > self.threshold:
      print("Fuck off!! i reached my threshold")

    self.request_being_served += 1

    return  True
  
  def complete_request(self):
    print("Request is completed by %s" % str(self.ip))
    self.request_being_served -= 1