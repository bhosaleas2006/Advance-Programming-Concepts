
#1.	Create a class Student with attributes such as roll_no, name, and marks. Create objects for multiple students and display their details and percentage.
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")


students = [
    Student(1, "Adarsh", [85, 90, 88, 92, 87]),
    Student(2, "Rahul", [78, 82, 80, 85, 81]),
    Student(3, "Sneha", [90, 88, 95, 91, 94])
]

for student in students:
    student.display()
    print()

#2.	Create a class Employee with attributes emp_id, name, and basic_salary. Define methods to calculate HRA, DA, and gross salary.

class Employee:
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id =emp_id
        self.name = name
        self.basic_salary = basic_salary

    def HRA(self):
        return self.basic_salary * 0.20
    def DA(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.HRA() + self.DA()

e = Employee(101,"Adarsha",100000)
e.HRA()
e.DA()
e.gross_salary()

print("Employee ID:", employee.emp_id)
print("Name:", e.name)
print("Basic Salary:", e.basic_salary)
print("HRA:", e.HRA())
print("DA:", e.DA())
print("Gross Salary:", e.gross_salary())


#3.	Create a class Rectangle with attributes length and breadth. Define methods to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rectangle = Rectangle(10, 5)

print("\nLength:", rectangle.length)
print("Breadth:", rectangle.breadth)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())


# 4. Create a class Circle with an attribute radius. Define methods to calculate the area and circumference of the circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14159 * self.radius


circle = Circle(7)

print("\nRadius:", circle.radius)
print("Area:", circle.area())
print("Circumference:", circle.circumference())


# 5. Create a class Book containing book_id, title, author, and price. Create objects for three books and display their information.
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


books = [
    Book(1, "Python Programming", "John Smith", 500),
    Book(2, "Data Structures", "Robert Brown", 600),
    Book(3, "Machine Learning", "David Miller", 750)
]

for book in books:
    print()
    book.display()


# 6. Create a class ElectricityBill containing consumer number, consumer name, and units consumed. Define a method to calculate the electricity bill according to different unit slabs.
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 1.50
        elif self.units <= 200:
            bill = 100 * 1.50 + (self.units - 100) * 2.50
        elif self.units <= 500:
            bill = 100 * 1.50 + 100 * 2.50 + (self.units - 200) * 4.00
        else:
            bill = 100 * 1.50 + 100 * 2.50 + 300 * 4.00 + (self.units - 500) * 6.00

        return bill

    def display(self):
        print("\nConsumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())


bill = ElectricityBill(1001, "Adarsh", 350)
bill.display()


# 7. Create a class MobilePhone with attributes brand, model, storage, and price. Define methods to display specifications and calculate the price after discount.
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("\nBrand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def price_after_discount(self, discount):
        return self.price - (self.price * discount / 100)


phone = MobilePhone("Samsung", "Galaxy A55", "128 GB", 35000)

phone.display_specs()
print("Price after 10% discount:", phone.price_after_discount(10))


# 8. Create a class Patient containing patient ID, name, age, disease, and consultation fee. Define methods to display patient information and calculate the total bill.
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("\nPatient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_charge, room_charge):
        return self.consultation_fee + medicine_charge + room_charge


patient = Patient(501, "Rahul", 35, "Fever", 500)

patient.display()
print("Total Bill:", patient.total_bill(1000, 2000))


# 9. Design an ATM class that allows a user to check balance, deposit money, withdraw money, and display account details. Create an object of the class and implement the operations through a menu-driven program.
class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


atm = ATM(123456, "Adarsh", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.display_account()
    elif choice == 5:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid Choice")


# 10. Create a class Vehicle containing vehicle number, model, rental rate, and availability. Implement methods to rent and return a vehicle and calculate rental charges based on the number of days.
class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = True

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self):
        self.availability = True
        print("Vehicle returned successfully")

    def rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("\nVehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.availability)


vehicle = Vehicle("MH09AB1234", "Swift", 1500)

vehicle.display()
vehicle.rent()
print("Rental Charges for 3 days:", vehicle.rental_charges(3))
vehicle.return_vehicle()
vehicle.display()


# 11. Create a class ShoppingCart with customer name and cart ID. Initialize these values using a constructor. Implement methods to add products, remove products, and calculate the total bill. Use a destructor to display a message when the shopping cart object is destroyed.
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart")
                return
        print("Product not found")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]
        return total

    def __del__(self):
        print("Shopping cart object destroyed")


cart = ShoppingCart("Adarsh", "C101")

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

cart.remove_product("Mouse")

print("\nCustomer Name:", cart.customer_name)
print("Cart ID:", cart.cart_id)
print("Total Bill:", cart.total_bill())


# 12. Create a class FoodOrder with order ID, customer name, food item, quantity, and price. Use a constructor to initialize the order. Define a method to calculate the total bill including tax. Implement a destructor to display an order completion message.
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        amount = self.quantity * self.price
        tax = amount * 0.05
        return amount + tax

    def display(self):
        print("\nOrder ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Total Bill Including Tax:", self.total_bill())

    def __del__(self):
        print("Order completed")


order = FoodOrder(1001, "Adarsh", "Pizza", 2, 300)
order.display()


# 13. Create a class StudentResult with student name and marks in five subjects. Use a constructor to initialize the details. Define methods to calculate total, percentage, and grade. Implement a destructor to display a suitable message.
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed")


result = StudentResult("Adarsh", [90, 85, 88, 92, 87])
result.display()


    
        
