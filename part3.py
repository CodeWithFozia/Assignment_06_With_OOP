# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Class A with method show()
class A:
    def show(self):
        print("A's show method")

# Class B inheriting from A and overriding show()
class B(A):
    def show(self):
        print("B's show method")

# Class C inheriting from A and overriding show()
class C(A):
    def show(self):
        print("C's show method")

# Class D inheriting from both B and C
class D(B, C):
    pass  # No need to override show() in D, will use MRO to decide

# Create an object of D
d = D()

# Call show() method
d.show()

# Display the MRO (Method Resolution Order)
print("MRO of class D:", D.__mro__)


# 16. Function Decorators
# Decorator function that logs the function call
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Call the original function
    return wrapper

# Applying the decorator to say_hello function
@log_function_call
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()


# 17. Class Decorators
# Class decorator that adds a greet() method to a class
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # Adding the greet method to the class
    cls.greet = greet
    return cls

# Applying the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_name(self):
        return f"My name is {self.name}"

# Creating an object of the Person class
person = Person("Alice")

# Calling the greet() method added by the decorator
print(person.greet())  # Output: Hello from Decorator!
print(person.say_name())  # Output: My name is Alice


# 18. Property Decorators: @property, @setter, and @deleter
class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    # @property to get the price
    @property
    def price(self):
        return self._price
    
    # @price.setter to update the price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    # @price.deleter to delete the price
    @price.deleter
    def price(self):
        print("Price is being deleted.")
        del self._price

# Creating a Product object
product = Product(100)

# Getting the price
print(f"Price: {product.price}")  # Output: Price: 100

# Setting a new price
product.price = 150
print(f"Updated Price: {product.price}")  # Output: Updated Price: 150

# Trying to set a negative price (will raise an error)
try:
    product.price = -50
except ValueError as e:
    print(e)  # Output: Price cannot be negative

# Deleting the price
del product.price  # Output: Price is being deleted.


# 19. callable() and __call__()
# Class Multiplier with __init__ and __call__
class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Initialize with a factor

    # __call__ method to make the object callable
    def __call__(self, number):
        return number * self.factor

# Creating an instance of Multiplier with a factor of 5
multiplier = Multiplier(5)

# Testing if the object is callable using callable()
print(callable(multiplier))  # Output: True

# Calling the object like a function to multiply a number by the factor
result = multiplier(10)  # Equivalent to multiplier.__call__(10)
print(f"10 multiplied by 5 is: {result}")  # Output: 10 multiplied by 5 is: 50


# 20. Creating a Custom Exception
# Custom exception InvalidAgeError
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")
    else:
        print(f"Age {age} is valid.")

# Handling the exception using try...except
try:
    # Test with an age less than 18
    age = 16
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")

# Test with an age greater than or equal to 18
try:
    age = 20
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")


# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start  # Initialize with a start number
    
    # __iter__ method to return the iterator object (self in this case)
    def __iter__(self):
        self.current = self.start  # Set current to the start value
        return self
    
    # __next__ method to return the next value in the countdown
    def __next__(self):
        if self.current <= 0:  # If the current number is 0 or less, stop the iteration
            raise StopIteration
        self.current -= 1  # Decrement the current value by 1
        return self.current  # Return the current value

# Create a Countdown object starting from 5
countdown = Countdown(5)

# Use a for-loop to iterate through the countdown
for number in countdown:
    print(number)

