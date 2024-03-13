# Python program to add two numbers
num1=float(input("First Number: "))
num2=float(input("Second Number: "))
ans=num1+num2
print(f"Answer is {ans}")

# Maximum of two numbers in Python
numm1=float(input("First Number: "))
numm2=float(input("Second Number: "))
print(max(numm1,numm2))

# Python Program for factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

no = int(input("Enter a number: "))
result = factorial(no)
print(f"Factorial of {no} is {result}")

# Python Program for simple interest
principle=float(input("Enter Principle Amount: "))
rate=float(input("Enter Rate of interest: "))
time=float(input("Enter Time: "))
Simple_interest=(principle*rate*time)/100
print(f"Simple Interest is {Simple_interest}")


# Python Program for compound interest
p=float(input("Enter Principle Amount: "))
r=float(input("Enter Rate of interest: "))
r1=r/100
t=float(input("Enter Time in Years: "))
n=float(input("Enter Number of times interest is compunded per year: "))
q=n*t
total=p*(1+(r1/n))**q
print(f"Compound interest is {total}")

# Python Program to check Armstrong Number
arm=input("Enter Your Number: ")
sum=0
for i in arm:
    i=int(i)
    sum+=i**3
if sum==int(arm):
    print("The number is Armstrong")
else:
    print("Not Armstrong")

# Python Program for Program to find area of a circle
import math
radius=int(input("Enter radius of circle: "))
area=math.pi*radius
print(f"Area is {area}")

# Python program to print all Prime numbers in an Interval
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

int1=int(input("Lower Limit: "))
int2=int(input("Upper Limit: "))

for n in range(int1,int2+1):
    if is_prime(n):
        print(n)

# Python program to check whether a number is Prime or not
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# Python Program for n-th Fibonacci number
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_term = fib_series[-1] + fib_series[-2] 
        fib_series.append(next_term) 

num_terms = int(input("Enter the number of Fibonacci terms you want to generate: "))
fib_series = fibonacci(num_terms)
print("Fibonacci series up to", num_terms, "terms:", fib_series)
