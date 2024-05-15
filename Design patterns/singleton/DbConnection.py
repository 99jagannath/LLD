# It is used when we have to create only one instance of the class

# 1. Eager initialization

from threading import Lock

class DbConnection:

  __dbConnection = DbConnection()

  def getDbConnectionInstance(self):
    return DbConnection.__dbConnection
  

# 2. Lazy initialization
  
class DbConnection:

  __dbConnection = None

  def getDbConnectionInstance(self):
    if  not DbConnection.__dbConnection:
      DbConnection.__dbConnection = DbConnection()

    return  DbConnection.__dbConnection


# 3. Synchronized 

class DbConnection:

  __dbConnection = None
  lock = Lock()

  def getDbConnectionInstance(self):
    with DbConnection.lock:
      if DbConnection.__dbConnection is None:
        DbConnection.__dbConnection = DbConnection()
      return DbConnection.__dbConnection


# 4. Double -checked locking idiom (DCL)
  
class DbConnection:
  __dbConnection = None
  lock = Lock()

  def getDbConnectionInstance(self):
    if DbConnection.__dbConnection is None:
      with DbConnection.lock:
        if DbConnection.__dbConnection is None:
          DbConnection.__dbConnection = DbConnection()
    return DbConnection.__dbConnection
  
# Problem with double checked locking items:
# 1.
# lets deep dive in the db connection create instance code
# DbConnection.__dbConnection = DbConnection()
# 1. memoryPointer =  allocateMemoryForObject()
# 2. memoryPointer.initilizeWithDefaultValues()
# 3 obj = memoryPointer.getReference()
# now we have three steps to execute for db connection instance and cpu can reorder the steps to make execution optimized.
# if the order of execution became 1,3 and 2
# after executing 3 if any other thread want to enter the critical section then it will find object is not none and it will return the object But internally obj don't store
# reference which will produce Null pointer exception
# 2.
# Suppose there are two cores executing the process and the 1st core initialize the obj and store in the l1 cache. There is a time lag between syncronization of l1 cache of 
# core1 and core2 and writing into the memory. Meanwhile another thread is running on the 2nd core will find the obj as None and it will try to create the object which is the
# duplication task
  
# Solution :-
  
# in Jva we can use volatile keyword to handle such cases.
# volatile keyword will make sure it will directly write to the memory  rather than keeping it in CPU cache.
# Volatile keyword will make sure all the instructions before the volatile object will execute before the execution of volatile object and vice versa.