
# list data type
# a=[2,3,4,'abc',2.5]
# print(a)
# print(type(a))

# tuple data type

# a=(10,20,304,33,40)

# print(type(a))

# set data type

# a={10,20,30,30,30}

# print(a)

# dictionary data type

# student={"name":"rohit","course":"btech" }


# program 1 : WAP to add two number.input should be taken 
# from user and data type should be of <int,float>

# num1=int(input("enter number 1:"))
# num2=int(input("enter number 2:"))

# num3= num1 + num2
# print(num3)

# Q2.check that a given number is even or odd
# Q3.find largest among two number
# Q4.check that  agiven number is prime or not
# calculate CI and take the value from the user

# a=int(input("enter the number:"))

# if (a%2==0):
#     print("even")
# else:
#     print("odd")

# a=int(input("enter the number1 :"))
# b=int(input("enter the number2:"))

# if (a>b):
#     print("a is greater")
# else:
#     print("b is greater")

# Compound Interest Program

p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time (in years): "))

amount = p * (1 + r/100) ** t
ci = amount - p

print("Compound Interest =", ci)
print("Total Amount =", amount)

# Prime Number Check Program

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a prime number")
else:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")