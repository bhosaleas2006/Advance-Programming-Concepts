import pandas as pd

dict ={"Amit":34, "Suresh":78 ,"Rakesh":89 ,"Sujit" : 78 }

print("Adding new element")
dict["Sahil"] = 78
print(dict)

print("Updating the element")
dict["Amit"]=90
print(dict)

print("Remove student from a list")
del dict["Amit"]
print(dict)

s = pd.Series(dict)
"""total =0
print("Calculate average grade of whole class")
for value in dict.values():
    total += value
avg = total / len(dict)"""
avg = s.mean()
print("Average of whole class :",avg)


print("Student with highest grade:")
print( s.idxmax(), ":" ,s.max())

print("Student with lowest grade:")
print( s.idxmin(), ":" ,s.min())
