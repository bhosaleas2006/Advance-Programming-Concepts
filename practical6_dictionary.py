# 1.	Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
student = {
    "Roll Number": 101,
    "Name": "Rahul",
    "Department": "Computer",
    "Marks": 85
}

print("Student details:")
for key, value in student.items():
    print(key, ":", value)


# 2.	Create a dictionary containing employee information and display the value associated with a specified key.
employee = {
    "ID": 101,
    "Name": "Amit",
    "Department": "Sales",
    "Salary": 50000
}

key = input("Enter a key: ")
if key in employee:
    print(employee[key])
else:
    print("Key not found")


# 3.	Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
products = {
    "Pen": 10,
    "Book": 50,
    "Bag": 500,
    "Bottle": 100,
    "Box": 80
}

products["Laptop"] = 50000

print("Products:", products)


# 4.	Create a dictionary containing student marks. Update the marks of a specified student.

marks = {
    "Amit": 80,
    "Rahul": 75,
    "Priya": 90
}

name = input("Enter student name: ")
if name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[name] = new_marks
print(marks)


# 5.	Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities = {
    "Pune": 5000000,
    "Mumbai": 12000000,
    "Delhi": 11000000
}

city = input("Enter city name to remove: ")

if city in cities:
    del cities[city]

print(cities)


# 6.	Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employees = {
    101: "Amit",
    102: "Rahul",
    103: "Priya"
}

employee_id = int(input("\nEnter employee ID: "))

if employee_id in employees:
    print("Employee exists")
else:
    print("Employee does not exist")


# 7.	Create a dictionary containing student records and find the total number of key-value pairs.
record = {
    "Roll": 1,
    "Name": "Amit",
    "Department": "Computer",
    "Marks": 85
}

print("Total key-value pairs:", len(record))


#8.	Create a dictionary and display:
# All keys
# All values
# All key-value pairs
data = {
    "A": 10,
    "B": 20,
    "C": 30
}

print("Keys:", data.keys())
print("Values:", data.values())
print("Key-value pairs:", data.items())


# 9.	Create a dictionary of programming languages and their creators. Display each key and value using a loop.
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie"
}

print("Programming languages:")

for key, value in languages.items():
    print(key, "-", value)

#10.	Accept five student names and their marks from the user and store them in a dictionary.
students = {}

print("\nEnter five student names and marks:")

for i in range(5):
    name = input("Name: ")
    mark = int(input("Marks: "))
    students[name] = mark

print(students)

#11.	Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
student = { }
print("Enter student records")
for i in range(5):
    name = input("Enter name")
    marks =int(input("Enter marks"))
    student[name]=marks
print(student)

marks = {
    "Amit": 80,
    "Rahul": 95,
    "Priya": 90
}

highest_student = max(marks, key=marks.get)

print("Highest marks:", highest_student, marks[highest_student])


# 12.	Create a dictionary containing student names and marks. Find the student with the lowest marks.
lowest_student = min(marks, key=marks.get)

print("Lowest marks:", lowest_student, marks[lowest_student])


# 13.	Create a dictionary containing student names and marks. Calculate the average marks of all students.
average = sum(marks.values()) / len(marks)

print("Average marks:", average)

# 14. Accept a string from the user and create a dictionary containing each character and its frequency.
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)


#15. Accept a sentence and create a dictionary containing each word and the number of times it occurs.
sentence = input("Enter a sentence: ")

words = sentence.split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)


#16. Create two dictionaries and merge them into a single dictionary.
d1 = {"A": 1, "B": 2}
d2 = {"C": 3, "D": 4}

merged = d1 | d2

print("Merged dictionary:", merged)


#17. Given two dictionaries, find the keys that are common to both dictionaries.
d1 = {"A": 1, "B": 2, "C": 3}
d2 = {"B": 5, "C": 6, "D": 7}

common_keys = []

for key in d1:
    if key in d2:
        common_keys.append(key)

print("Common keys:", common_keys)


# 18 Given two dictionaries, identify the values that are common to both dictionaries.
d1 = {"A": 1, "B": 2, "C": 3}
d2 = {"X": 2, "Y": 3, "Z": 5}

common_values = []

for value in d1.values():
    if value in d2.values():
        common_values.append(value)

print("Common values:", common_values)


#19 Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30
}

