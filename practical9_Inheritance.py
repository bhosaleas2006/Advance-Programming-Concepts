
# 1. Create a class Employee with attributes emp_id, name, and salary. Create a derived class Manager that inherits from Employee and contains an additional attribute department. Display all employee and manager details and calculate the manager's annual salary.
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


manager = Manager(101, "Adarsh", 50000, "IT")
manager.display_manager()


# 2. Create a base class Vehicle with attributes brand and model. Create a derived class Car with additional attributes fuel_type and price. Define methods to display vehicle details and calculate the discounted price of the car.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


car = Car("Toyota", "Fortuner", "Diesel", 3500000)
car.display_car()
print("Discounted Price:", car.discounted_price(10))


# 3. Create two classes Academic and Sports. The Academic class should store marks obtained by a student, while the Sports class should store sports points. Create a class Student that inherits from both classes and calculates the student's overall performance.
class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def performance(self):
        total = self.marks + self.sports_points
        print("Name:", self.name)
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", total)


student = Student("Adarsh", 85, 15)
student.performance()


# 4. Create classes PersonalDetails and ProfessionalDetails. Store personal information such as name and age in the first class and employee ID, designation, and salary in the second class. Create an Employee class that inherits from both classes and displays complete employee information.
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


employee = Employee("Rahul", 30, 101, "Software Engineer", 60000)
employee.display()


# 5. Create a class Person containing name and age. Derive a class Student from Person with roll number and course. Further derive a class ResearchStudent from Student with research topic and guide name. Display all details.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Adarsh", 21, 101, "Computer Engineering",
    "Artificial Intelligence", "Dr. Patil"
)
research_student.display()


# 6. Create a base class BankAccount with account number and balance. Derive SavingsAccount from it with an interest rate. Further derive PremiumSavingsAccount with additional benefits. Define methods to calculate interest and display account details.
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


account = PremiumSavingsAccount(
    123456, 100000, 7, "Free ATM and Priority Banking"
)
account.display()


# 7. Create a base class Shape containing a method to display the name of the shape. Create three derived classes Circle, Rectangle, and Triangle. Each class should implement its own method to calculate the area.
class Shape:
    def display_name(self):
        print("Shape:", self.name)


class Circle(Shape):
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.name = "Rectangle"
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.name = "Triangle"
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(7)
circle.display_name()
print("Area:", circle.area())

rectangle = Rectangle(10, 5)
rectangle.display_name()
print("Area:", rectangle.area())

triangle = Triangle(10, 8)
triangle.display_name()
print("Area:", triangle.area())


# 8. Create a base class Employee containing employee ID, name, and basic salary. Create derived classes Manager, Developer, and Tester. Each derived class should calculate salary differently based on its respective allowances.
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.40


class Developer(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Tester(Employee):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20


manager = Manager(101, "Adarsh", 50000)
developer = Developer(102, "Rahul", 40000)
tester = Tester(103, "Sneha", 35000)

print("Manager Salary:", manager.salary())
print("Developer Salary:", developer.salary())
print("Tester Salary:", tester.salary())


# 9. Create a class Person. Derive Student and Faculty from Person. Create another class TeachingAssistant that inherits from both Student and Faculty. Display the details and demonstrate the use of multiple and hierarchical inheritance together.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, age, faculty_id):
        super().__init__(name, age)
        self.faculty_id = faculty_id


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, faculty_id):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.faculty_id = faculty_id

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student Roll No:", self.roll_no)
        print("Faculty ID:", self.faculty_id)


ta = TeachingAssistant("Adarsh", 22, 101, "F501")
ta.display()


# 10. Create a base class Vehicle. Derive Car and Bike from Vehicle. Create a class SportsCar that inherits from Car and another class ElectricBike that inherits from Bike. Add suitable attributes and methods to demonstrate a combination of inheritance types.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Top Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery, "kWh")


sports_car = SportsCar("Ferrari", "488", 340)
sports_car.display()

