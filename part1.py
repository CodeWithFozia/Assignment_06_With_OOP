 # 1. Using self
class Student:
    def __init__(self, name, marks):
        # Initializing attributes using self
        self.name = name
        self.marks = marks

    def display(self):
        # Displaying student details
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Ali", 85)
student1.display()


# 2. Using cls
class Counter:
    count = 0  # Class variable to keep track of the number of objects created
    
    def __init__(self):
        # Increment the count whenever a new object is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        # Class method to display the count of objects created
        print(f"Number of objects created: {cls.count}")

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the count of objects created
Counter.display_count()


# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable to store the brand of the car
    
    def start(self):
        # Public method to start the car
        print(f"The {self.brand} car is now starting!")

# Example usage
my_car = Car("Toyota")  # Instantiate the Car class and pass the brand
print(my_car.brand)     # Access the public variable
my_car.start()          # Call the public method


# 4. Class Variables and Class Methods
class Bank:
    # Class variable to store the bank name
    bank_name = "Default Bank"

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Creating instances of the Bank class
bank1 = Bank()
bank2 = Bank()

# Before changing the bank name
print("Before changing bank name:")
print(f"Bank1 name: {bank1.bank_name}")
print(f"Bank2 name: {bank2.bank_name}")

# Changing the bank name using the class method
Bank.change_bank_name("SuperBank")

# After changing the bank name
print("\nAfter changing bank name:")
print(f"Bank1 name: {bank1.bank_name}")
print(f"Bank2 name: {bank2.bank_name}")


# 5. Static Variables and Static Methods
class MathUtils:
    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

# Example usage of the static method
result = MathUtils.add(5, 3)
print(f"The sum is: {result}")


# 6. Constructors and Destructors
class Logger:
    # Constructor (called when an object is created)
    def __init__(self):
        print("Logger object has been created.")
    
    # Destructor (called when an object is destroyed)
    def __del__(self):
        print("Logger object has been destroyed.")

# Creating an object of the Logger class
logger1 = Logger()

# Deleting the object to trigger the destructor message
del logger1


# 7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn           # Private variable

# Creating an object of the Employee class
emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing the public variable
print(f"Employee Name: {emp.name}")

# Accessing the protected variable (typically should be accessed within the class or subclasses)
print(f"Employee Salary: {emp._salary}")

# Trying to access the private variable will raise an AttributeError
# print(f"Employee SSN: {emp.__ssn}")  # This line will cause an error!

# Accessing the private variable using the name mangling technique
print(f"Employee SSN (using name mangling): {emp._Employee__ssn}")
