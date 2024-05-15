
from roundRobbin import RoundRobbin
from leastConnection import LeastConnection


class loadBalancerFactory:


  def  createLoadBalancer(self, method):
    if method == "roundrobin":
      return  RoundRobbin()
    elif  method == "leastconnection":
      return  LeastConnection()