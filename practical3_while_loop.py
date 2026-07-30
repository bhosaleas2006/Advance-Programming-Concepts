'''#Write a PYTHON program to print the natural numbers up to n
n = int(input("Enter Number"))
i=1
while i <= n:
    print(i)
    i +=1
#Write a PYTHON program to print even numbers up to n
n = int(input("Enter Number"))
i=1
while i <= n:
    if i % 2 ==0:
        print(i)
    i +=1
#Write a PYTHON program to print odd numbers up to n
n = int(input("Enter Number"))
i=1
while i <= n:
    if i % 2 != 0:
        print(i)
    i +=1
#Write a PYTHON program to print sum of natural numbers up to n
n = int(input("Enter Number"))
i=1
sum =0
while i <= n:
    sum +=i
    i +=1
print(sum)

#Write a PYTHON program to print sum of odd numbers up to n
n = int(input("Enter Number"))
i=1
sum =0
while i <= n:
    if i % 2 ==0:
        sum +=i
    i +=1
print(sum)

#Write a PYTHON program to print sum of even numbers up to n
n = int(input("Enter Number"))
i=1
sum =0
while i <= n:
    if i % 2 !=0:
        sum +=i
    i +=1
print(sum) 
#Write a PYTHON program to print natural numbers up to n in reverse order.
n = int(input("Enter Number"))
i=1
while n >= 1:
    print(n)
    n -= 1
    
#Write a PYTHON program to print Fibonacci series up to n
n = int(input("Enter Number"))
a,b=0,1
i=1
while i <= n:
    print(a, end=" ")
    a,b = b,a+b
    i+=1

#Write a PYTHON program  find a factorial of given number
n = int(input("Enter Number"))
fact =1
i =1

while i <= n:
    fact *= i
    i +=1
print("factorial is",fact)

#Write a PYTHON program to check the entered number is prime or not
n = int(input("Enter Number"))
i=2
count=0
while i < n :
    if n % i == 0:
        count +=1
    i +=1
if n > 1 and count == 0:
    print("Prime Number")
else:
    print("Not Prime Number")

#Write a PYTHON program to find the sum of digits of given number
num = int(input("Enter Number"))
i =1
s =0
while i <= num:
    rem = num % 10
    s +=rem
    num //=10
print("sum of digits ",s)
'''
#Write a PYTHON program to check the entered  number is palindrome or not
num = int(input("Enter Number"))
rev =0
org=num

while num > 0:
    rem = num % 10
    rev= rev * 10+rem
    num //=10

if org == rev:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")

    
#Write a PYTHON program to reverse the given number.
num = int(input("Enter Number"))
rev =0
while num > 0:
    rem = num % 10
    rev= rev * 10+rem
    num //=10
print("reverse number is ",rev)

#Write a PYTHON program to print the multiplication table
n = int(input("Enter Number to get multiplication table"))
i=1
while i <= 10:
    print( n , "x" , i , "=" ,n* i)
    i +=1

# Write a PYTHON program to print the largest of n numbers
n = int(input("Enter how many numbers: "))
i = 1
num = int(input("Enter number: "))
largest = num
while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i += 1
print("Largest =", largest)

# Write a PYTHON program to print smallest of n numbers
n = int(input("Enter how many numbers: "))
i = 1
num = int(input("Enter number: "))
smallest = num
while i < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i += 1
print("Smallest =", smallest)



