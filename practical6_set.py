#1.	Write a Python program to create a set containing five integers and display all its elements.
numbers = {10, 20, 30, 40, 50}

print("Set of integers:", numbers)


#2. Create a list containing duplicate values.
# Convert the list into a set and display the resulting set.
values = [10, 20, 10, 30, 20, 40, 50]

unique_values = set(values)

print("\nSet after removing duplicates:", unique_values)


print("\nSet after removing duplicates:", s)

#3. Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
set ={"Apple","Orange","Jackfruit","Mango"}
set.add("Banana")
set.add("Watermelon")
print(set)

#4.	Create a set of numbers and remove a specified number from the set.
set ={1,2,3,4,5}
print(set)
set.remove(2)
print(set)

#5.	Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
set ={"Ramesh","Mukesh","Rakesh","Suresh"}
name = input("Enter student name to check")
if name in set:
    print(name,"Present in set")
else:
    print(name,"Not present in set")

#6.6.	Create a set of cities and determine the total number of cities using an appropriate function.
city ={"Pune","Satara","Kolhapur","Sangali"}
print("total number of cities",len(set))

#7.	Create a set of programming languages and display each language using a for loop.
lan={"Python","CPP","C","Java"}
for i in lan:
    print(i)

#8.	Create a list containing duplicate numbers, use a set to remove the duplicates.
list =[1,2,3,2,4,3,5,6,1]
print(list)
set = set(list)
print("Affter removing duplicate numbers",set)

#9.	Create two sets of integers and find their union.
s1 ={1,2,3,4,5}
s2 ={3,4,5,6,7}
print("Union :",s1.union(s2) )

#10.	Create two sets and find the elements common to both sets.
s1 ={1,2,3,4,5}
s2 ={3,4,5,6,7}
print("Commen Elements :",s1.intersection(s2) )

#11.	Create two sets and find:
#	Elements present in the first set but not the second 
#	Elements present in the second set but not the first
s1 ={1,2,3,4,5}
s2 ={3,4,5,6,7}
print("Elements present in the first set",s1.difference(s2))
print("Elements present in the second set",s2.difference(s1))

#12.	Create two sets of numbers and find the elements that are present in either set but not in both.
s1 ={1,2,3,4,5}
s2 ={3,4,5,6,7}
print("elements that are present in either set but not in both",s1.symmetric_difference(s2))

#13.	Create two sets and determine whether the first set is a subset of the second set.
print("subset",s1.issubset(s2))

#14.	Create two sets and determine whether the first set is a superset of the second set.
print("subset",s1.issuperset(s2))

#15.	Write a program to determine whether two sets have no elements in common.
set3= {1, 2, 3}
set4= {4, 5, 6}

if set3.isdisjoint(set4):
    print("\nThe sets have no common elements")
else:
    print("\nThe sets have common elements")

#16.	Create two sets and check whether they are equal.
s5={1,2,3}
s6={3,2,1}
if s5 == s6:
    print("equal")
else:
    print("not equal")

#17.	Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.

student1 = {"Math", "Physics", "Python", "English"}
student2 = {"Python", "Chemistry", "Physics", "Biology"}

print("\nSubjects studied by both students:")
print(student1.intersection(student2))

#18.	Accept a sentence from the user and use a set to display all unique words.
sentence = input("\nEnter a sentence: ")

words = sentence.split()

unique_words = set(words)

print(unique_words)

# Create two sets:
# Students present in the morning session
# Students present in the afternoon session
# Find different groups of students.
morning = {"Amit", "Rahul", "Priya", "Neha"}
afternoon = {"Rahul", "Neha", "Sneha", "Rohan"}

print("\nStudents present in both sessions:")
print(morning.intersection(afternoon))

print("Students present only in the morning:")
print(morning.difference(afternoon))

print("Students present only in the afternoon:")
print(afternoon.difference(morning))

print("Students present in at least one session:")
print(morning.union(afternoon))

#20.	Create sets representing students enrolled in:
python_students = {"Amit", "Rahul", "Neha", "Priya"}
java_students = {"Rahul", "Sneha", "Priya", "Rohan"}

#21. Find students enrolled in both courses and students enrolled in only one course.
print("\nStudents enrolled in both courses:")
print(python_students.intersection(java_students))

print("Students enrolled in only one course:")
print(python_students.symmetric_difference(java_students))


#22.	Create two sets representing technical skills of two employees. Find:
#•	Common skills 
#•	Skills unique to Employee 1 
#•	Skills unique to Employee 2 
#•	All available skills

e1 = {"Python", "Java", "SQL", "HTML"}
e2 = {"Python", "C++", "SQL", "JavaScript"}

print("\nCommon skills:")
print(employee1.intersection(employee2))

print("Skills unique to Employee 1:")
print(employee1.difference(employee2))

print("Skills unique to Employee 2:")
print(employee2.difference(employee1))

print("All available skills:")
print(employee1.union(employee2))


#23.	Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Python", "Java", "C", "DBMS"}
requested_books = {"Python", "C++", "DBMS"}

print("\nRequested books that are available:")
print(available_books.intersection(requested_books))


# 24.	Store visitor IDs from two different days in separate sets. Determine:
day1 = {101, 102, 103, 104, 105}
day2 = {104, 105, 106, 107, 108}

print("\nUnique visitors across both days:")
print(day1.union(day2))

print("Returning visitors:")
print(day1.intersection(day2))

print("Visitors who came only on the first day:")
print(day1.difference(day2))

print("Visitors who came only on the second day:")
print(day2.difference(day1))


#	Represent the friends of two users using sets. Find:
category1 = {"Laptop", "Mouse", "Keyboard", "Printer"}
category2 = {"Keyboard", "Printer", "Scanner", "Monitor"}

print("\nProducts belonging to both categories:")
print(category1.intersection(category2))


#25.	Represent the friends of two users using sets. Find:
user1 = {"Amit", "Rahul", "Neha", "Priya"}
user2 = {"Rahul", "Priya", "Sneha", "Rohan"}

print("\nMutual friends:")
print(user1.intersection(user2))

print("Friends unique to User 1:")
print(user1.difference(user2))

print("Friends unique to User 2:")
print(user2.difference(user1))

print("Total unique friends:")
print(user1.union(user2))
