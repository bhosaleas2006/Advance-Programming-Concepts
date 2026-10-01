import pandas as pd

# 1. Create a dictionary containing the following information for 5 students: Student ID, Student Name, Python Marks, DBMS Marks, Mathematics Marks. Convert the dictionary into a Pandas DataFrame and display the DataFrame, calculate total marks, calculate average marks, and display students who scored more than 75% average.


data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Adarsh", "Rahul", "Sneha", "Priya", "Amit"],
    "Python": [85, 72, 90, 68, 80],
    "DBMS": [88, 75, 85, 70, 82],
    "Mathematics": [90, 78, 92, 65, 85]
}

df = pd.DataFrame(data)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("DataFrame:")
print(df)

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])

#2.	Create a dictionary containing:employee

emp ={ "Emp id": [101, 102, 103, 104, 105],
       "emp name": ["Adarsh", "Rahul", "Sneha", "Priya", "Amit"],
       "dept":["CSE","ENTC","AI","CS","ME"],
       "salary":[10000,2000,3000,4000,5000],
       "exp":[ 5,3,4,6,7]
    }

df = pd.DataFrame(emp)

print("Saalry greater than 5000 \n")
print(df[df["salary"] > 400])

print("\nAverage Salary:", df["salary"].mean())
print("Highest Salary:", df["salary"].max())

print("\nEmployee with Highest Experience:")
print(df.loc[df["exp"].idxmax()])

#3.	Create a dictionary containing:product_id

data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Mouse"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"],
    "Price": [60000, 30000, 1500, 12000, 800],
    "Quantity": [2, 5, 10, 4, 15]
}

df = pd.DataFrame(data)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("Product DataFrame:")
print(df)

print("\nProduct with Highest Total Sales:")
print(df.loc[df["Total_Amount"].idxmax()])


#4. Create a dictionary containing:Patient ID

data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Rahul", "Sneha", "Amit", "Priya", "Kiran"],
    "Age": [65, 45, 72, 35, 61],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Flu", "Kidney Disease"],
    "Medical_Charges": [55000, 12000, 85000, 8000, 62000]
}

df = pd.DataFrame(data)

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:", df["Medical_Charges"].mean())
print("Maximum Medical Charge:", df["Medical_Charges"].max())

print("\nPatients with Medical Charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])

#5.	Create a dictionary containing:Order_ID
data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Rahul", "Sneha", "Priya", "Kiran"],
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor", "Printer"],
    "Quantity": [1, 2, 3, 2, 1],
    "Price": [60000, 30000, 20000, 12000, 15000],
    "Discount": [5000, 3000, 2000, 1000, 1500]
}
df =pd.DataFrame(data)

amount = df["Quantity"] * df["Price"] - df["Discount"] 
print("All Orders:")
print(df)

