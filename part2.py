# 8. The super() Function
# Base class Person
class Person:
    def __init__(self, name):
        self.name = name  # Constructor to set the name

# Derived class Teacher inherits from Person
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the base class (Person) constructor
        self.subject = subject  # Adding a subject field for the Teacher class

# Creating an object of the Teacher class
teacher = Teacher("John Doe", "Mathematics")

# Printing the name and subject of the teacher
print(f"Teacher Name: {teacher.name}")
print(f"Teacher Subject: {teacher.subject}")


# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method to be implemented by subclasses

# Subclass Rectangle that implements area()
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Create a Rectangle object
rect = Rectangle(5, 3)

# Print the area of the rectangle
print(f"Area of the rectangle: {rect.area()} square units")


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed
    
    # Instance method that prints a message including the dog's name
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

# Creating an object of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Calling the bark method
dog1.bark()


# 11. Class Methods
class Book:
    # Class variable to keep track of the total number of books
    total_books = 0

    # Constructor to initialize the book's name and author
    def __init__(self, name, author):
        self.name = name
        self.author = author
        # Call the class method to increment the total book count when a new book is created
        Book.increment_book_count()

    # Class method to increment the book count
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Creating instances of the Book class
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Printing the total number of books
print(f"Total books: {Book.total_books}")


# 12. Static Methods
class TemperatureConverter:
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage of the static method
celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")


# 13. Composition
# Class Engine with a method start
class Engine:
    def __init__(self, model):
        self.model = model
    
    def start(self):
        print(f"Engine {self.model} is starting... Vroom Vroom!")

# Class Car that uses composition by having an Engine object
class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine
    
    def start_car(self):
        print(f"{self.make} {self.model} is ready to go!")
        self.engine.start()  # Accessing Engine's method via Car

# Creating an Engine object
engine1 = Engine("V8")

# Creating a Car object, passing the Engine object to it
car1 = Car("Ford", "Mustang", engine1)

# Accessing the method of Engine via the Car object
car1.start_car()


# 14. Aggregation
# Class Employee
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")

# Class Department that uses aggregation to store a reference to an Employee
class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # This will store multiple Employee objects
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_department_info(self):
        print(f"Department: {self.department_name}")
        for employee in self.employees:
            employee.display_employee_info()

# Creating Employee objects
emp1 = Employee("Alice", "Manager")
emp2 = Employee("Bob", "Developer")

# Creating a Department object
dept = Department("Engineering")

# Aggregating Employee objects to the Department
dept.add_employee(emp1)
dept.add_employee(emp2)

# Displaying information about the department and its employees
dept.display_department_info()
