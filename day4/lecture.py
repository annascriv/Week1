print("hello,world")

a_small_number = 4.5

#checking data types
print(type(a_small_number))

#In python there is no type casting (ie 'five' != 5)
print('five'==5) #false

name = 'Anna'
#string interpolation - f string
print(f"Hello, my name is {name}")

#Data Types

#Lists
berries = ['grape','tomato','raspberry','blackberry','couscous']
print(berries)

#in this class arrays and lists are interchangeable

print(berries[0])
print(berries[-1]) #prints the last element, indexes backwards

#cool features of python lists
print(berries[2:4]) #a slice from a list, start is inclusive & end is inclusive
print(berries[2:]) #slices from 2 (inclusive) to the end

#reverse
print(berries[::-1])

#Tuples
#tuple is kinda like a list but it is immutable

days_of_the_week = ('sunday','monday','tuesday','wednesday','thursday','friday','saturday')

#if a tuple has only one element must be followed by a comma

#Dictionaries
jeff = {
    'name':'jeff',
    'age':45,
    'job': 'influencer',
    'favorite foods': 'french fries'
}
print(jeff['age'])
print(jeff.get('favorite foods'))

# Functions

def gimme_five():
    return 5

print(gimme_five()+10)

def add_one(n):
    return n+1

print(f"I have {add_one(4)} berries.")

def print_them_all(*args):
    print(args)

print(print_them_all("alice",5,"eleanor",18))

#keyword args
def describe_berries(n=1, color="blue"):
    return(f"I have {n} {color} berries.")
print(describe_berries(n=4,color='purple'))

# def who_am_I(**kwargs):
#     for kwarg in kwargs:
#         print(f"My {kwarg} is {kwargs[kwarg]}")
# print(who_am_I('1','3','4'))      

#with keyword args argument order does not matter

#tuple holds less memory than list since it is immutable

#conditional logic and loops

def can_drink_beer(age,country):
    if age >= 21 or age >= 18 and country == 'Canada':
        return True
    
    #else if statement
    elif country == 'Antarctica':
        return True
    else:
        return False
    

print(can_drink_beer(20,'Canada'))

#Looping over list elements
my_list = ['a','b','c']

for x in my_list:
    print(x)

#range
one_to_ten = range(10)
print(one_to_ten)

#loop through range

for x in one_to_ten:
    print(x)

for x in range(7):
    print(x)

#loop through list and get an index
for index, el in enumerate(my_list):
    print(index,el)

#builtins-lambdas-modules
#python number methods

name = 'anna louise'
print(name.title())

print("roberto".capitalize())

name.capitalize()
print("young".replace("ng","th"))
last_name='scriven'
print(last_name.capitalize())

#lamda functions

def say_hello(name):
    print(f"hello {name}")

def say_hello_extra(name,other_hello_function):
    print(f"hi {name}")
    other_hello_function(name)

say_hello_extra("Robert", say_hello)


## parameters can be anything, they are just placeholders for arguments that are passed into the function

def add_one(x):
    return x + 1

add_two = lambda x : x + 2

print(add_two(5))

say_hi = lambda name : f"hello {name}"

say_hello_extra = ("Bob", say_hi)

#map function: maps an item from one list to a new item in a new list
new_list = map(lambda item : item + 2, my_list)
print(new_list)

# for x in new_list: 
#     print(x)

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_list_divisible_by_three = filter(lambda item : item%3 == 0, my_list)

print(list(new_list_divisible_by_three))

#reduce function (also a sort function but skipped it)

a_list = [1,2,3,4,5,6,7,8,9,10]

words = ["hello", "world","it's","sunny"]

import functools
sentence = functools.reduce(lambda agg, item : f"{agg} {item}", words)


#modules: from <file_one> import <name>

import filetwo
my_var = 5
print(my_var)

filetwo.hello()
print(filetwo.my_var)
print(my_var)

#reading and writing files

# import os 

# abs_path_to_file = os.path.abspath()

#try & except error handling

