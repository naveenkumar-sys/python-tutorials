#type casting => convert one data type to another
#int() , float() , str()
# Note: we cant change the natural type like we cannot change string to integer

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