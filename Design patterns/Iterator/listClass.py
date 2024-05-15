from listterator import  ListIterator

class listClass:

  def __init__(self, num_arr) -> None:
    self.list = num_arr

  def Iterator(self):
    return ListIterator(self.list)
  


def main():
  num_list = [1,2,3,4,5,6]
  it = listClass(num_list).Iterator()

  while it.has_next():
    print(it.next())


if __name__ in ['main', '__main__']:
  main()