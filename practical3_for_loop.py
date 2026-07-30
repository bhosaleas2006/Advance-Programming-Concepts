# 1 Write a PYTHON program to print the natural numbers up to n
n=int(input("enter number"))
for i in range(1,n+1):
    print(i)

# 2 Write a PYTHON program to print even numbers up to n
n=int(input("enter number"))
for i in range(1,n+1):
    if i % 2 == 0:
        print(i)

# 3 Write a PYTHON program to print odd numbers up to n
n=int(input("enter number"))
for i in range(1,n+1):
    if i % 2 != 0:
       print(i)

#4 Write a PYTHON program that prints  1 2 4 8 16 32 … n2
n=int(input("enter number"))
for i in range(1,n+1):
    print( i * i)

# 5Write a PYTHON program to sum the given sequence
#1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!
n = int(input("Enter number: "))
fact = 1
s = 1
for i in range(1, n + 1):
    fact *= i
    s += 1 / fact
print("Sum =", s)


# 6 Write a PYTHON program to compute the cosine series
x = float(input("Enter x: "))
n = int(input("Enter n: "))
sum = 1
fact = 1
sign = -1
for i in range(2, n + 1, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum += sign * (x ** i) / fact
    sign *= -1
print("Cosine Series =", sum)


# 7 Write a short PYTHON program to check whether the square root of number is prime or not
n = int(input("Enter number "))
root = int(n ** 0.5)
count = 0
for i in range(2, root):
    if root % i == 0:
        count += 1
if root > 1 and count == 0:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")

#8.Write a PYTHON program to produce following design
			#A B C 
			#A B C 
			#A B C 

for j in range(1,4):
    for i in range(65,68):
        print(chr(i), end = " " )
    print()


'''9.  Write a PYTHON program to produce following design
      A
      A B
      A B C
      A B C D 
      A B C D E
      If user enters n value as 5
'''
n = int(input("Enter number "))
for i in range(1,n+1):
    for j in range(65,65+i):
        print(chr(j), end = " " )
    print()
'''
10. Write a PYTHON program to produce following design
       A B C D E
       A B C D
       A B C
       A B
       A                      
      (If user enters n value as 5)

'''

n = int(input("Enter number "))
for i in range(n,0,-1):
    for j in range(65,65+i):
        print(chr(j), end = " " )
    print()

'''
11. Write a PYTHON program to produce following  
      design
      1
      1 2
      1 2 3
      1 2 3 4
      1 2 3 4 5
      If user enters n value as 5
'''
n = int(input("Enter number "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print( j , end = " " )
    print()

'''
12. Write a PYTHON program to produce following design
      1
      2 2
      3 3 3
      4 4 4 4 
      5 5 5 5 5
      If user enters n value as 5
'''
n = int(input("Enter number "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print( i , end = " " )
    print()
