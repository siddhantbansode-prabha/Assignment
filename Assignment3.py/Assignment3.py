# Assignment 3 - Python Modules & OOP Practice Coding
print("Assignment 3 - Python Modules & OOP Practice Coding")

# Section 1: Modules
print("Assignment 3 - Python Modules & OOP Practice Coding")


# Section 1: Modules

print("Section 1: Modules\n")

# Q1: Calculator functions
print("Q1: Calculator Operations")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print()


# Q2: Employee module simulation
print("Q2: Employee Details")

emp_name = "Saquib"
salary = 50000

def display_emp():
    print("Employee Name:", emp_name)
    print("Salary:", salary)

display_emp()
print()


# Q3: Math module
print("Q3: Math Operations")

import math

print("Square Root of 144:", math.sqrt(144))
print("Value of Pi:", math.pi)
print("Factorial of 6:", math.factorial(6))
print()


# Q4: Random module
print("Q4: Random Operations")

import random

print("Random Number:", random.randint(1, 100))
print("Random Choice:", random.choice(["Python", "Java", "React", "Django"]))
print()


# Q5: Area module simulation
print("Q5: Area Calculations")

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, breadth):
    return length * breadth

radius = 7
length = 10
breadth = 5

print(f"Radius = {radius}\nLength = {length}\nBreadth = {breadth}")
print("Area of Circle:", area_circle(radius))
print("Area of Rectangle:", area_rectangle(length, breadth))
print("\n")



# Section 2: Classes & Objects

print("Section 2: Classes & Objects\n")

# Q6: Student class
print("Q6: Student Class")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Siddhant", 19)

print("Name:", student1.name)
print("Age:", student1.age)
print()


# Q7: Car class
print("Q7: Car Class")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Fortuner")
car2 = Car("Honda", "City")

print("Car 1:")
print("Brand:", car1.brand)
print("Model:", car1.model)

print("Car 2:")
print("Brand:", car2.brand)
print("Model:", car2.model)
print()


# Q8: Book class
print("Q8: Book Class")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

book1 = Book("Python Basics", "Author A", 300)
book2 = Book("Java Fundamentals", "Author B", 400)
book3 = Book("React Guide", "Author C", 350)

print("Book 1:", book1.title, book1.author, book1.price)
print("Book 2:", book2.title, book2.author, book2.price)
print("Book 3:", book3.title, book3.author, book3.price)

# Q9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.
print("Q9: Create a class Laptop with attributes brand, RAM, and price. Create two objects and print information.")
class Laptop:
    brand = "iPhone"
    ram = "16 GB"
    price = 55000

laptop1 = Laptop()
laptop2 = Laptop()

print("Laptop 1:")
print("Brand:", laptop1.brand)
print("RAM:", laptop1.ram)
print("Price:", laptop1.price)
print()

print("Laptop 2:")
print("Brand:", laptop2.brand)
print("RAM:", laptop2.ram)
print("Price:", laptop2.price)
print()

# Q10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details.
print("Q10: Create a class Mobile with attributes company, model, and storage. Create multiple objects and display details.")
class Mobile:
    company = "Realme"
    model = "12 5G"
    storage = "128 GB"

mobile1 = Mobile()
mobile2 = Mobile()
mobile3 = Mobile()

print("Mobile 1:")
print("Company:", mobile1.company)
print("Model:", mobile1.model)
print("Storage:", mobile1.storage)

print("Mobile 2:")
print("Company:", mobile2.company)
print("Model:", mobile2.model)
print("Storage:", mobile2.storage)

print("Mobile 3:")
print("Company:", mobile3.company)
print("Model:", mobile3.model)
print("Storage:", mobile3.storage)
print("\n\n")


# Section 3: Constructor (__init__)
print("Section 3: Constructor")
print()

# Q11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information.
print("Q11: Create a class Employee. Use constructor to initialize emp_id, emp_name, and salary. Display employee information.")
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.salary = salary
    
    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Salary:", self.salary)

emp1 = Employee(101, "Siddhant", 90000)
emp1.display()
print()

# Q12: Create a class BankAccount. Initialize account_number, holder_name, and balance. Create two accounts and display details.
print("Q12: Create a class BankAccount. Initialize account_number, holder_name, and balance. Create two accounts and display details.")
class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def display(self):
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)
        print()

