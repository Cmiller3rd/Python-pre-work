# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    """Greet a user by their username"""
    print("hello_" + user_name.upper() + "!")
    
hello_name('cmiller')

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """print odd numbers from 1-100"""
    x = 0
    while x < 100:
        x +=1
        if x % 2 == 0:
            continue
        print(x)

first_odds()

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    """find the highest value in a list"""
    a_list.sort()

    return a_list[-1]

max_num_in_list([1, 4, 10, 12, 1000, 0, 33, 875])
               
# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """determine whether this is a leap year"""
    leap = True
    if a_year % 4 != 0:    
        leap = False
    elif a_year % 400 != 0 & a_year % 100 == 0:
        leap = False
    else:
        leap = True
    return leap

is_leap_year(2200)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    """check for consecutive numbers"""
    consecutive = False
    for num in range(len(a_list) - 1):
        if a_list[num] + 1 == a_list[num+1]:
            consecutive == True
    return consecutive


is_consecutive([1,2,4,5,7])