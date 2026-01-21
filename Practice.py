#  Checking Whether a Given Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Printing Decimal Equivalents of Fractions Using a For Loop
for i in range(2, 11):
    print(f"1/{i} = {1/i}")


# Demonstration of List and Tuple in Python
my_list = [10, 20, 30, 40]
my_tuple = (10, 20, 30, 40)

print("List:", my_list)
print("Tuple:", my_tuple)

# Looping Over a Sequence Using a For Loop
sequence = ["Apple", "Banana", "Cherry"]
for item in sequence:
    print(item)

# Countdown Using a While Loop
n = 10
while n >= 0:
    print(n)
    n -= 1

# Finding the Sum of All Prime Numbers Below Two Million

limit = 2000000
sieve = [True] * limit
sieve[0] = sieve[1] = False

for i in range(2, int(limit**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, limit, i):
            sieve[j] = False

prime_sum = sum(i for i in range(limit) if sieve[i])
print(prime_sum)

# Finding the Sum of Even-Valued Terms in the Fibonacci Sequence
a, b = 1, 2
even_sum = 0

while b <= 4000000:
    if b % 2 == 0:
        even_sum += b
    a, b = b, a + b

print(even_sum)

#Checking Whether a Number is Positive, Negative, or Zero
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Checking Divisibility of a Number by 5 and 11
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")

# Printing Squares of Numbers Using a For Loop
for i in range(1, 11):
    print(f"{i}^2 = {i*i}")


