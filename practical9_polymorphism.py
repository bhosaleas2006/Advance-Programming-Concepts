
# 1. Create a base class Shape with a method area(). Derive Circle, Rectangle, and Triangle classes and override the area() method in each class. Create objects of each class and demonstrate runtime polymorphism.
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(7), Rectangle(10, 5), Triangle(10, 8)]

for shape in shapes:
    print("Area:", shape.area())


# 2. Create a base class Employee with a method calculate_salary(). Derive Manager, Developer, and Tester classes. Override the method in each class to calculate salary according to the employee's role.
class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 20000


class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 12000


class Tester(Employee):
    def calculate_salary(self):
        return 35000 + 7000


employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print("Salary:", employee.calculate_salary())


# 3. Create a base class Vehicle with a method start(). Derive Car, Bike, and Bus classes and override start() to display the starting behavior of each vehicle.
class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a heavy engine")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()


# 4. Create a base class Animal with a method sound(). Create subclasses Dog, Cat, Cow, and Lion. Override sound() in each class to display the appropriate sound.
class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog: Bark")


class Cat(Animal):
    def sound(self):
        print("Cat: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion: Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()


# 5. Create a base class Notification with a method send(). Derive EmailNotification, SMSNotification, and PushNotification. Override send() to display the appropriate notification method.
class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()


# 6. Create a base class Student with a method calculate_grade(). Derive EngineeringStudent, MedicalStudent, and ManagementStudent. Override the method according to different grading criteria.
class Student:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "F"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 55:
            return "C"
        else:
            return "F"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print("Grade:", student.calculate_grade(82))


# 7. Create a base class BankAccount with a method calculate_interest(). Derive SavingsAccount, CurrentAccount, and FixedDepositAccount. Override the method to calculate interest differently for each account type.
class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.04


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.07


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest(100000))


# 8. Create a base class Report with a method generate(). Derive PDFReport, ExcelReport, and HTMLReport. Override generate() in each class. Write a function that accepts any report object and calls generate().
class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def generate_report(report):
    report.generate()


reports = [PDFReport(), ExcelReport(), HTMLReport()]

for report in reports:
    generate_report(report)


# 9. Create a class Distance with feet and inches. Overload the + operator to add two distance objects and display the result in normalized form.
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        feet = self.feet + other.feet + total_inches // 12
        inches = total_inches % 12
        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(6, 9)

d3 = d1 + d2
d3.display()


# 10. Create a class Student containing the student's name and total marks. Overload the > and < operators to compare the marks of two students.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = Student("Adarsh", 450)
student2 = Student("Rahul", 420)

print("Student 1 has greater marks:", student1 > student2)
print("Student 1 has smaller marks:", student1 < student2)


# 11. Create a class Product with product name and price. Overload the == and > operators to compare two products based on their prices.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 40000)

print("Prices are equal:", product1 == product2)
print("Product 1 is more expensive:", product1 > product2)


# 12. Develop an online shopping payment module using polymorphism. Create a base class Payment and derived classes UPIPayment, CardPayment, and WalletPayment. Each class should implement its own make_payment() method. Demonstrate polymorphism using a common function.
class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI Payment of", amount, "completed")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card Payment of", amount, "completed")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet Payment of", amount, "completed")


def process_payment(payment, amount):
    payment.make_payment(amount)


payments = [
    UPIPayment(),
    CardPayment(),
    WalletPayment()
]

for payment in payments:
    process_payment(payment, 5000)


# 13. Create a base class Person with a method display_role(). Derive Student, Faculty, and Administrator. Override the method to display the respective role. Store all objects in a list and invoke the same method using a loop.
class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [Student(), Faculty(), Administrator()]

for person in people:
    person.display_role()


# 14. Create a base class Media with a method play(). Derive Audio, Video, and Podcast. Override play() according to the media type.
class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


media_list = [Audio(), Video(), Podcast()]

for media in media_list:
    media.play()


# 15. Create a base class SmartDevice with methods turn_on() and turn_off(). Derive Light, Fan, AC, and TV. Override the methods according to each device.
class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light turned ON")

    def turn_off(self):
        print("Light turned OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan started")

    def turn_off(self):
        print("Fan stopped")


class AC(SmartDevice):
    def turn_on(self):
        print("AC turned ON")

    def turn_off(self):
        print("AC turned OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV turned ON")

    def turn_off(self):
        print("TV turned OFF")


devices = [Light(), Fan(), AC(), TV()]

for device in devices:
    device.turn_on()
    device.turn_off()