acc1 = BankAccount(1001, "Siddhant", 30000)
acc2 = BankAccount(1002, "Arun", 11000)
print("Account 1")
acc1.display()
print("Account 2")
acc2.display()
print()

# Q13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details.
print("Q13: Create a class Movie. Initialize movie_name, hero, and rating. Display movie details.")
class Movie:
    def __init__(self, movie_name, hero, rating):
        self.movie_name = movie_name
        self.hero = hero
        self.rating = rating

movie1 = Movie("Kung Fu Panda", "Po", 9.5)

print("Movie Name:", movie1.movie_name)
print("Hero:", movie1.hero)
print("Rating:", movie1.rating)
print()

# Q14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details.
print("Q14: Create a class Product. Initialize product_id, product_name, and price. Create multiple products and print details.")
class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def display(self):
        print(f"ID: {self.product_id}\nProduct: {self.product_name}\nPrice: {self.price}\n")

product1 = Product(1, "Laptop", 50000)
product2 = Product(2, "Mobile", 25000)
product3 = Product(3, "Keyboard", 1200)

print("Product 1:")
product1.display()
print("Product 2:")
product2.display()
print("Product 3:")
product3.display()
print()

# Q15: Create a class College. Initialize college_name, city, and students_count. Display details using objects.
print("Q15: Create a class College. Initialize college_name, city, and students_count. Display details using objects.")
class College:
    def __init__(self, college_name, city, students_count):
        self.college_name = college_name
        self.city = city
        self.students_count = students_count

    def display(self):
        print("College Name:", college1.college_name)
        print("City:", college1.city)
        print("Students Count:", college1.students_count)

college1 = College("Government Polytechnic", "Pune", 1200)

print("College Name:", college1.college_name)
print("City:", college1.city)
print("Students Count:", college1.students_count)
print("\n\n")


# Section 4: self Keyword
print("Section 4: self Keyword")
print()

# Q16: Create a class Person. Use self to store name and age. Display values using a method.
print("Q16: Create a class Person. Use self to store name and age. Display values using a method.")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person("Siddhant", 19)
person1.display()
print()

# Q17: Create a class Animal. Store animal_name and color. Print values using self.
print("Q17: Create a class Animal. Store animal_name and color. Print values using self.")
class Animal:
    def __init__(self, animal_name, color):
        self.animal_name = animal_name
        self.color = color

    def display(self):
        print("Animal Name:", self.animal_name)
        print("Color:", self.color)

animal1 = Animal("Peacock", "Purple")
animal1.display()
print()

# Q18: Create a class Vehicle. Store company and model. Display details using a method and self.
print("Q18: Create a class Vehicle. Store company and model. Display details using a method and self.")
class Vehicle:
    def __init__(self, company, model):
        self.company = company
        self.model = model

    def display(self):
        print("Company:", self.company)
        print("Model:", self.model)

vehicle1 = Vehicle("MG", "Alto")
vehicle1.display()
print()

# Q19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.
print("Q19: Create a class Teacher. Store teacher_name and subject. Display teacher information using self.")
class Teacher:
    def __init__(self, teacher_name, subject):
        self.teacher_name = teacher_name
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.teacher_name)
        print("Subject:", self.subject)

teacher1 = Teacher("Mr. Smith", "Java")
teacher1.display()
print()

# Q20: Create a class Player. Store player_name and team. Print details using self.
print("Q20: Create a class Player. Store player_name and team. Print details using self.")
class Player:
    def __init__(self, player_name, team):
        self.player_name = player_name
        self.team = team

    def display(self):
        print("Player Name:", self.player_name)
        print("Team:", self.team)

player1 = Player("Virat Kohli", "India")
player1.display()
print("\n\n")


# Section 5: Instance Attributes
print("Section 5: Instance Attributes")
print()

# Q21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.
print("Q21: Create a class Student with instance attributes name, roll_no, and marks. Create three students and display details.")
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

student1 = Student("Siddhant", 101, 85)
student2 = Student("Arun", 102, 84)
student3 = Student("Shravan", 103, 86)

print("Student 1:", student1.name, student1.roll_no, student1.marks)
print("Student 2:", student2.name, student2.roll_no, student2.marks)
print("Student 3:", student3.name, student3.roll_no, student3.marks)
print()

