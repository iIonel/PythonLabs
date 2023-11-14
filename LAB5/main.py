#EXERCITIU 1
import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * self.length + 2 * self.width

class Triangle(Shape):
    def __init__(self, lat1, lat2, lat3):
        self.lat1 = lat1
        self.lat2 = lat2
        self.lat3 = lat3

    def area(self):
        s = (self.lat1 + self.lat2 + self.lat3) / 2
        return math.sqrt(s * (s - self.lat1) * (s - self.lat2) * (s - self.lat3))

    def perimeter(self):
        return self.lat1 + self.lat2 + self.lat3


#EXERCITIU 2
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdrawal(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount


#EXERCITIU 3
class Vehicle:
    def __init__(self, make, model, year, GVM, GCM, distance):
        self.make = make
        self.model = model
        self.year = year
        self.GVM = GVM
        self.GCM = GCM
        self.distance = distance

    def calculate_mileage(self):
        pass

    def calculate_towing_capacity(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year, GVM, GCM, distance):
        super().__init__(make, model, year, GVM, GCM, distance)

    def calculate_mileage(self):
        return self.distance

    def calculate_towing_capacity(self):
        return self.GCM - self.GVM

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, GVM, GCM, distance):
        super().__init__(make, model, year, GVM, GCM, distance)

    def calculate_mileage(self):
        return self.distance

    def calculate_towing_capacity(self):
        return self.GCM - self.GVM

class Truck(Vehicle):
    def __init__(self, make, model, year, GVM, GCM, distance):
        super().__init__(make, model, year, GVM, GCM, distance)

    def calculate_mileage(self):
        return self.distance

    def calculate_towing_capacity(self):
        return self.GCM - self.GVM


#EXERCITIU 4
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def object(self):
        pass

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def object(self):
        return "Team and projects manangement"

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def object(self):
        return "Developing software"

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id, salary)
        self.sales_target = sales_target

    def object(self):
        return "Clients sales target"


#EXERCITIU 5
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def legs(self):
        pass

    def regn(self):
        pass

class Mammal(Animal):
    def __init__(self, name, habitat, color, legs):
        super().__init__(name, habitat)
        self.color = color
        self.legs = legs

    def legs(self):
        return self.legs # {EXAMPLE: 0 -> whale, 2 -> human, 4-> monkey}

class Bird(Animal):
    def __init__(self, name, habitat, wing_span):
        super().__init__(name, habitat)
        self.wing_span = wing_span

    def legs(self):
        return 2

    def wings(self):
        return 2

class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def legs(self):
        return 0

    def branhi(self):
        return 2


#EXERCITIU 6
class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} checked out successfully.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} returned successfully.")
        else:
            print(f"{self.title} is not checked out.")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.publisher = publisher
        self.issue_number = issue_number