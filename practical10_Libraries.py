import numpy as np
#1.	Write a Python program using NumPy to create a one-dimensional array containing 10 integers and display the array, its size, data type, and number of dimensions.

arr =np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.size)
print(arr.ndim)

#2.	Create two NumPy arrays of 5 integers each. Perform and display:
#•	Addition 
#•	Subtraction 
#•	Multiplication 
#•	Division 
#•	Modulus

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + 2)
print(a - 2)      
print(a * b)     
print(a / b)
print( a % b)

#3.	Create a NumPy array containing 10 numbers. Find and display the maximum, minimum, sum, and average of the elements.
arr =np.array([1,2,3,4,5,6,7,8,9,10])
print("Maximum :",np.max(arr))
print("Minimum:",np.min(arr))
print("Sum:",np.sum(arr))
print("Average:",np.mean(arr))

#4.	Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.
arr = np.arange(1,21)
even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]
print("Even Number:",even)
print("Odd Number:",odd)

#5.	Create a one-dimensional array containing numbers from 1 to 12. Reshape it into:
#•	2 × 6 matrix 
#•	3 × 4 matrix 
#•	4 × 3 matrix
arr = np.arange(1,13)
print("2 x 6 matrix:")
print(arr.reshape(2,6))
print("3 x 4 :")
print(arr.reshape(3,4))
print("4 x 3:")
print(arr.reshape(4,3))

#6.	Create two 3 × 3 NumPy matrices and perform matrix addition.
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

result = matrix1 + matrix2

print("Matrix Addition:")
print(result)


#7.	Create two compatible matrices using NumPy and perform matrix multiplication using an appropriate NumPy function.
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

matrix2 = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

result = np.matmul(matrix1, matrix2)

print("Matrix Multiplication:")
print(result)

#8.	Create a 3 × 4 matrix and display its transpose.
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("Original:")
print(matrix)

print("Transpose:")
print(matrix.T)

#9.	Create a 4 × 4 NumPy array and write a program to:
#•	Display the first row 
#•	Display the last column 
#•	Display the diagonal elements 
#	Display the elements from the second and third rows

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("First Row:", matrix[0])
print("Last Column:", matrix[:, -1])
print("Diagonal Elements:", np.diag(matrix))
print("Second and Third Rows:")
print(matrix[1:3])

# 10. Create a 4 × 4 matrix and calculate the sum of each row and each column separately.
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Sum of Each Row:", np.sum(matrix, axis=1))
print("Sum of Each Column:", np.sum(matrix, axis=0))

# 11. Create a NumPy array containing numbers from 1 to 20. Using slicing, display the first 5 elements, last 5 elements, alternate elements, and elements in reverse order.
arr = np.arange(1, 21)

print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[-5:])
print("Alternate Elements:", arr[::2])
print("Reverse Order:", arr[::-1])

# 12. Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
arr = np.array([10, 65, 30, 80, 45, 90, 25, 55, 40, 75])

arr[arr > 50] = 0

print("Modified Array:", arr)

# 13. Create an unsorted NumPy array and display it in ascending order and descending order.
arr = np.array([45, 12, 78, 3, 56, 23, 89, 10])

ascending = np.sort(arr)
descending = np.sort(arr)[::-1]

print("Ascending Order:", ascending)
print("Descending Order:", descending)

# 14. Create an array containing duplicate values. Find and display only the unique elements.
arr = np.array([10, 20, 10, 30, 40, 20, 50, 30, 60, 40])

unique = np.unique(arr)

print("Unique Elements:", unique)

#15.	Create two NumPy arrays and concatenate them horizontally and vertically.
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[11,22],[33,44]])

print("Horizontal Concatenation")
print(np.hstack((arr1,arr2)))
print("Vertical Concatenation:")
print(np.vstack((arr1, arr2)))

#16.	Store marks of 10 students in a NumPy array. Calculate:
#•	Highest marks 
#•	Lowest marks 
#•	Average marks 
#•	Median 
#•	Standard deviation
marks = np.array([85, 72, 90, 68, 95, 78, 88, 76, 92, 81])

print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))

# 17. Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.
marks = np.array([
    65, 78, 82, 90, 55,
    72, 88, 95, 60, 75,
    85, 92, 68, 80, 70,
    58, 96, 87, 73, 84
])

average = np.mean(marks)
above_average = marks[marks > average]

print("Class Average:", average)
print("Marks Above Average:", above_average)

# 18. Write a Python program using NumPy to create a 3D array of shape (2, 3, 4) containing numbers from 1 to 24. Display the array and its number of dimensions, shape, and size.
arr = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:")
print(arr)
print("Number of Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# 19. Create a 3D array of shape (2, 3, 4) and write a program to access the first element, last element, element at index [0,1,2], and element at index [1,2,3].
arr = np.arange(1, 25).reshape(2, 3, 4)

print("First Element:", arr[0, 0, 0])
print("Last Element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])


# 20. Create a (2, 3, 4) array and calculate the sum of all elements, sum of each layer, sum along rows, and sum along columns.
arr = np.arange(1, 25).reshape(2, 3, 4)

print("Sum of All Elements:", np.sum(arr))
print("Sum of Each Layer:", np.sum(arr, axis=(1, 2)))
print("Sum Along Rows:", np.sum(arr, axis=2))
print("Sum Along Columns:", np.sum(arr, axis=1))

# 21. Create a 3D array of random integers between 1 and 100. Replace all values greater than 50 with 0.
arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original Array:")
print(arr)

arr[arr > 50] = 0

print("Modified Array:")
print(arr)


# 22. Generate a random 3D array of shape (3, 4, 5) and calculate its mean, median, standard deviation, variance, minimum, and maximum.
arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 23. Create a 3D NumPy array of shape (2, 3, 4) containing numbers from 1 to 24. Flatten the array into a one-dimensional array and display both the original and flattened arrays.
arr = np.arange(1, 25).reshape(2, 3, 4)
flattened = arr.flatten()

print("Original 3D Array:")
print(arr)

print("Flattened Array:")
print(flattened)


# 24. Create a 3D array containing integers from 1 to 27. Flatten the array and calculate sum, average, maximum, and minimum.
arr = np.arange(1, 28).reshape(3, 3, 3)
flat = arr.flatten()

print("Flattened Array:", flat)
print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))


# 25. Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are greater than 50, even numbers, and less than the average value.
arr = np.random.randint(1, 101, size=(3, 4, 5))
flattened = arr.flatten()
average = np.mean(flattened)

print("Original 3D Array:")
print(arr)

print("Elements Greater Than 50:")
print(flattened[flattened > 50])

print("Even Numbers:")
print(flattened[flattened % 2 == 0])

print("Average:", average)

print("Elements Less Than Average:")
print(flattened[flattened < average])

