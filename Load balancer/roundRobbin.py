from loadBalancer import LoadBalancer
from collections import defaultdict, deque
class RoundRobbin(LoadBalancer):

  def __init__(self) -> None:
    self.dest_for_req = defaultdict(deque)
    super().__init__()


  def server_request(self, request):
    if request.request_type not in self.dest_for_req:
      destinations = self.get_destinations(request.request_type)
      self.dest_for_req[request.request_type] = deque(destinations)

    destinations = self.dest_for_req[request.request_type]

    front_dest = destinations.pop_left()

    front_dest.serve_request()
    front_dest.complete_request()

    destinations.append(front_dest) # Add back to the end of queue

    self.dest_for_req[request.request_type] = destinations
