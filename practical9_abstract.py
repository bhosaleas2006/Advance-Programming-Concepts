
# 1. Create an abstract class Shape with an abstract method area(). Derive Circle, Rectangle, and Triangle classes and implement the area() method for each shape. Create objects of the derived classes and display their areas.
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
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


shapes = [
    Circle(7),
    Rectangle(10, 5),
    Triangle(10, 8)
]

for shape in shapes:
    print("Area:", shape.area())


# 2. Create an abstract class Vehicle with abstract methods start() and stop(). Derive Car, Bike, and Bus classes and implement these methods.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()


# 3. Create an abstract class BankAccount with abstract methods deposit() and withdraw(). Derive SavingsAccount and CurrentAccount and implement the required operations.
class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Savings Account Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings Account Balance:", self.balance)
        else:
            print("Insufficient Balance")


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print("Current Account Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Current Account Balance:", self.balance)
        else:
            print("Insufficient Balance")


savings = SavingsAccount(10000)
savings.deposit(5000)
savings.withdraw(3000)

current = CurrentAccount(20000)
current.deposit(10000)
current.withdraw(5000)


# 4. Create an abstract class FoodOrder with abstract methods calculate_bill() and delivery_charge(). Derive RestaurantOrder and HomeDeliveryOrder and implement the methods appropriately.
class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price + self.delivery_charge()

    def delivery_charge(self):
        return 50


restaurant = RestaurantOrder(500)
print("Restaurant Bill:", restaurant.calculate_bill())
print("Restaurant Delivery Charge:", restaurant.delivery_charge())

home_delivery = HomeDeliveryOrder(500)
print("Home Delivery Bill:", home_delivery.calculate_bill())
print("Home Delivery Charge:", home_delivery.delivery_charge())


# 5. Create an abstract class Patient with abstract methods calculate_bill() and treatment(). Derive InPatient, OutPatient, and EmergencyPatient classes and implement the methods according to the patient type.
class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def __init__(self, room_charge, treatment_charge):
        self.room_charge = room_charge
        self.treatment_charge = treatment_charge

    def calculate_bill(self):
        return self.room_charge + self.treatment_charge

    def treatment(self):
        return "In-patient treatment with hospital stay"


class OutPatient(Patient):
    def __init__(self, consultation_fee, medicine_charge):
        self.consultation_fee = consultation_fee
        self.medicine_charge = medicine_charge

    def calculate_bill(self):
        return self.consultation_fee + self.medicine_charge

    def treatment(self):
        return "Out-patient consultation and medicine"


class EmergencyPatient(Patient):
    def __init__(self, emergency_fee, treatment_charge):
        self.emergency_fee = emergency_fee
        self.treatment_charge = treatment_charge

    def calculate_bill(self):
        return self.emergency_fee + self.treatment_charge

    def treatment(self):
        return "Emergency treatment"


patients = [
    InPatient(3000, 7000),
    OutPatient(500, 1500),
    EmergencyPatient(2000, 8000)
]

for patient in patients:
    print("Treatment:", patient.treatment())
    print("Bill:", patient.calculate_bill())


# 6. Create an abstract class Transport with an abstract method calculate_fare(distance). Implement subclasses Bus, Train, Taxi, and Flight. Calculate the fare according to the transportation type.
class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 15


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 10


transports = [
    Bus(),
    Train(),
    Taxi(),
    Flight()
]

distance = 100

for transport in transports:
    print("Fare for", distance, "km:", transport.calculate_fare(distance))


# 7. Create an abstract class Question with an abstract method evaluate_answer(). Derive MCQQuestion, TrueFalseQuestion, and DescriptiveQuestion. Implement answer evaluation for each question type.
class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer.upper() == self.correct_answer.upper():
            return "Correct Answer"
        return "Wrong Answer"


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer.lower() == self.correct_answer.lower():
            return "Correct Answer"
        return "Wrong Answer"


class DescriptiveQuestion(Question):
    def __init__(self, keywords):
        self.keywords = keywords

    def evaluate_answer(self, answer):
        count = 0

        for keyword in self.keywords:
            if keyword.lower() in answer.lower():
                count += 1

        if count >= 2:
            return "Answer Accepted"
        return "Answer Needs Improvement"


mcq = MCQQuestion("B")
print(mcq.evaluate_answer("B"))

true_false = TrueFalseQuestion("True")
print(true_false.evaluate_answer("True"))

descriptive = DescriptiveQuestion(["python", "object", "class"])
print(descriptive.evaluate_answer("Python is a programming language that uses class and object concepts."))


# 8. Create an abstract class Authentication with an abstract method authenticate(). Implement the method using Password authentication, OTP authentication, and Biometric authentication. Demonstrate abstraction by interacting with objects through the abstract interface.
class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def __init__(self, password):
        self.password = password

    def authenticate(self):
        if self.password == "1234":
            print("Password Authentication Successful")
        else:
            print("Password Authentication Failed")


class OTPAuthentication(Authentication):
    def __init__(self, otp):
        self.otp = otp

    def authenticate(self):
        if self.otp == "5678":
            print("OTP Authentication Successful")
        else:
            print("OTP Authentication Failed")


class BiometricAuthentication(Authentication):
    def __init__(self, biometric):
        self.biometric = biometric

    def authenticate(self):
        if self.biometric == "valid":
            print("Biometric Authentication Successful")
        else:
            print("Biometric Authentication Failed")


authentications = [
    PasswordAuthentication("1234"),
    OTPAuthentication("5678"),
    BiometricAuthentication("valid")
]

for authentication in authentications:
    authentication.authenticate()


# 9. Create an abstract class CloudStorage with abstract methods upload_file(), download_file(), and delete_file(). Create subclasses representing different storage services and implement the operations.
class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to Google Drive")

    def download_file(self, filename):
        print(filename, "downloaded from Google Drive")

    def delete_file(self, filename):
        print(filename, "deleted from Google Drive")


class OneDrive(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to OneDrive")

    def download_file(self, filename):
        print(filename, "downloaded from OneDrive")

    def delete_file(self, filename):
        print(filename, "deleted from OneDrive")


class Dropbox(CloudStorage):
    def upload_file(self, filename):
        print(filename, "uploaded to Dropbox")

    def download_file(self, filename):
        print(filename, "downloaded from Dropbox")

    def delete_file(self, filename):
        print(filename, "deleted from Dropbox")


storage_services = [
    GoogleDrive(),
    OneDrive(),
    Dropbox()
]

for storage in storage_services:
    storage.upload_file("document.pdf")
    storage.download_file("document.pdf")
    storage.delete_file("document.pdf")


# 10. Create an abstract class Appointment with abstract methods book_appointment() and calculate_fee(). Derive GeneralAppointment, SpecialistAppointment, and EmergencyAppointment.
class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    print("Appointment Fee:", appointment.calculate_fee())
