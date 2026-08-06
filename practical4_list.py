
# 1. Write a Python program to create a list of five fruits and display the list.

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
print("Fruit List:", fruits)


# 2. Create a list of five integers. Display:
# First element
# Last element
# Third element

numbers = [10, 20, 30, 40, 50]
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])
print("Third Element:", numbers[2])


# 3. Create a list of colors. Replace the third color with another color and display the updated list.

colors = ["Red", "Blue", "Green", "Yellow", "Black"]
colors[2] = "Purple"
print("Updated Colors:", colors)


# 4. Create a list of numbers. Add:
# One element at the end
# One element at the beginning
# One element at a specified position
# Display the updated list.

numbers = [10, 20, 30, 40]
numbers.append(50)
numbers.insert(0, 5)
numbers.insert(3, 25)
print("Updated List:", numbers)


# 5. Create a list of student names. Remove:
# First student
# Last student
# A specific student by name
# Display the remaining list.

students = ["Amit", "Ravi", "Neha", "Priya", "Kiran"]
students.pop(0)
students.pop()
students.remove("Neha")
print("Remaining Students:", students)


# 6. Write a program to find the largest and smallest number in a list without using max() or min().

numbers = [25, 12, 78, 5, 90, 34]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest Number:", largest)
print("Smallest Number:", smallest)


# 7. Accept 10 numbers from the user and store them in a list. Calculate:
# Sum
# Average

numbers = []

for i in range(10):
    num = int(input("Enter Number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)


# 8. Store 15 integers in a list. Count how many numbers are:
# Even
# Odd

numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd)


# 9. Create a list of cities. Ask the user to enter a city name and check whether it exists in the list.

cities = ["Mumbai", "Pune", "Nagpur", "Nashik", "Kolhapur"]

city = input("Enter City Name: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")


# 10. Write a program to reverse a list without using the reverse() method.

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original List:", numbers)
print("Reversed List:", reversed_list)


# 11. Create a list of 10 numbers and display:
# First 5 elements
# Last 5 elements
# Middle 4 elements
# Alternate elements
# Reverse list using slicing

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 5 Elements:", numbers[:5])
print("Last 5 Elements:", numbers[5:])
print("Middle 4 Elements:", numbers[3:7])
print("Alternate Elements:", numbers[::2])
print("Reverse List:", numbers[::-1])


# 12. Display all elements present at even index positions.

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Elements at Even Index Positions:")
for i in range(0, len(numbers), 2):
    print(numbers[i])


# 13. Accept 10 numbers and sort them in:
# Ascending order
# Descending order

numbers = []

for i in range(10):
    num = int(input("Enter Number: "))
    numbers.append(num)

ascending = numbers.copy()
ascending.sort()

descending = numbers.copy()
descending.sort(reverse=True)

print("Ascending Order:", ascending)
print("Descending Order:", descending)


# 14. Create a list containing duplicate values and display only unique elements.

numbers = [10, 20, 10, 30, 40, 20, 50, 30]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original List:", numbers)
print("Unique Elements:", unique)


# 15. Find the second largest element in a list.

numbers = [12, 45, 67, 89, 34, 78]

largest = second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest Element:", second)


# 16. Create a nested list storing:
# Student Name
# Roll Number
# Marks
# Display all student details.

students = [
    ["Amit", 1, 85],
    ["Neha", 2, 90],
    ["Ravi", 3, 78]
]

print("Student Details:")
for student in students:
    print("Name:", student[0], "Roll No:", student[1], "Marks:", student[2])


# 17. Create two 3 × 3 matrices using nested lists and perform matrix addition.

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Matrix Addition:")
for row in result:
    print(row)


# 18. Create a shopping cart using a list.
# Perform:
# Add item
# Remove item
# Search item
# Display cart
# Count total items

cart = ["Milk", "Bread", "Butter"]

cart.append("Rice")
cart.remove("Bread")

item = input("Enter item to search: ")

if item in cart:
    print("Item Found")
else:
    print("Item Not Found")

print("Shopping Cart:", cart)
print("Total Items:", len(cart))


# 19. Store names of students present in class.
# Display:
# Total students
# Search a student's attendance
# Add a new student
# Remove an absent student

students = ["Amit", "Ravi", "Neha", "Priya"]

print("Total Students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student Present")
else:
    print("Student Absent")

new_student = input("Enter new student name: ")
students.append(new_student)

absent = input("Enter absent student name: ")

if absent in students:
    students.remove(absent)

print("Updated Student List:", students)


# 20. Create a list of books.
# Implement:
# Add a new book
# Search a book
# Remove a book
# Display all books
# Count total books

books = ["Python", "Java", "C++", "HTML"]

new_book = input("Enter new book: ")
books.append(new_book)

search_book = input("Enter book to search: ")

if search_book in books:
    print("Book Found")
else:
    print("Book Not Found")

remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)

