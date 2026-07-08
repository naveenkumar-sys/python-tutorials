#  creating Variable  note -> variable does not store value it stored address (reference) of the value
a=10
b=10
print(a+b)
# fint the data type of the variable 
print(type(a))
#scoping - L , E, G, B
#local scope  -> retun inside in one block of code it only acces inside that 
def greet():
    name = 'Naveen'
    print(name)

# print(name) # name is not defined 

greet()

# global scope 

num1 = 10 # access this variable from anywhere
def add():
    num2=20
    print(num1+num2)
    
add()

# enclosing scope -> whcih is like closure in java script
def outer():
    num = 25 
    def inner():
        print(num*20) # inner functrion will remember outer function variable 
    inner()

# print(outer()) 
outer()

# Buit - in 
print(len([1,2,3])) #buit-in words 


#using f string in python -> where we can add the varibale inside the string

name="kamal"
print(f"my is name is {name}") 


a=10
a=20
print(a)