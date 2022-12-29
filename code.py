import matplotlib.pyplot as plt
print('\n\n 	Welcome to graphing program!! \n ') 

title = input('Enter the title of graph you want to make: \n')
plt.title(title)

x_name =input("Enter the name of X axis : \n")
y_name =input("Enter the name of Y axis : \n")
plt.xlabel(x_name)
plt.ylabel(y_name)

n = int(input("Enter number of elements  : \n"))

xval = []
yval = []
# adding points
print("\n Values of"+x_name)
for i in range(0, n):
	ele1 = float(input())
	xval.append(ele1) 
	

print("\n Values of"+y_name)
for i in range(0, n):
	ele2 = float(input())
	yval.append(ele2) 
	

plt.plot(xval, yval)
plt.show()