# Q22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.
print("Q22: Create a class Employee with instance attributes emp_id, emp_name, and department. Display all employee details.")
class Employee:
    def __init__(self, emp_id, emp_name, department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.department = department

emp1 = Employee(1, "Siddhant", "IT")
emp2 = Employee(2, "Arun", "HR")

print("Employee 1:", emp1.emp_id, emp1.emp_name, emp1.department)
print("Employee 2:", emp2.emp_id, emp2.emp_name, emp2.department)
print()

# Q23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details.
print("Q23: Create a class Hospital with instance attributes doctor_name and specialization. Create multiple objects and display details.")
class Hospital:
    def __init__(self, doctor_name, specialization):
        self.doctor_name = doctor_name
        self.specialization = specialization

doctor1 = Hospital("Dr. A", "Dentist")
doctor2 = Hospital("Dr. B", "Vet")

print("Doctor 1:", doctor1.doctor_name, doctor1.specialization)
print("Doctor 2:", doctor2.doctor_name, doctor2.specialization)
print()

# Q24: Create a class Course with instance attributes course_name, duration, and fees. Display course details.
print("Q24: Create a class Course with instance attributes course_name, duration, and fees. Display course details.")
class Course:
    def __init__(self, course_name, duration, fees):
        self.course_name = course_name
        self.duration = duration
        self.fees = fees

course1 = Course("Python", "3 Months", 5000)

print("Course Name:", course1.course_name)
print("Duration:", course1.duration)
print("Fees:", course1.fees)
print()

# Q25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.
print("Q25: Create a class CricketPlayer with instance attributes player_name, runs, and matches. Display player details.")
class CricketPlayer:
    def __init__(self, player_name, runs, matches):
        self.player_name = player_name
        self.runs = runs
        self.matches = matches

player1 = CricketPlayer("M.S. Dhoni", 14000, 300)

print("Player Name:", player1.player_name)
print("Runs:", player1.runs)
print("Matches:", player1.matches)
print("\n\n")


# Section 6: Instance Methods
print("Section 6: Instance Methods")
print()

# Q26: Create a class Rectangle with an instance method calculate_area(). Take length and width from constructor.
print("Q26: Create a class Rectangle with an instance method calculate_area(). Take length and width from constructor.")
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rectangle1 = Rectangle(10, 5)

print("Length:", rectangle1.length)
print("Width:", rectangle1.width)
print("Area:", rectangle1.calculate_area())
print()

# Q27: Create a class Circle with an instance method calculate_area(). Take radius from constructor.
print("Q27: Create a class Circle with an instance method calculate_area(). Take radius from constructor.")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

circle1 = Circle(7)

print("Radius:", circle1.radius)
print("Area:", circle1.calculate_area())
print()

# Q28: Create a class Employee with an instance method annual_salary(). Calculate yearly salary.
print("Q28: Create a class Employee with an instance method annual_salary(). Calculate yearly salary.")
class Employee:
    def __init__(self, emp_name, monthly_salary):
        self.emp_name = emp_name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

emp1 = Employee("Siddhant", 90000)

print("Employee Name:", emp1.emp_name)
print("Monthly Salary:", emp1.monthly_salary)
print("Annual Salary:", emp1.annual_salary())
print()

# Q29: Create a class Student with an instance method calculate_percentage(). Calculate percentage from marks.
print("Q29: Create a class Student with an instance method calculate_percentage(). Calculate percentage from marks.")
class Student:
    def __init__(self, name, marks_obtained, total_marks):
        self.name = name
        self.marks_obtained = marks_obtained
        self.total_marks = total_marks

    def calculate_percentage(self):
        return (self.marks_obtained / self.total_marks) * 100

student1 = Student("Siddhant", 400, 500)

print("Student Name:", student1.name)
print("Marks Obtained:", student1.marks_obtained)
print("Total Marks:", student1.total_marks)
print("Percentage:", student1.calculate_percentage(), "%")
print()

# Q30: Create a class BankAccount with methods deposit() and withdraw(). Update account balance.
print("Q30: Create a class BankAccount with methods deposit() and withdraw(). Update account balance.")
class BankAccount:
    def __init__(self, holder_name, balance):
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Current Balance:", self.balance)

account1 = BankAccount("Saquib", 10000)

account1.display_balance()
account1.deposit(5000)
account1.display_balance()
account1.withdraw(3000)
account1.display_balance()