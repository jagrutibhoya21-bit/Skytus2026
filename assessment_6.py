#  1  Car Class
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print("Speed increased to:", self.speed)

    def brake(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print("Speed reduced to:", self.speed)


c1 = Car("Tata", "Nexon")
c1.accelerate(40)
c1.brake(10)


#  2  BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)


acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()


#  3   Student Class (Average Marks)
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        print("Average Marks:", avg)


s1 = Student("Amit", [70, 80, 90])
s1.average()



#   4    Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.width))


r = Rectangle(10, 5)
r.area()
r.perimeter()



#  5    Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Ravi", 25000)
e1.display()



# 6    Book Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(self.title, self.author, self.price)


b1 = Book("Python Basics", "Guido", 499)
b1.display()



# 7   Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

    def circumference(self):
        print("Circumference:", 2 * 3.14 * self.radius)


c = Circle(7)
c.area()
c.circumference()


#   8    Laptop Class (Discount)
class Laptop:
    def __init__(self, price):
        self.price = price

    def discount(self, percent):
        discount_amount = self.price * percent / 100
        final_price = self.price - discount_amount
        print("Final Price:", final_price)


l = Laptop(50000)
l.discount(10)



#   9     Flight Class (Seat Booking)
class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked")
        else:
            print("No seats available")


f = Flight(2)
f.book_seat()
f.book_seat()
f.book_seat()


# 10  Shop Class
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("Products:", self.products)


s = Shop()
s.add_product("Mobile")
s.add_product("Laptop")
s.show_products()