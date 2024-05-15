
from loadBalancer import LoadBalancer



class LeastConnection(LoadBalancer):

  def server_request(self, request):

    destinations = self.service_map[request.request_type]
    least_connection_dest = None
    min_conn = float('inf')

    for dest in destinations:
      if dest.request_being_served < min_conn:
        min_conn = least_connection_dest
        least_connection_dest = dest

    dest.serve_request()
    dest.complete_request()