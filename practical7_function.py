
#1. Write a function factorial(n) that accepts an integer and returns its factorial.
def fact(n):
    f=1
    for i in range(1,n+1):
        f = i * f

    return f
print(fact(5))

#2. Write a function check_even_odd(n) that determines whether a given number is even or odd.

def check_even_odd(n):
    if n % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
check_even_odd(2)

#3.	Define a function that accepts two numbers and returns the greater number.
def greater(n1,n2):
    if n1 > n2:
        print(n1,"is greater than",n2)
    else:
        print(n2,"is greater than",n1)

greater(3,7)

#4. Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    return (p * r * t) / 100

print("4.", simple_interest(10000, 5, 2))


#5. Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
def is_prime(n):
    if n < 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("5.", is_prime(17))


# 6. Define a function to calculate the area of a circle using its radius.
def circle_area(radius):
    return 3.14 * radius * radius

print("6.", circle_area(5))


# 7. Write a function that accepts n and returns the sum of the first n natural numbers.
def natural_sum(n):
    return n * (n + 1) // 2

print("7.", natural_sum(10))


# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    return base ** exponent

print("8.", power(2, 5))

#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function
def largest(list):
    large =list[0]
    for i in list:
        if i > large:
            large=i
    return large
print("Largest",largest([12,56,32,12,97,98,52]))
   
#10. Define a function that accepts a string and returns the number of vowels present in it.
def countvowel(str):
    count=0
    for i in str.lower():
        if i in "aeiou":
            count +=1
    return count
print(countvowel("Adarsha"))
   
#11.Write a function that accepts a string and returns its reverse.
def reverse_string(string):
    reverse = ""
    
    for char in string:
        reverse = char + reverse
    
    return reverse


string = input("Enter a string: ")

result = reverse_string(string)

print("Original String:", string)
print("Reversed String:", result)

#12.Create a function that checks whether a given string or number is a palindrome.
def reverse_string(string):
    reverse = ""
    
    for char in string:
        reverse = char + reverse
    
    return reverse


string = input("Enter a string: ")

result = reverse_string(string)

print("Original String:", string)
print("Reversed String:", result)

# 13. Write a function that accepts a list of numbers and returns their average.
def average(numbers):
    return sum(numbers) / len(numbers)

print( average([10, 20, 30, 40, 50]))

#14.Define a function that accepts a list and an element and returns the number of times that element occurs.
def countitem(list,ele):
    count = 0
    for i in list:
        if i == ele:
            count +=1
    return count

print("Count:",countitem([1,2,3,4,5,2,6,2],2))

# 15. Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

print(unique_elements([1, 2, 2, 3, 4, 4, 5]))


# 16. Create a function to find the second-largest number in a list.
def second_largest(numbers):
    unique = list(set(numbers))
    unique.sort()
    return unique[-2]

print( second_largest([10, 30, 20, 50, 40]))


# 17. Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

print(fibonacci(8))

#18.	Create a function that accepts marks in five subjects and returns the student's percentage and grade.
def percentage_grade(m1, m2, m3, m4, m5):
    percentage = (m1 + m2 + m3 + m4 + m5) / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

print("18.", percentage_grade(85, 90, 80, 75, 88))

#19.	Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

print(electricity_bill(250))
#20.	Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.

def salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

print(salary(30000))

#21.	Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    if total >= 5000:
        discount = total * 0.10
    elif total >= 2000:
        discount = total * 0.05
    else:
        discount = 0

    return total - discount

print("21.", total_bill([1000, 500, 2000], [2, 2, 1]))

#22.	Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.

