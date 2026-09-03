
# 1. Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.

name = input("Enter student name: ")
roll = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Roll Number: " + roll + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("Semester: " + semester + "\n")

print("Student information written successfully.")


# 2. Write a program to open a text file and display its complete contents.

with open("student.txt", "r") as file:
    content = file.read()

print(content)


# 3. Write a program to append additional student information to an existing file without deleting its previous contents.

name = input("Enter student name: ")
roll = input("Enter roll number: ")

with open("student.txt", "a") as file:
    file.write("\nName: " + name + "\n")
    file.write("Roll Number: " + roll + "\n")

print("Information appended successfully.")


# 4. Write a program to read a text file line by line and display each line separately.

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


# 5. Write a program to count and display the total number of lines present in a text file.

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))


# 6. Write a program to count the total number of words present in a text file.

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

print("Total number of words:", len(words))


# 7. Write a program to count the total number of characters in a text file, including spaces.

with open("student.txt", "r") as file:
    content = file.read()

print("Total number of characters:", len(content))


# 8. Write a program to read a text file and display its lines in reverse order.

with open("student.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())


# 9. Read a text file and count the number of vowels and consonants present in the file.

with open("student.txt", "r") as file:
    content = file.read()

vowels = 0
consonants = 0

for ch in content.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

#10.Read a text file and calculate the number of alphabets, digits, spaces, and special characters.
with open("student.txt", "r") as file:
    content = file.read()

alpha =0
digit = 0
space =0
special =0

for ch in content.lower():
    if ch.isalpha():
        alpha += 1
    elif ch.isdigit():
        digit += 1
    elif ch == " ":
        space +=1
    elif special == "\n":
        special +=1
print("the number of alphabets:",alpha)
print("the number of digits:",digit)
print("the number of spaces:",space)
print("the number of specuial characters:",special)

#11.	Read a text file and find the longest word present in the file.

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("File is empty.")


# 12.  Read a text file and count how many times each word occurs. Display the result using a dictionary.

with open("student.txt", "r") as file:
    content = file.read().lower()

words = content.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

#13.	Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
search_word = input("Enter word to search: ")

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        words = line.split()

        for word in words:
            if word.lower() == search_word.lower():
                count += 1
                if line_number not in line_numbers:
                    line_numbers.append(line_number)

print("Number of occurrences:", count)
print("Line numbers:", line_numbers)

#14.	Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open("student.txt", "w") as file:
    file.write(content)

print("Word replaced successfully.")


# 15. Read a Python source file and create another file after removing single-line comments.

source_file = input("Enter Python source file name: ")
output_file = input("Enter output file name: ")

with open(source_file, "r") as source:
    with open(output_file, "w") as output:
        for line in source:
            if not line.strip().startswith("#"):
                output.write(line)

print("Comments removed successfully.")


# 16. Read a text file and create another file containing the same text in uppercase.

source_file = input("Enter source file name: ")
output_file = input("Enter output file name: ")

with open(source_file, "r") as source:
    content = source.read()

with open(output_file, "w") as output:
    output.write(content.upper())

print("Uppercase file created successfully.")


# 17. Create a file containing student records in the format: RollNo,Name,Marks. Write a program to display all records, find the student with the highest marks, calculate average marks, and display students who scored more than 80.

filename = "students.csv"

with open(filename, "w") as file:
    file.write("RollNo,Name,Marks\n")
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

students = []

with open(filename, "r") as file:
    next(file)

    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((roll, name, int(marks)))

print("All records:")

for student in students:
    print(student)

highest = max(students, key=lambda x: x[2])

print("Student with highest marks:", highest)

average = sum(student[2] for student in students) / len(students)

print("Average marks:", average)

print("Students who scored more than 80:")

for student in students:
    if student[2] > 80:
        print(student)


# 18. Store employee ID, name, department, and salary in a file. Write functions to display all employees, find the highest-paid employee, calculate average salary, and display employees earning above a given salary.

filename = "employees.txt"

with open(filename, "w") as file:
    file.write("1,Amit,IT,50000\n")
    file.write("2,Priya,HR,60000\n")
    file.write("3,Rahul,Finance,75000\n")

employees = []

with open(filename, "r") as file:
    for line in file:
        emp_id, name, department, salary = line.strip().split(",")
        employees.append((emp_id, name, department, float(salary)))

print("All employees:")

for employee in employees:
    print(employee)

highest = max(employees, key=lambda x: x[3])

print("Highest-paid employee:", highest)

average = sum(employee[3] for employee in employees) / len(employees)

print("Average salary:", average)

salary = float(input("Enter salary: "))

print("Employees earning above given salary:")

for employee in employees:
    if employee[3] > salary:
        print(employee)


# 19. Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.

filename = "attendance.txt"

with open(filename, "w") as file:
    file.write("101,Amit,70,90\n")
    file.write("102,Priya,80,90\n")
    file.write("103,Rahul,60,90\n")

with open(filename, "r") as file:
    for line in file:
        roll, name, present, total = line.strip().split(",")

        present = int(present)
        total = int(total)

        percentage = (present / total) * 100

        print(name, "Attendance:", percentage, "%")

        if percentage < 75:
            print("Below 75%:", name)


# 20. Store deposits and withdrawals in a file. Read the file and calculate total deposits, total withdrawals, final balance, and largest transaction.

filename = "transactions.txt"

with open(filename, "w") as file:
    file.write("deposit,5000\n")
    file.write("withdrawal,1000\n")
    file.write("deposit,3000\n")
    file.write("withdrawal,500\n")

total_deposits = 0
total_withdrawals = 0
transactions = []

with open(filename, "r") as file:
    for line in file:
        transaction_type, amount = line.strip().split(",")

        amount = float(amount)
        transactions.append(amount)

        if transaction_type == "deposit":
            total_deposits += amount
        elif transaction_type == "withdrawal":
            total_withdrawals += amount

final_balance = total_deposits - total_withdrawals
largest_transaction = max(transactions)

print("Total deposits:", total_deposits)
print("Total withdrawals:", total_withdrawals)
print("Final balance:", final_balance)
print("Largest transaction:", largest_transaction)


# 21. Maintain book records containing book ID, title, author, and availability status. Implement operations to add a book, search for a book, issue a book, return a book, and display available books.

books = [
    {
        "id": "101",
        "title": "Python Programming",
        "author": "John",
        "available": True
    },
    {
        "id": "102",
        "title": "Data Structures",
        "author": "Robert",
        "available": True
    }
]

while True:
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter book ID: ")
        title = input("Enter title: ")
        author = input("Enter author: ")

        books.append({
            "id": book_id,
            "title": title,
            "author": author,
            "available": True
        })

        print("Book added successfully.")

    elif choice == "2":
        book_id = input("Enter book ID: ")

        found = False

        for book in books:
            if book["id"] == book_id:
                print(book)
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "3":
        book_id = input("Enter book ID: ")

        found = False

        for book in books:
            if book["id"] == book_id:
                found = True

                if book["available"]:
                    book["available"] = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")

                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Enter book ID: ")

        found = False

        for book in books:
            if book["id"] == book_id:
                book["available"] = True
                print("Book returned successfully.")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "5":
        print("Available Books:")

        for book in books:
            if book["available"]:
                print(book)

    elif choice == "6":
        break

    else:
        print("Invalid choice.")


# 22. Read the contents of two text files and create a third file containing the contents of both files.

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
file3 = input("Enter third file name: ")

with open(file1, "r") as f1:
    content1 = f1.read()

with open(file2, "r") as f2:
    content2 = f2.read()

with open(file3, "w") as f3:
    f3.write(content1)
    f3.write("\n")
    f3.write(content2)

print("Files combined successfully.")


# 23. Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.

file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")

with open(file1, "r") as f1:
    lines1 = f1.readlines()

with open(file2, "r") as f2:
    lines2 = f2.readlines()

if lines1 == lines2:
    print("Both files are identical.")
else:
    print("Files are different.")

    minimum = min(len(lines1), len(lines2))

    for i in range(minimum):
        if lines1[i] != lines2[i]:
            print("First difference is at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            break
    else:
        print("One file contains more lines than the other.")


                                         
