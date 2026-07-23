#Area of square
length =int(input("Enter length of square"))
area = length * length
print("Area of square is",area)

#Area of triangle
base =float(input("Enter base of triangle"))
height = float(input("Enter height of traingle"))
area = 0.5 *  base * height
print("Area of triangle is",area)

#Volume of sphere
import math
radius=int(input("Radius of sphere"))
volume= 4/3 * math.pi * radius**3
print("Volume of sphere",volume)

#surface area of cylinder
radius=int(input("enter radius of sphere"))
height = float(input("Enter height of sphere"))

lateral_area = 2 * math.pi * radius * height
total_area =2 * math.pi * radius * (radius + height)
print("Lateral Area ",lateral_area)
print("Total Area ",total_area)


#calculate factorial of a number
num = int(input("Enter number to calculate factorial"))
fact=1
for i in range(1,num+1):
    fact *= i
print("factorial of number",fact)

# number is palindrom or not
num = int(input("Enter number"))
org=num
rev =0
while num > 0:
    rem =num % 10
    rev = (rev * 10) + rem 
    num //=10

if org == rev:
    print("number is palindrome")
else:
    print("nnumber is not palindrome")

#check number is prime or not
import math
isprime= True
num = int(input("Enter number"))
if num < 2:
    isprime = False
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i== 0:
            isprime=False
            break
if isprime :
    print("Prime  number")
else:
    print("not prime")

#convert kilometers into miles
kilometer= int(input("Enter value in kilometer"))
miles = kilometer * 0.621371
print(miles)

#convert pounds into kilgrams
pounds= int(input("Enter value in pounds"))
kilograms = pounds * 0.45359237
print(kilograms)

# --- GET INPUTS ---
dec_str = input("Enter a positive decimal number: ")
char = input("Enter a single character: ")
decimal_num = int(dec_str)

# Binary 
temp = decimal_num
binary_str = ""
if temp == 0:
    binary_str = "0"
while temp > 0:
    remainder = temp % 2
    binary_str = str(remainder) + binary_str
    temp = temp // 2

# Octal
temp = decimal_num
octal_str = ""
if temp == 0:
    octal_str = "0"
while temp > 0:
    remainder = temp % 8
    octal_str = str(remainder) + octal_str
    temp = temp // 8

# Hexadecimal 
temp = decimal_num
hex_str = ""
hex_chars = "0123456789ABCDEF"
if temp == 0:
    hex_str = "0"
while temp > 0:
    remainder = temp % 16
    hex_str = hex_chars[remainder] + hex_str
    temp = temp // 16

print("\n--- Results for Number " ,decimal_num ,"\n")
print("Binary:     ", binary_str)
print("Octal:      ", octal_str)
print("Hexadecimal:", hex_str)

#CALCULATE FACTORS
factors = []
for i in range(1, decimal_num + 1):
    if decimal_num % i == 0:
        factors.append(i)
print("Factors:    ", factors)

#ASCII Value 
ascii_value = list(char.encode('ascii'))
print("\n--- Results for Character '" + char + "' ---")
print("ASCII Value:", ascii_value)

