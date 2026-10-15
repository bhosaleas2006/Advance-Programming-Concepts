
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.title("Simple Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

#scatter Plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]
plt.scatter(x, y)
plt.title("Simple Scatter Plot")
plt.show()

#Bar Plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.bar(x, y)
plt.legend(["bar"])
plt.title("Bar Chart")
plt.show()

plt.barh(x,y)
plt.show()

#PIE CHART
x=[1,2,3,4,5]
e=(0,1,0,0,0)
plt.pie(x,explode=e)
plt.show()

#HISTOGRAM
x=[1,2,3,4,5,6,7]
plt.hist(x,bins=[1,2,3,4,5,6,7])
plt.show()


# 3D plot
import numpy as np
fig = plt.figure()
ax = plt.axes()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
z = [3, 1, 4, 2, 5]

ax.plot(x, y, z)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.title("3D Line Plot")
plt.show()

# First subplot
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Line Plot")

# Second subplot
plt.subplot(1, 2, 2)
plt.bar([1, 2, 3], [10, 20, 30])
plt.title("Bar Chart")

plt.tight_layout()
plt.show()

#Multiple Line Plot
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.title("Multiple Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.show()


#3D Scatter Plot

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
z = [2, 4, 1, 5, 3]

ax.scatter(x, y, z)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

plt.title("3D Scatter Plot")
plt.show()

