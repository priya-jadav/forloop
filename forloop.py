# What is a Loop?
# A loop is used to repeat a block of code multiple
# times until a condition is met.

# Types of Loops in Python
# 1. for loop
# Used when we know how many times we want to repeat.



# Syntax:
# for variable in sequence:
 #     # code

 # range() function is commonly used to generate a
 # sequence of numbers:

 #range comes with 3 parameters:
 # 1. start (inclusive)
 # 2. stop (exclusive)
 # 3. step (optional, default is 1)
 

 # range(start, stop-1, step)

# Key Points:
# 2. range(start, stop) generates numbers
# 2. Loop runs fixed number of times


#
# 2. while loop
# Used when we repeat until a condition becomes False

# Syntax:
# while condition:
#  #code

# break
# stops the loop immediately

# ex:
for i in range(1, 6):
    if i == 3:
        break
        print(i)

# 2. continue
# skips current iteration

for i in range(1, 6):
    if i == 3:
        continue
        print(i)
# 3. pass
# Does nothing (placeholder)

#for i in range(5):

#3.pass
#does nothing
for i in range(5):
    pass

#1.print number 1 to 10  using for loop
for i in range(1, 11):
    print(i)


# Task 2
# Print even numbers from 1 to 20.



for i in range(1, 21):
    if i % 2 == 0:
        print(i)


for i in range(2, 21, 2):
    print (i, end='')


# Task 3
# Print odd numbers from 1 to 15.

# start:1
# end: 16
# step:2

for i in range(1, 16, 2):
    print(i, end='')


# Task 4
# print each character of the string.
text = "python"
  
for char in text:
    print(char)


# Task 5
# print all items in the list.

data = ["Data", "Science", "AI"]

for item in data:
     print(item)


# task 6
# Find the sum of numbers from 1 to 10.

total = 0
for i in range(1, 11):
    total += i

    print(total)

# task 7
# print multiplication table of 5.

for i in range(1, 11):
    print(f"5 x {i} {5 * i}")


# task 8
# Count how many vowels are in a string.

text = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
    print(f"Number of vowels: {count}")

# task 9
# print numbers in reverse order from 10 to 1.

for i in range(10, 0, -1):
    print(i)

# task 10
# print square of numbers from 1 to 5.

for i in range(1, 6):
    print(i ** 2)
    