electric_bike = ElectricBike("Ola", "S1 Pro", 4)
electric_bike.display()


# 11. Create a base class Student with attributes roll_no, name, and course. Derive a class Result that stores marks in three subjects and calculates total marks, percentage, and grade.
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

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
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())


result = Result(101, "Adarsh", "Computer Engineering", [90, 85, 88])
result.display()


# 12. Create a class Product with product ID, name, and price. Derive ElectronicProduct with additional attributes such as brand and warranty. Calculate the final price after applying a discount.
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Price:", self.price)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)
        print("Final Price:", self.final_price(10))


product = ElectronicProduct(
    101, "Laptop", 60000, "HP", "2 Years"
)
product.display()


# 13. Create classes Printer and Scanner with suitable methods for printing and scanning documents. Create a MultifunctionDevice class that inherits from both and supports both operations.
class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        self.print_document()
        self.scan_document()


device = MultifunctionDevice()
device.display()


# 14. Create classes Camera and Phone. The Camera class should provide methods for taking photographs, while Phone should provide methods for making calls. Create a Smartphone class inheriting from both.
class Camera:
    def take_photo(self):
        print("Taking photograph")


class Phone:
    def make_call(self, number):
        print("Calling:", number)


class Smartphone(Camera, Phone):
    def use_device(self):
        self.take_photo()
        self.make_call("9876543210")


smartphone = Smartphone()
smartphone.use_device()


# 15. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research = ResearchStudent(
    "Adarsh", 21, 101, "Computer Engineering",
    "Machine Learning", "Dr. Patil"
)
research.display()


# 16. Create a class Person with name and age. Derive Student with roll number and course. Further derive ResearchStudent with research topic and guide name.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


research_student = ResearchStudent(
    "Rahul", 22, 102, "Information Technology",
    "Artificial Intelligence", "Dr. Sharma"
)
research_student.display()


# 17. Create a base class Animal with common attributes and methods. Derive Dog, Cat, and Cow classes and implement their specific sounds and behaviors.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Dog(Animal):
    def sound(self):
        print("Sound: Bark")

    def behavior(self):
        print("Behavior: Loyal")


class Cat(Animal):
    def sound(self):
        print("Sound: Meow")

    def behavior(self):
        print("Behavior: Independent")


class Cow(Animal):
    def sound(self):
        print("Sound: Moo")

    def behavior(self):
        print("Behavior: Calm")


dog = Dog("Tommy", 3)
dog.display()
dog.sound()
dog.behavior()

cat = Cat("Kitty", 2)
cat.display()
cat.sound()
cat.behavior()

cow = Cow("Gauri", 5)
cow.display()
cow.sound()
cow.behavior()


# 18. Create a class Person and derive Doctor and Patient. Create additional classes representing Surgeon and MedicalResearcher. Design the hierarchy so that the program demonstrates multiple inheritance along with hierarchical inheritance.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_doctor(self):
        self.display_person()
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def display_patient(self):
        self.display_person()
        print("Disease:", self.disease)


class Surgeon(Doctor):
    def __init__(self, name, age, specialization, surgery):
        super().__init__(name, age, specialization)
        self.surgery = surgery

    def display_surgeon(self):
        self.display_doctor()
        print("Surgery:", self.surgery)


class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, age, specialization, disease, research_area):
        Person.__init__(self, name, age)
        self.specialization = specialization
        self.disease = disease
        self.research_area = research_area

    def display_researcher(self):
        self.display_person()
        print("Specialization:", self.specialization)
        print("Disease:", self.disease)
        print("Research Area:", self.research_area)


surgeon = Surgeon(
    "Dr. Patil", 45, "Cardiology", "Heart Surgery"
)
surgeon.display_surgeon()

researcher = MedicalResearcher(
    "Dr. Sharma", 40, "Neurology", "Brain Disorder",
    "Medical AI"
)
researcher.display_researcher()