print("\nOrders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("\nHighest Value Order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("\nAverage Order Value:", df["Final_Amount"].mean())



# 6. Create a dictionary containing Student_ID, Name, Department, Total_Classes, and Classes_Attended. Create a DataFrame and calculate Attendance Percentage = (Classes_Attended / Total_Classes) × 100. Display students whose attendance is below 75%.
data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Adarsh", "Rahul", "Sneha", "Priya", "Amit"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [85, 70, 92, 65, 78]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("Student Data:")
print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


# 7. A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity. Convert the dictionary into a Pandas DataFrame, add a Total_Sales column, calculate total sales using Price × Quantity, display products with sales greater than 10,000, find the product with maximum sales, and calculate average sales.
data = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [60000, 30000, 1500, 12000, 15000],
    "Quantity": [2, 5, 10, 4, 3]
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Sales DataFrame:")
print(df)

print("\nProducts with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nProduct with Maximum Sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("\nAverage Sales:", df["Total_Sales"].mean())


# 7. Create a Pandas Series using a dictionary where the student names are keys and their marks are values. Display the Series, display marks of a particular student, find maximum and minimum marks, calculate average marks, and display students who scored more than 75.
student_marks = {
    "Adarsh": 85,
    "Rahul": 72,
    "Sneha": 90,
    "Priya": 68,
    "Amit": 82
}

series = pd.Series(student_marks)

print("Student Marks:")
print(series)

print("\nMarks of Adarsh:", series["Adarsh"])
print("Maximum Marks:", series.max())
print("Minimum Marks:", series.min())
print("Average Marks:", series.mean())

print("\nStudents who scored more than 75:")
print(series[series > 75])


# 8. Create a Pandas Series using a dictionary containing employee names and their salaries. Display the Series, find highest salary, lowest salary, average salary, and employees earning more than 50,000.
employee_salaries = {
    "Amit": 60000,
    "Rahul": 45000,
    "Sneha": 75000,
    "Priya": 52000,
    "Kiran": 48000
}

series = pd.Series(employee_salaries)

print("Employee Salaries:")
print(series)

print("\nHighest Salary:", series.max())
print("Lowest Salary:", series.min())
print("Average Salary:", series.mean())

print("\nEmployees earning more than 50000:")
print(series[series > 50000])

# 9. Create a Pandas Series using a dictionary containing product names and prices. Display all products and prices, increase every price by 10%, find the most expensive product, and find products costing more than 1,000.
product_prices = {
    "Laptop": 60000,
    "Mobile": 30000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 12000
}

series = pd.Series(product_prices)

print("Products and Prices:")
print(series)

series = series * 1.10

print("\nPrices after 10% increase:")
print(series)

print("\nMost Expensive Product:")
print(series.idxmax(), ":", series.max())

print("\nProducts costing more than 1000:")
print(series[series > 1000])


#10.	Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values.
patient_ages = {
    "P101": 65,
    "P102": 45,
    "P103": 72,
    "P104": 35,
    "P105": 61
}

series = pd.Series(patient_ages)

print("Patient Ages:")
print(series)

print("\nAverage Age:", series.mean())
print("Oldest Patient:", series.idxmax(), "Age:", series.max())
print("Youngest Patient:", series.idxmin(), "Age:", series.min())

print("\nPatients above 60 years:")
print(series[series > 60])


#11.	Create a Pandas Series using a dictionary containing student names and attendance percentages.

student ={"Adarsh":90, "Rahul":78, "Sneha":67, "Priya":99, "Amit":34}

series = pd.Series(student)
print("Average attendance ",series.mean())
print("Attendance below 75",series[series < 75])
print("Attendance above 90",series[series >90])
print("Highest Attendance",series.max())

# 12. Dataset: students.csv. Columns: Student_ID, Name, Department, Python, DBMS, Maths. Read students.csv using Pandas and display first 5 records, last 5 records, total and average marks of each student, students whose average marks are greater than 75, student with highest average, and average marks for each subject.

df = pd.read_csv("students.csv")

print("First 5 Records:")
print(df.head(5))

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nLast 5 Records:")
print(df.tail(5))

print("\nTotal and Average Marks of Each Student:")
print(df[["Student_ID", "Name", "Total", "Average"]])

print("\nStudents with Average Marks Greater Than 75:")
print(df[df["Average"] > 75][["Student_ID", "Name", "Average"]])

print("\nStudent with Highest Average:")
highest = df["Average"].idxmax()
print(df.loc[highest])

print("\nAverage Marks for Each Subject:")
print("Python:", df["Python"].mean())
print("DBMS:", df["DBMS"].mean())
print("Maths:", df["Maths"].mean())

#13.	Dataset: employees.csv Columns:Employee_ID,Name,Department,Experience,Salary

df = pd.read_csv("employees.csv")

print("Employees from CSE Department:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees with Salary Greater Than ₹50,000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())


#14.	Dataset: patients.csvColumns:Patient_ID,Name,Age,Gender,Disease,Medical_Expense

df = pd.read_csv("patients.csv")

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

print("\nPatient with Highest Medical Expense:")
highest = df["Medical_Expense"].idxmax()
print(df.loc[highest])

print("\nNumber of Patients for Each Disease:")
print(df["Disease"].value_counts())

print("\nPatients with Medical Expense Greater Than ₹50,000:")
print(df[df["Medical_Expense"] > 50000])

#15.	Dataset: weather.csvColumns:Date,City,Temperature,Humidity,Rainfal
df = pd.read_csv("weather.csv")

print("Maximum Temperature:")
print(df["Temperature"].max())

print("\nMinimum Temperature:")
print(df["Temperature"].min())

print("\nAverage Temperature:")
print(df["Temperature"].mean())

print("\nRecords where Temperature is above 35°C:")
print(df[df["Temperature"] > 35])

print("\nCity-wise Average Temperature:")
print(df.groupby("City")["Temperature"].mean())


