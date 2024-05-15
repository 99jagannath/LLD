from abc import  ABC, abstractmethod

class LoadBalancer(ABC):

  def __init__(self) -> None:
    self.service_map = {}

  def register(self, request_type, service):
    self.service_map[request_type] = service

  def get_destinations(self, request_type):
    destinations = None
    if request_type in self.service_map:
      destinations = self.service_map[request_type].destinations
    return destinations

  @abstractmethod
  def server_request(self):
    pass