def number_details(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    avg = total / len(numbers)

    return minimum, maximum, total, avg

print( number_details([10, 20, 30, 40, 50]))

#23.	Write a program using separate functions to process student records containing name, roll number, and marks in five subjects. Calculate total, percentage, grade, class average, highest scorer, and lowest scorer.
def student_total(marks):
    return sum(marks)


def student_percentage(marks):
    return sum(marks) / 5


def student_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "F"


def process_students(students):
    percentages = []

    for student in students:
        total = student_total(student["marks"])
        percentage = student_percentage(student["marks"])
        grade = student_grade(percentage)
        percentages.append(percentage)

        print(student["name"], student["roll"], total, percentage, grade)

    print("Class Average:", sum(percentages) / len(percentages))

    highest = max(students, key=lambda x: student_percentage(x["marks"]))
    lowest = min(students, key=lambda x: student_percentage(x["marks"]))

    print("Highest Scorer:", highest["name"])
    print("Lowest Scorer:", lowest["name"])


students = [
    {"name": "Amit", "roll": 1, "marks": [80, 85, 90, 75, 88]},
    {"name": "Rahul", "roll": 2, "marks": [70, 75, 65, 80, 72]},
    {"name": "Sneha", "roll": 3, "marks": [90, 92, 95, 88, 91]}
]


process_students(students)


# 24. Create functions for deposit, withdrawal, balance enquiry, and transaction history. Prevent withdrawal when the balance is insufficient and maintain a transaction record.
balance = 0
transactions = []


def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited " + str(amount))


def withdrawal(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")


def balance_enquiry():
    return balance


def transaction_history():
    return transactions



deposit(5000)
withdrawal(1500)
print("Balance:", balance_enquiry())
print("Transactions:", transaction_history())


# 25. Create functions to add books, issue books, return books, search books, and display available books. Maintain book availability using dictionaries.
books = {}


def add_book(book, author):
    books[book] = {"author": author, "available": True}


def issue_book(book):
    if book in books and books[book]["available"]:
        books[book]["available"] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book(book):
    if book in books:
        books[book]["available"] = True
        print("Book returned")


def search_book(book):
    if book in books:
        print(books[book])
    else:
        print("Book not found")


def display_available():
    for book in books:
        if books[book]["available"]:
            print(book)



add_book("Python", "Guido")
add_book("Java", "James")
issue_book("Python")
return_book("Python")
search_book("Python")
display_available()


# 26. Develop a modular program using functions to calculate electricity bills using different consumption slabs. Include fixed charges, taxes, and discounts.
def calculate_units_charge(units):
    if units <= 100:
        return units * 5
    elif units <= 200:
        return 100 * 5 + (units - 100) * 7
    else:
        return 100 * 5 + 100 * 7 + (units - 200) * 10


def calculate_electricity_final_bill(units):
    fixed_charge = 100
    charge = calculate_units_charge(units)
    tax = charge * 0.05
    discount = charge * 0.10 if units < 100 else 0

    return charge + fixed_charge + tax - discount


print( calculate_electricity_final_bill(250))


# 27. Create functions to calculate consultation charges, laboratory charges, medicine charges, room charges, and final bill. Apply discounts based on patient category.
def consultation_charge(amount):
    return amount


def laboratory_charge(amount):
    return amount


def medicine_charge(amount):
    return amount


def room_charge(amount):
    return amount


def patient_bill(consultation, laboratory, medicine, room, category):
    total = (
        consultation_charge(consultation)
        + laboratory_charge(laboratory)
        + medicine_charge(medicine)
        + room_charge(room)
    )

    if category == "senior":
        discount = total * 0.20
    elif category == "regular":
        discount = total * 0.10
    else:
        discount = 0

    return total - discount


print(patient_bill(500, 1500, 2000, 3000, "senior"))


# 28. Implement functions to add/remove products, calculate subtotal, apply coupon discounts, calculate GST, and generate the final invoice.
cart = {}


def add_product(name, price, quantity):
    cart[name] = [price, quantity]


def remove_product(name):
    if name in cart:
        del cart[name]


def calculate_subtotal():
    total = 0
    for product in cart.values():
        total += product[0] * product[1]
    return total


def apply_coupon(subtotal, coupon):
    if coupon == "SAVE10":
        return subtotal * 0.90
    return subtotal


def calculate_gst(amount):
    return amount * 0.18


def final_invoice(coupon):
    subtotal = calculate_subtotal()
    discounted = apply_coupon(subtotal, coupon)
    gst = calculate_gst(discounted)

    print("Subtotal:", subtotal)
    print("After Discount:", discounted)
    print("GST:", gst)
    print("Final Amount:", discounted + gst)


add_product("Laptop", 50000, 1)
add_product("Mouse", 1000, 2)
final_invoice("SAVE10")


# 29. Write a recursive function to search for an element in a sorted list using binary search.
def binary_search(numbers, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if numbers[mid] == target:
        return mid
    elif target < numbers[mid]:
        return binary_search(numbers, target, low, mid - 1)
    else:
        return binary_search(numbers, target, mid + 1, high)


numbers = [10, 20, 30, 40, 50, 60]
print( binary_search(numbers, 40, 0, len(numbers) - 1))


# 30. Convert a decimal number into binary using recursion without using Python's built-in conversion functions.
def decimal_to_binary(n):
    if n == 0:
        return ""

    return decimal_to_binary(n // 2) + str(n % 2)


print( decimal_to_binary(10))


# 31. Check whether a string is a palindrome using recursion.
def recursive_palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return recursive_palindrome(text[1:-1])


print("31.", recursive_palindrome("madam"))

#32.	Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculate(a, b, operation):
    return operation(a, b)


print("32.", calculate(10, 5, addition))
print(calculate(10, 5, subtraction))
print(calculate(10, 5, multiplication))
print(calculate(10, 5, division))

#---------------------------------------------Lambda Function--------------------------------------------

#33.Write a lambda function to calculate the square of a given number.
square = lambda n: n * n

print(square(5))

#34.Create a lambda function that returns the cube of a number.
cube = lambda n: n * n * n

print(cube(5))

#35.Write a lambda function that returns True if a number is even and False otherwise.
even = lambda n : n % 2 == 0
print(even(4))
print(even(5))

#36.Use a lambda function to find the maximum of two numbers.

max = lambda a,b : a if a > b else b
print(max(12,67))

#37.Create a lambda function to calculate simple interest using principal, rate, and time.
simple_interest = lambda p ,r,t: (p * r * t) /100
print(simple_interest(10000,10,2))

#38.Take a list of numbers, use map() and a lambda function to generate a list containing their squares.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n * n, numbers))

print(squares)

# 39. Use map() with lambda to calculate the cube of every element in a list.
numbers = [1, 2, 3, 4, 5]
cubes = list(map(lambda n: n ** 3, numbers))

print(cubes)

# 40. Take two lists of numbers, use map() and lambda to create a third list containing the sum of corresponding elements.
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

result = list(map(lambda a, b: a + b, list1, list2))

print(result)


# 41. Take a list of integers, use filter() and lambda to extract all even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))

print(even_numbers)


# 42. Take a list of integers, use filter() with an appropriate lambda expression to identify prime numbers.
def prime_check(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


numbers = [2, 3, 4, 5, 6, 7, 8, 11]
prime_numbers = list(filter(lambda n: prime_check(n), numbers))

print(prime_numbers)


# 43. Use filter() and lambda to extract positive numbers from a list.
numbers = [-5, -2, 0, 3, 7, -1, 10]
positive = list(filter(lambda n: n > 0, numbers))

print(positive)


# 44. Take a list of numbers, use filter() and lambda to find numbers greater than 50.
numbers = [20, 55, 40, 70, 90, 30]
greater_than_50 = list(filter(lambda n: n > 50, numbers))

print(greater_than_50)


# 45. Take a list of words, use filter() and lambda to find words having more than five characters.
words = ["apple", "banana", "cat", "orange", "computer"]
long_words = list(filter(lambda word: len(word) > 5, words))

print(long_words)

#46.Take a list of words; sort them according to their length using lambda.
words = ["apple", "banana", "cat", "orange", "computer"]
sort = sorted(words,key = lambda word : len(word) )
print(sort)

#47.Take a list of tuples containing student names and marks, sort the students according to their marks using lambda.
students=[("Ramesh",90),("Suresh",89),("Mukesh",88),("Rakesh",99)]
sort = sorted(students,key = lambda student :student[1])
print(sort)

#48.Take employee records containing name and salary, sort them according to salary using lambda.
employees = [("Amit", 50000),("Rahul", 70000),("Sneha", 60000),("Neha", 45000)]

sorted_employees = sorted(employees, key=lambda employee: employee[1])

# 49. Take a list containing student names and marks, use functions and lambda expressions to: a) Calculate average marks. b) Filter students scoring above 75. c) Sort students according to marks.
students = [("Amit", 80),("Rahul", 65),("Sneha", 90),("Neha", 72)
]


def student_average(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)


def students_above_75(students):
    return list(filter(lambda student: student[1] > 75, students))


def sort_students(students):
    return sorted(students, key=lambda student: student[1])


print("Average:", student_average(students))
print("Above 75:", students_above_75(students))
print("Sorted:", sort_students(students))


# 50. Take employee records containing name, department, and salary, use filter(), map(), and sorted() with lambda functions to: a) Find employees earning more than ₹50,000. b) Increase salaries by 10%. c) Sort employees according to salary.
employees = [("Amit", "IT", 60000),("Rahul", "HR", 45000),("Sneha", "IT", 75000),("Neha", "Sales", 55000)
]

high_salary = list(filter(lambda employee: employee[2] > 50000, employees))

increased_salary = list(
    map(lambda employee: (employee[0], employee[1], employee[2] * 1.10), employees)
)

sorted_salary = sorted(employees, key=lambda employee: employee[2])

print("Above 50000:", high_salary)
print("10% Increased:", increased_salary)
print("Sorted:", sorted_salary)


# 51. Take a list of products with names, prices, and quantities, use functions and lambda expressions to: a) Calculate total value of each product. b) Filter products costing more than ₹1,000. c) Sort products according to total value.
products = [("Laptop", 50000, 1),("Mouse", 800, 2),("Keyboard", 1500, 2),("Pen", 50, 5)
]


def product_value(product):
    return product[1] * product[2]


values = list(map(lambda product: (product[0], product_value(product)), products))

costly_products = list(
    filter(lambda product: product_value(product) > 1000, products)
)

sorted_products = sorted(products, key=lambda product: product_value(product))

print("Product Values:", values)
print("Above 1000:", costly_products)
print("Sorted:", sorted_products)


# 52. Write a program using functions, map(), filter(), and lambda expressions to process a list of words and: a) Find the length of every word. b) Extract words having more than five characters. c) Sort words according to their length.
words = ["apple", "banana", "cat", "orange", "computer", "dog"]


def word_lengths(words):
    return list(map(lambda word: len(word), words))


def long_words(words):
    return list(filter(lambda word: len(word) > 5, words))


def sort_by_length(words):
    return sorted(words, key=lambda word: len(word))

print("Lengths:", word_lengths(words))
print("More than 5 characters:", long_words(words))
print("Sorted:", sort_by_length(words))
