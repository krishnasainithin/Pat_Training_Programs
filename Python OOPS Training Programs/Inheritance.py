class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

dog = Dog("Max")
dog.eat() 
dog.bark()
# Output: Max is eating
# Output: Max is barking
