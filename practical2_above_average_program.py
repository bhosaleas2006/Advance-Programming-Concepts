#check number is even or odd
num = int(input("enter number"))
if num % 2 == 0:
    print(num,"is even number")
else:
    print(num,"is odd number")

#check year leap or not
year = int(input("enter year"))
if num % 4 == 0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")

#company insurance to its drivers

marital_status = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if marital_status.lower() == "married":
         print("The driver is insured.")
elif marital_status.lower() == "unmarried":
    
    if gender.lower() == "male" and age > 30:
             print("The driver is insured.")
    elif gender.lower() == "female" and age > 25:
            print("The driver is insured.")
    else:
     print("The driver is not insured.")

else:
     print("Wrong Choice")
  



