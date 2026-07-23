#evaluate student performance
marks=float(input("enter marks of student"))

if marks >= 90:
    print("Excellent Performance")
elif marks >=80:
    print("Very Good performance")
elif marks >=70:
    print("Good performance")
elif marks >=60:
    print("Average performance")
else:
    print("poor performace")


#find largest of three number
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

if num1 > num2:
    if num1 > num3:
        print(num1,"is largest")
    else:
         print(num3,"is largest")
else:
    if num2 > num3:
        print(num2,"is largest")
    else:
         print(num3,"is largest")

#find smallest of three number
num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))

if num1 < num2:
    if num1 < num3:
        print(num1,"is smallest")
    else:
         print(num3,"is smallest")
else:
    if num2 < num3:
        print(num2,"is smallest")
    else:
         print(num3,"is smallest")

