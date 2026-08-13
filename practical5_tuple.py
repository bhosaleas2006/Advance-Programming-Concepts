
#Write a Python program to create a tuple of five integers and display it.
tuple =(1,2,3,4,5)
print(tuple)

#Create a tuple containing five city names. Display:
#First city 
#Last city 
#Third city

city =("Kolhapur","Satara","Sangali","Pune","Sindhudurga")

print("First City",city[0])
print("Last City",city[-1])
print("Third City",city[2])

#Create a tuple of student names and display the total number of students using the len() function.
stud=("Ramesh","Ganesh","Sursh","Raakesh")
print("Length of student ",len(stud))


#4.	Create a tuple of colors. Check whether a given color exists in the tuple
color =("Red","Pink","Yellow","Green")
if "Red" in color:
    print("Color is present")
else:
    print("Color is not present")

#5.	Create a tuple of fruits and display each fruit using a loop.
fruits=("Mango","Apple","Banana","Orange")
print("Fruits : \n")
for i in fruits:
    print(i)

#6.Create a tuple with repeated numbers and count how many times a particular number appears.
tuple =(1,2,3,4,5,2,2)
print(tuple.count(2),"number of times 2 appeared")

#Create a tuple of employee IDs and find the index of a given ID.
tuple = (123,122,3545,3446 )
print( "index of id 123 is ",tuple.index(123))

#Create two tuples of numbers and concatenate them into a single tuple.
tuple1 =(1,2,3,4,5,2,2)
tuple2 = (123,122,3545,3446 )
tuple3 = tuple1 + tuple2
print("Concatenated tuple is :",tuple3)

#Create a tuple containing three elements and repeat it four times.
city =("Kolhapur","Satara","Sangali","Pune","Sindhudurga")
multipletime = city * 4
print("City Multipletimes",multipletime)

#10.	Create a tuple of 10 numbers and display: First five elements Last five elements Middle four elements Alternate elements 	Reverse tuple

t =(1,2,3,4,5,6,7,8,9,10)
print("First Five elements",t[:5])
print("Last Five elements",t[-5:])
print("Middle elements",t[3:7])
print("Alternate elements",t[::2])
print("Reverse the numbers",t[::-1])

#Convert a tuple into a list and add a new element.
t =(1,2,3,4,5)
l = list(t)
l.append(6)
print("List after append",l)

#Accept five numbers from the user, store them in a list, and convert the list into a tuple.
list =[]
for i in range(5):
    list.append(int(input("Enter number")))

tuple = tuple(list)
print("Tuple after appending data into list",tuple)

#Modify a tuple by converting it into a list and then back into a tuple.
t =(1,2,3,4,5)
l =list(t)
l[2]=10
t = tuple(l)
print("Tuple after modification",t)


#Create a tuple and delete it completely.
t =(1,2,3,4,5)
print(t)
del t
print(t)

#Create a nested tuple containing student details and display each record.
student_details = (
    (1, "Amit", 85),
    (2, "Rahul", 90),
    (3, "Priya", 88)
)

print("\nStudent records:")

for student in student_details:
    print(student)

#Store ten numbers in a tuple and calculate their sum.

t =(1,2,3,4,5,6,7,8,9,10)
sum =0
for i in t:
    sum +=i
print("Sum of ten elements",sum)

#Find the largest and smallest number in a tuple without using max() and min().
t =(1,2,3,4,5,6,7,8,9,10)

largest = t[0]
smallest =t[0]

for i in t:

    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("largest element ",largest)
print("Smallest element ",smallest)

#Calculate the average of elements stored in a tuple.
t =(1,2,3,4,5,6,7,8,9)
avg = sum(t) // len(t)
print("Average of elements :",avg)

#Store 15 integers in a tuple and count:
#Even numbers 
#Odd numbers

t =(1,2,3,4,5,6,7,8,9,10)
e=0
o =0
for i in t:
    if i % 2 == 0:
        e +=1
    else:
        o +=1
print("Count of even nnumbers is ",e)
print("Count of odd nnumbers is ",o)

#Accept a number from the user and determine whether it exists in the tuple.
t =(1,2,3,4,5,6,7,8,9)
n = int(input("Enter Number"))
if n in t:
    print("Number Present")
else:
    print("Number not Present")

#Store student details in a tuple:
stud=(1,"Rahul","CSE",99)
print("Student roll number",stud[0])
print("Student Name",stud[1])
print("Student Department",stud[2])
print("Student Marks :",stud[3])

#22.Create tuples containing:
#•	Employee ID
#•	Name 
#•	Salary 
#Display all employee information.

employee = (101, "Amit", 50000)

print("\nEmployee information:")
print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Salary:", employee[2])

#23.	Store item prices in a tuple and calculate:
#•	Total bill 
#•	Average price 
#	Highest-priced item 
#	Lowest-priced item

t = ( 20,30,40,50,60)
print("Total bill ",sum(t))
print("Average price", sum(t) / len(t) )
print("Highest-priced item",max(t) )
print("Lowest-priced item", min(t) )

# Store temperatures of seven days in a tuple and determine:
# Maximum temperature
# Minimum temperature
# Average temperature
temperatures = (30, 32, 29, 35, 31, 28, 33)

print("\nMaximum temperature:", max(temperatures))
print("Minimum temperature:", min(temperatures))
print("Average temperature:", sum(temperatures) / len(temperatures))

# Store runs scored in 10 matches and calculate:
# Total runs
# Highest score
# Lowest score
# Average score
runs = (45, 60, 30, 80, 55, 70, 40, 90, 65, 50)

print("\nTotal runs:", sum(runs))
print("Highest score:", max(runs))
print("Lowest score:", min(runs))
print("Average score:", sum(runs) / len(runs))

#Create two tuples and find the common elements between them.
t1 =(1,2,3,4,5)
t2 =(2,4,6,8,9)
common=()
for i in t1:
    if i in t2:
        common +=(i,)

print("Common elements are",common)
        
# Merge two tuples and remove duplicate elements.
merged_tuple = tuple_a + tuple_b

unique_tuple = tuple(set(merged_tuple))

print("\nTuple after removing duplicates:", unique_tuple)

# Count the frequency of each element in a tuple.
frequency_tuple = (1, 2, 1, 3, 2, 4, 1)

print("\nFrequency of each element:")

for item in set(frequency_tuple):
    print(item, ":", frequency_tuple.count(item))

# Convert a tuple into a sorted tuple in ascending and descending order.
sort_tuple = (8, 2, 5, 1, 9, 4)

ascending = tuple(sorted(sort_tuple))
descending = tuple(sorted(sort_tuple, reverse=True))

print("\nAscending order:", ascending)
print("Descending order:", descending)

# Create a tuple containing patient records:
# Patient ID
# Name
# Age
# Blood Group
# Perform the following operations:
# Display all records
# Search for a patient by ID
# Count the total number of patients
# Display patients with a specific blood group
patients = (
    (101, "Amit", 25, "A+"),
    (102, "Rahul", 30, "B+"),
    (103, "Priya", 28, "A+")
)

print("\nPatient records:")

for patient in patients:
    print(patient)

patient_id = int(input("\nEnter patient ID: "))

for patient in patients:
    if patient[0] == patient_id:
        print("Patient found:", patient)

print("Total number of patients:", len(patients))

blood_group = input("Enter blood group: ")

print("Patients with the same blood group:")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)

