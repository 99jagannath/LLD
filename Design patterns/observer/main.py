import os
import sys

observable_path = os.path.join('./observable')
observer_path = os.path.join('./observer')

sys.path.append(observable_path)
sys.path.append(observer_path)

from p1observable import P1observalble
from u1observer import U1observer

def main():
    p1 = P1observalble()
    u1 = U1observer(p1)
    u1.notify_me()
    p1.update_state(1)

if __name__ in ['main' , '__main__']:
    sys.exit(main())