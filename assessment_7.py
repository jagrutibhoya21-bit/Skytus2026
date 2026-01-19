# 1   Base class Animal and subclasses Dog, Cat
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.speak()
c.speak()


#  2  Vehicle → Car → ElectricCar (Class Hierarchy)
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

e = ElectricCar()
e.start()
e.drive()
e.charge()


#   3   Method Overriding (Base & Derived)
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):
        print("This is child class")

c = Child()
c.show()


# 4    Multiple Inheritance (Two Parent Classes)
class Father:
    def skills(self):
        print("Father skills")

class Mother:
    def qualities(self):
        print("Mother qualities")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.qualities()


#5   Polymorphism – Different Shapes
class Shape:
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of Square")

class Circle(Shape):
    def area(self):
        print("Area of Circle")

shapes = [Square(), Circle()]

for s in shapes:
    s.area()
    
# 6  Bank System (Savings & Current Account)
class BankAccount:
    def account_type(self):
        print("General Account")

class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings Account")

class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account")

s = SavingsAccount()
c = CurrentAccount()

s.account_type()
c.account_type()    


#  7  Private Attributes + Getter / Setter
class Student:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

s = Student()
s.set_name("Jagruti")
print(s.get_name())


#  8  Teacher & Student (Inheritance)
class Teacher:
    def teach(self):
        print("Teacher teaches")

class Student(Teacher):
    def study(self):
        print("Student studies")

s = Student()
s.teach()
s.study()



#  9  MusicPlayer & Spotify (Override play method)
class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")

sp = Spotify()
sp.play()


#  10   super()
class Person:
    def __init__(self):
        print("Person constructor")

class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Employee constructor")

e = Employee()