print("Books List:", books)
print("Total Books:", len(books))

# 21. Accept two lists and merge them into a single list.

list1 = []
list2 = []

print("Enter 5 elements for List 1:")
for i in range(5):
    list1.append(int(input("Enter Number: ")))

print("Enter 5 elements for List 2:")
for i in range(5):
    list2.append(int(input("Enter Number: ")))

merged_list = list1 + list2

print("Merged List:", merged_list)


# 22. Find common elements between two lists.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common Elements:", common)


# 23. Count the frequency of each element in a list.

numbers = [10, 20, 10, 30, 20, 10, 40, 30, 50]

checked = []

for i in numbers:
    if i not in checked:
        count = 0
        for j in numbers:
            if i == j:
                count += 1
        print(i, "appears", count, "times")
        checked.append(i)


# 24. Rotate a list:
# Left by one position
# Right by one position

numbers = [10, 20, 30, 40, 50]

left_rotate = numbers[1:] + numbers[:1]
right_rotate = numbers[-1:] + numbers[:-1]

print("Original List:", numbers)
print("Left Rotation:", left_rotate)
print("Right Rotation:", right_rotate)


# 25. Remove all duplicate elements while preserving the original order.

numbers = [10, 20, 10, 30, 40, 20, 50, 30, 60]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original List:", numbers)
print("List After Removing Duplicates:", unique)


# 26. Store marks of 20 students in a list and determine:
# Highest marks
# Lowest marks
# Average marks
# Number of students scoring above average
# Number of students scoring below average

marks = []

for i in range(20):
    marks.append(int(input("Enter Marks: ")))

highest = marks[0]
lowest = marks[0]
total = 0

for i in marks:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total += i

average = total / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)


# 27. Store salaries of employees and determine:
# Highest salary
# Lowest salary
# Average salary
# Employees earning above ₹50,000
# Employees earning below ₹30,000

salaries = []

n = int(input("Enter Number of Employees: "))

for i in range(n):
    salaries.append(float(input("Enter Salary: ")))

highest = salaries[0]
lowest = salaries[0]
total = 0

for i in salaries:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total += i

average = total / len(salaries)

above50000 = 0
below30000 = 0

for i in salaries:
    if i > 50000:
        above50000 += 1
    if i < 30000:
        below30000 += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees Above ₹50000:", above50000)
print("Employees Below ₹30000:", below30000)


# 28. Store scores of a batsman in 10 matches and calculate:
# Highest score
# Lowest score
# Total runs
# Average runs
# Number of centuries (≥100)
# Number of half-centuries (50–99)

scores = []

for i in range(10):
    scores.append(int(input("Enter Score: ")))

highest = scores[0]
lowest = scores[0]
total = 0
centuries = 0
half_centuries = 0

for i in scores:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total += i
    if i >= 100:
        centuries += 1
    elif i >= 50:
        half_centuries += 1

average = total / len(scores)

print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Total Runs:", total)
print("Average Runs:", average)
print("Centuries:", centuries)
print("Half-Centuries:", half_centuries)


# 29. Store the temperature of 30 days and determine:
# Hottest day
# Coldest day
# Average temperature
# Days above average temperature
# Days below average temperature

temperature = []

for i in range(30):
    temperature.append(float(input("Enter Temperature: ")))

highest = temperature[0]
lowest = temperature[0]
total = 0

for i in temperature:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total += i

average = total / len(temperature)

above = 0
below = 0

for i in temperature:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Hottest Temperature:", highest)
print("Coldest Temperature:", lowest)
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)


# 30. Store patient names and ages using lists.
# Perform:
# Add a patient
# Delete a patient
# Search a patient
# Display all patients
# Count total patients

patients = ["Amit", "Neha", "Ravi"]
ages = [25, 30, 40]

new_patient = input("Enter New Patient Name: ")
new_age = int(input("Enter Age: "))

patients.append(new_patient)
ages.append(new_age)

search = input("Enter Patient Name to Search: ")

if search in patients:
    print("Patient Found")
else:
    print("Patient Not Found")

delete = input("Enter Patient Name to Delete: ")

if delete in patients:
    index = patients.index(delete)
    patients.pop(index)
    ages.pop(index)

print("Patient Details:")
for i in range(len(patients)):
    print("Name:", patients[i], "Age:", ages[i])

print("Total Patients:", len(patients))



