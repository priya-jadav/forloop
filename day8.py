# What is a Function?
# A function is a block of code that runs only when it is called.

# Why use Functions?

# 1. Avoid repeating code
# 2. Makes program clean & organized
# 3. Easy to debug and reuse

# Syntax:
# def function name():
    # code
# ex:
# def greet():
#     print ("Hello Students")

# Syntax:
# def function_name():
    # code
# ex:
def greet():
      print ("Hello Students")
greet()

# Function with Parameters
# Used to pass values

def greet (name):
      print (f"Hello {name}")

greet("shreyarth")
greet("AICW")

def greet():
    print("hello student")
greet()

# Task 1:
# Create a finction to calculate and return result
# Hint: Use return statement)








# Task 2:
# Create a function to check if a number is even or odd.


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "odd"

check_even_odd(4) 
check_even_odd(7)


# Task 3:
# Create a function to find the factorial of a number
# Hint: Use a loop or recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -1)

num = int(input("Enter a number: "))
result = factorial(num)
print(result)

# Task 4
# create a function to find maximum of three numbers.

def find_max (a, b, C):
    if a >= b and a >= c:
       return a
    elif b >= a and b >= c:
       return b 
    else:
       return c

a = float(input("Enter first number: "))
b = float(input ("Enter second number: "))
c = float(input("Enter third number: "))
result = find_max(a, b, c)
print (f"The greatest number is: {result}")

# Task 5
# create a function to check if a string is palindrome.

def is_palindrome(s):
    # Remove spaces, punctuation, and convert to lowercase
    import string
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    
    return s == s[::-1]
    print(is_palindrome("Madam"))           # True
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("Hello"))           # False

#6.create a function to calculate the area of circle
def area_of_circle(radius):
   return 3.14 * radius ** 2

radius = float(input("enter radius of the circle:" ))
area = area_of_circle(radius)
print("the area of the circle is:(radius)")
