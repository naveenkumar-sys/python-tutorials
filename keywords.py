#keyword - the word which has special meaning , in python there are 36 keywords
# get keyword from python  lib 
import keyword 
print(keyword.kwlist)

#method-2
help("keywords")

#find the defintion for that exact keyword 
# print(help("if"))

#types of keyword
    #1.value keyword - True.False, None .
    #2.operator keyword - and->both value are true , or -> any oen of this true  , in -> value which is inside that range  , is -> returns true if both memory address are true  ,not -> logical keyword where return true if expression are false 
#example - and , or , not -> logical operators
# x=True
# y=True
# if(x and y):
#     print("Both are true")
#     if(x or y):
#         print("one value is true")
# else:
#     print("both are false")
# if(not x and y):
#     print("invalid x , y is not defined")
    
#example - is 
x=10
y=12
z=10

if(x is y):
    print("x and y as same memory address")
elif( x is z):
    print(" x and z has same memory address")
else:
    print("both condition are false")
    
# example - in  -> its return any number in sequence like includes() method in js
arr = [1,2,3,4,5]
num = 5
if num in arr:
    print("The num is present")
for i in range(len(arr)):
    print(arr[i])
    
# print(help('len'))

    