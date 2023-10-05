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

