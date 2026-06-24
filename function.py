#function - block of code that is executed only when it is called , it can be reused many times
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