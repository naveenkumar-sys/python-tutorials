#function - block of code that is executed only when it is called , it can be reused many times

#--->syntax:<-----
# def fn_name(parameters):
#     # function definition
# fn_name() #function call

#Example 3: Sum of numbers from 1 to n using recursion

# def sum(n):
#     if(n==1):
#         return 1
#     return n + sum(n-1) 
# print(sum(4))

# def total(n):
#     if n == 1:
#         return 1
#     return n + total(n - 1)

# print(total(5))


#global variable - variable that is defined outside of a function and can be accessed from inside the function but modify it inside the function

global_var=10

def greet():
    # global_val+=2  #UnboundLocalError: cannot access local variable 'global_val' where it is not associated with a value
    print(global_var)
greet()
print(global_var)



#local variable - variable that is defined inside a function and can only be accessed inside the function

def welcome():
    name="Naveen"
    print("welcome",name)
welcome()
# print(name) #we cannot access local variable

#if we want to access local variable we have to use global variable and modify it means use global keyword

name="Naveen"
def welcome():
    global name # we have to use global keyword
    name += "kumar"   #this will modify the global variable
    print("welcome",name)
welcome()
print(name)

#non local variable - variable that is defined inside a function but can be accessed outside the function and act as a global variable inside the function
def outer():
    x=15
    print("outer",x)
    def inner():
        nonlocal x # we have to use nonlocal keyword , inner function will access and modify the outer function variable , like closure in javascript
        x+=10
        print("inner",x)
    inner()

outer()
# print(x) # we cannot access non local variable

# Positional arguments
def sum(a,b,c):
    print(a+b+c)
sum(1,2,3)
# keyword arguments
sum(b=2,a=1,c=3)
# Default arguments
def sum(a=1,b=2,c=3):
    print(a+b+c)
sum()
# Variable-length arguments
def sum(*args):
    print(args)
sum(1,2,3,4,5)

a = range(1,11)
print(set(a))

#recursion - a function that calls itself and is used to solve complex problems by breaking them down into simpler sub problems , it save data into call stack which is last in first out
#Example 1 — sum of first n numbers
sum=0
def total(n):
    if n==0:  #1. base case - decide when to stop
        return 
    global sum #2 . expression
    sum+=n
    total(n-1) #3. recursive call
total(5)
print(sum)

#Example 2 - print n numbers in 1 to 10
def n_number(n):
    if n==0:
        return
    n_number(n-1) # for each time function call , the print is not executed and value is stored in call stack and after the function is executed the value is printed in last in first out order
    print(n)  #1,2,3,4,5
n_number(5)
print("---------------")
#Example 2 - print n numbers in 1 to 10
def n_number(n):
    if n==0:
        return
    print(n) #here data is directly printed instead of storing in call stack
    n_number(n-1)
n_number(5)


#return

# here once the a is called and answer is came after only its return 
def a():
    return 10

def b():
    return 5 + a()

print(b())


#lamba function -> anonymous function , which is one line function
#Function syntax 
# # lambda parameters: return_expression
add=lambda a : print(a)
add(10)

#sum of two number fnction 
print_sum=lambda a,b:a+b
print(print_sum(2,3))

#even/odd using lambda
check=lambda x : x%2==0
print(check(1) )

# normal function 
# def res(x):
#     if(x>0):
#         return "Positive"
#     else:
#         return "Negative"
# print(res(10))
#lambda with condition
result=lambda x:"postive" if x>0 else "negative"
print(result(3))
print(result(-3))
# Lambda allows only short expressions like:
# lambda x: x * 2
# lambda x: x % 2 == 0
# lambda x: "Even" if x % 2 == 0 else "Odd"
# lambda x: len(x)
# lambda x: x[1]

# Important small point
# Direct loop block inside lambda → ❌ not allowed

# But lambda can still be used with functions that internally iterate, like:
# map()
# filter()
# sorted()

# 1) map() → transform every item

# Use when: “For each value in this list, change it to something else.”

# Syntax
# map(function, iterable)
# function = what to do to each item
# iterable = list/tuple/string/etc.
#Example: double every number wiht map and lamda 
nums = [1, 2, 3, 4]
res=list(map(lambda n:n*2 ,nums)) #we pass function , itrables in function we return value  and givre new map object (<map object at 0x7fb2ce693910>) and we change that to list
print(res)

#map with noraml function
def mult(n):
    return n*2

res2=list(map(mult,nums))
print(res2)

#perform cubic operation for sequence
list1 = [2, 3, 4, 8, 9]
final=list(map(lambda x: x**3,list1))
print("Cubic List is",final)

# 2) filter() → keep only matching items

# Use when: “From this list, keep only the items that satisfy a condition.”
# Syntax
# filter(function, iterable)
# function should return True/False
# if True → keep the item
# if False → remove it 
# sorted(iterable, key=function, reverse=boolean)

#Example with lambda function
num2=[1,2,3,4,5,6]
fil_res=list(filter(lambda n:n%2==0 , num2))
print(fil_res)

#example using filter with normal function 

def even(n):
    if n%2==0:
        return n

res2=list(filter(even,num2))
print(res2)

#2.filter positive number in list
l = [-10, 5, 12, -78, 6, -1, -7, 9]

result3=list(filter(lambda val:val>0,l))

print("positive list are ",result3)




#3. reduce() function in Python
# In Python, the reduce() function is used to minimize sequence elements into a single value by applying the specified condition.

# The reduce() function is present in the functools module; hence, we need to import it using the import statement before using it.

# Syntax of reduce() function:

# reduce(function, sequence)
from functools import reduce
list1 = [2, 3, 4, 8, 9]
sum=reduce(lambda x,y:x+y,list1)
print("The sum of all sume using reduce",sum)












#  sorted() → arrange items in order and dirtectly return new list 

# Use when: “Sort this data.”

# Syntax
# sorted(iterable, key=None, reverse=False)
# iterable = data to sort
# key = function that tells Python what value to sort by
# reverse=True = descending order

# words = ["apple", "kiwi", "banana", "fig"]
# res=[]
# len_fuit=0

# words.sort(key=len)
# print(words)


# Difference between sorted() and .sort()
# 1. sorted()

# Returns a new sorted list, original list stays same.

words = ["apple", "kiwi", "banana", "fig"]

res = sorted(words, key=len)
print(res)    # sorted result
print(words)  # original unchanged
# 2. .sort()

# Changes the original list itself

words = ["apple", "kiwi", "banana", "fig"]

words.sort(key=len)
print(words)

# Use map() when:
# every item must be transformed
# examples:
# double all numbers
# convert strings to uppercase
# add 10 to each item
# Use filter() when:
# you want only some items
# examples:
# keep even numbers
# keep words longer than 5
# keep names starting with A
# Use sorted() when:
# you want order
# examples:
# sort numbers
# sort by string length
# sort students by marks
