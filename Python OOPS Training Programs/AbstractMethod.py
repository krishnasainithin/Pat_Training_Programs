from abc import ABC , abstractmethod
class Example(ABC):
  @abstractmethod
  def method_one(self):
    print("hello")
    for i in range(10):
      print(i)
      
class Student(Example):
  def method_one(self):
    print("Hello World")