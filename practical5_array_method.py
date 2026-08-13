from array import array

a = array('i', [10, 20, 30, 40, 50])

print("Original Array:", a)

print("\n1. Accessing Elements")
print("First element:", a[0])
print("Third element:", a[2])
print("Last element:", a[-1])

print("\n2. Append Element")
a.append(60)
print("After append:", a)

print("\n3. Insert Element")
a.insert(2, 25)
print("After insert:", a)

print("\n4. Remove Element")
a.remove(25)
print("After remove:", a)

print("\nSort Array")
a = array('i', sorted(a))
print("After sorting:", a)

print("\nReverse Array")
a.reverse()
print("After reverse:", a)

print("\nLength of Array")
print("Length:", len(a))

print("\nSearch Element")
n = int(input("Enter element to search: "))

if n in a:
    print("Element found")
else:
    print("Element not found")

print("\nMaximum Element")
print("Maximum:", max(a))

print("\nMinimum Element")
print("Minimum:", min(a))

print("\nSum of Elements")
print("Sum:", sum(a))

print("\nDisplay Elements Using Loop")
for i in a:
    print(i)

print("\nCopy Array")
b = array('i', a)
print("Original Array:", a)
print("Copied Array:", b)

print("\n Slicing Array")
print("First three elements:", a[:3])
print("Elements from index 2:", a[2:])
print("Elements from index 1 to 3:", a[1:4])
print("Every second element:", a[::2])
print("Reverse using slicing:", a[::-1])
