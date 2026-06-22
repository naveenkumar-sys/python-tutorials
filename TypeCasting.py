#type casting => convert one data type to another
#int() , float() , str()

# Note: we cant change the natural type like we cannot change string to integer
# important note 

# Type casting works only if the value can actually be converted to that type.
# str()   → Almost anything can become a string ✅

# int()   → Must look like an integer ✅

# float() → Must look like a number ✅


# # More Examples:
    
# String → Integer
# int("50")     # ✅ 50
# int("-50")    # ✅ -50
# int("5.5")    # ❌ Error
# int("abc")    # ❌ Error

# String → Float
# float("5")      # ✅ 5.0
# float("5.5")    # ✅ 5.5
# float("abc")    # ❌ Error

# Integer → String
# str(123)      # ✅ "123"

#There are two types of type casting 
#1. Implicit type casting - by default with python interpretor
#2. Explicit type casting - by user with inbuilt function
# 1.Implicit type casting 
a = 10      # int
b = 2.5     # float

result = a + b

print(result)
print(type(result))

#2.explicit type casting 
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