new_dict = {}
used_values = []

for key, value in data.items():
    if value not in used_values:
        new_dict[key] = value
        used_values.append(value)

print("Dictionary after removing duplicate values:", new_dict)


#20 Create a dictionary and display its elements in ascending order of keys.
data = {
    "C": 30,
    "A": 10,
    "B": 20
}

print("Dictionary in ascending order:")

for key in sorted(data):
    print(key, ":", data[key])


#21 Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
squares = {}

for i in range(1, 11):
    squares[i] = i * i

print("Squares:", squares)


# 22 Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
even_squares = {}

for i in range(1, 21):
    if i % 2 == 0:
        even_squares[i] = i * i

print("Even squares:", even_squares)


#23 Given a list of numbers, create a dictionary containing each unique number and its frequency.
numbers = [1, 2, 1, 3, 2, 4, 1]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency:", frequency)


# 24 Create a dictionary containing integers from 1 to 10 and their cubes.
cubes = {}

for i in range(1, 11):
    cubes[i] = i ** 3

print("Cubes:", cubes)


# 25 Create a dictionary containing student names and marks.
students = {
    "Amit": 80,
    "Rahul": 90,
    "Priya": 85
}

students["Neha"] = 88
students["Rahul"] = 95
del students["Amit"]

search = input("\nEnter student name to search: ")

if search in students:
    print("Student found:", students[search])

print("All students:", students)

highest = max(students, key=students.get)

print("Highest marks:", highest, students[highest])

average = sum(students.values()) / len(students)

print("Average:", average)


#26 Create a dictionary containing employee names and salaries.
salary = {
    "Amit": 45000,
    "Rahul": 60000,
    "Priya": 70000
}

print("Highest salary:", max(salary.values()))
print("Lowest salary:", min(salary.values()))
print("Average salary:", sum(salary.values()) / len(salary))

print("Employees earning more than 50000:")

for name, amount in salary.items():
    if amount > 50000:
        print(name)


#27 Create a dictionary containing product names and quantities.

products = {
    "Pen": 5,
    "Book": 20,
    "Bag": 8
}

products["Pencil"] = 15
products["Pen"] = 10
del products["Bag"]

search = input("Enter product name: ")

if search in products:
    print("Product found")

print("Products with quantity below 10:")

for name, quantity in products.items():
    if quantity < 10:
        print(name)


# 28 Create a dictionary containing names and phone numbers.

contacts = {
    "Amit": "9876543210",
    "Rahul": "8765432109"
}

contacts["Priya"] = "7654321098"

search = input("Enter contact name: ")

if search in contacts:
    print(contacts[search])

contacts["Rahul"] = "9999999999"
del contacts["Amit"]

print("All contacts:", contacts)


# 29 Create a dictionary containing book IDs and book names.

books = {
    101: "Python",
    102: "Java"
}

books[103] = "C Programming"

book_id = int(input("Enter book ID: "))

if book_id in books:
    print(books[book_id])

del books[102]

print("Books:", books)
print("Total books:", len(books))


# 30 Take a dictionary containing student names and their departments.Create a new dictionary that groups students according to their department.
students = {
    "Amit": "Computer",
    "Rahul": "Mechanical",
    "Priya": "Computer",
    "Neha": "Mechanical"
}

departments = {}

for student, department in students.items():
    if department not in departments:
        departments[department] = []

    departments[department].append(student)

print("Students grouped by department:")
print(departments)


# 31.Take a list of integers and a target value.Find two numbers whose sum is equal to the target using a dictionary.
numbers = [2, 7, 11, 15]

target = int(input("Enter target value: "))

data = {}

for num in numbers:
    difference = target - num

    if difference in data:
        print("Numbers are:", difference, num)
        break

    data[num] = True


# 32 Take a string, use a dictionary to find the first character that occurs only once.
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] == 1:
        print("First non-repeating character:", ch)
        break


# 33 Take a string, use a dictionary to find the first character that occurs more than once.
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch in text:
    if frequency[ch] > 1:
        print("First repeating character:", ch)
        break


# 34 Accept a paragraph and create a dictionary where:

paragraph = input("Enter a paragraph: ")

words = paragraph.split()

length_count = {}

for word in words:
    length = len(word)

    length_count[length] = length_count.get(length, 0) + 1

print(length_count)

