#type casting => convert one data type to another
#int() , float() , str()
# Note: we cant change the natural type like we cannot change string to integer

#There are two types of type casting 
#1. Implicit type casting - by default with pyhton interpretor
#2. Explicit type casting - by user with inbuilt function
name ="name"
print(type(name))
print(int(name)) # ValueError: invalid literal for int() with base 10: 'name'

#but we change integer into any other data type 
x = 10
print(type(x))
y = float(x)
print(type(y))
z = str(x)
print(type(z))