Python 3.15.0b4 (tags/v3.15.0b4:0a6fa62, Jul 18 2026, 08:28:49) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
integer = 10
type(integer)
<class 'int'>
floating = 20.5
type(floating)
<class 'float'>
complex_num = 3 + 4j
type(complex_num)
<class 'complex'>
boolean = True
type(boolean)
<class 'bool'>
str = "Python"
type(str)
<class 'str'>
fruits = ("Apple", "Banana", "Mango")
type(fruits)
<class 'tuple'>
colors = {"Red", "Green", "Blue"}
type(colors)
<class 'set'>
student = {
    "Name": "John",
    "Age": 21,
    "Marks": 85
}

type(student)
<class 'dict'>
numbers = [10, 20, 30]
type(numbers)
<class 'list'>
nothing = None
type(nothing)
<class 'NoneType'>
byte=bytearray(5)
byte
bytearray(b'\x00\x00\x00\x00\x00')
type(byte)
<class 'bytearray'>
b = b"Hello"
b
b'Hello'
type(b)
<class 'bytes'>
m = memoryview(5)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    m = memoryview(5)
TypeError: memoryview: a bytes-like object is required, not 'int'
m = memoryviewbytes(5)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    m = memoryviewbytes(5)
NameError: name 'memoryviewbytes' is not defined
a = 15

b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
SyntaxError: multiple statements found while compiling a single statement
print("Addition:", a + b)
Addition: 19
a - b
11
a * b
60
a/b
3.75
a // b
3
a % b
3
a ** b
50625

a == b
False
a != b
True
a > b
True
a< b
False
a >= b
True
x =10
x +=5
x
15
x /= 2
x
7.5
p = True
q = False
p and q
False
p or q
True
not p
False
m=5
>>> n =3
>>> m & n
1
>>> m | n
7
>>> m ^ n
6
>>> ~m
-6
>>> m << 1
10

>>> m >> 1
2
>>> list = [1,2,3,4,5]
>>> 4 in list
True
>>> 4 not in list
False
>>> 8 not in list
True
>>> 9 in list
False
>>> l1=[1,2,3]
>>> l2=[1,2,3]
>>> l1 is l2
False
>>> l2 = l1
>>> l1 is l2
True
>>> list = [12,34,56,87,21]
>>> list
[12, 34, 56, 87, 21]
>>> list.append(78)
>>> list
[12, 34, 56, 87, 21, 78]
>>> list.insert(4,90)
>>> list
[12, 34, 56, 87, 90, 21, 78]
>>> list.extend([32,65])
>>> list
[12, 34, 56, 87, 90, 21, 78, 32, 65]
>>> list.remove(56)
>>> list
[12, 34, 87, 90, 21, 78, 32, 65]
>>> list.pop()
65
>>> list
[12, 34, 87, 90, 21, 78, 32]
