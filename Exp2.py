# Distance between two points without using math library

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("Distance between two points =", distance)

# add.py without using sys library

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

sum = a + b

print("Sum =", sum)