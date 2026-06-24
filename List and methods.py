#List in python are sequence of data types and mutable
#List is a collection of items in a particular order

#creating a list - 2types
# 1.By enclosing elements in the square brackets []
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))
# 2. Using a list() class
my_list = list((1, 2, 3, 4, 5))
print(my_list)

#accessing the list-3 types 
# 1. Indexing 
print(my_list[2]) #3
print(my_list[-2]) #4
# 2. Slicing - listname[start:end:step]
print(my_list[1:4]) #[2,3,4] shows elements from index 1 to 3
print(my_list[:3]) #[1,2,3] print upto 2nd index
print(my_list[3:]) #[4,5] start from index 3 to the list end
print(my_list[::2]) #[1,3,5] start is none, end is none , i give step is 2 so it give start with first and move on to every second index
print(my_list[::-1]) #[5,4,3,2,1] printing the list in reverse order , -1 is step 
print(my_list[::1]) #[1,2,3,4,5] print list with left to right
print(my_list[0:4:2]) #printing from 0th index to 3rd index with step of 2 , it first 0th index followd by 2 step of index

#3.Iterating the List -> 2 type
# 1.only access the value 
for  num in my_list:
    print(num)
print("----------------")
# 2. access the index 
for i in range(0,len(my_list)):
    print(i,my_list[i])
print("-------------------")
#3.access the index and value both at same time 
for i,val in enumerate(my_list):
    print(f"The {i} index of value is {val}")
print("----------------------")

#Adding the elements/list in the list 
# With these three type we can add the element append , insert , extend 
#append-add the element in end of the List , it only accept one element or single list , add nested list if we pass a parameter as list
my_list.append("Emma")
print(my_list)

#insert - add the element/sequence in particular index of the element , It expect two arguement(index,element)
my_list.insert(2,25)
my_list.insert(3,[45,46,47,89])
print(my_list)

#extend - add the sequence of element at the end of the list
my_list.extend([3,5,6,7,8])
print(my_list)

# for i in range(len(my_list)):
#     if(i==3):
#         for j in range(0,len(my_list[i])):
#             print(my_list[i][j])
#     # print(my_list[i])

#Modifying the element 

#1.modifying the single element 
my_list[3]=43
print(my_list)

#2.modifying range of items
my_list[1:4]=["apple","Orange","Grapes"] #modifying element which is in 1 index tt until 3rd index
print(my_list)

my_list[3:]=["banana","pineapple"]
print(my_list)

# my_list[::2]=["True"]
# print(my_list)

# #Modify all the element
# for i in range(len(my_list)):

#Remove Element 
#1.remove() -> remove the element from the list
my_list.remove("apple")
print(my_list)

#2.pop() -> remove the element from the list
my_list.pop() #default remove last element in the list
print(my_list)
my_list.pop(1)
print(my_list)

#3.clear() -> clear the elements in lists return empty List
my_list.clear()
print(my_list)

# #4.delete() -> delete entire list
# del my_list
# print(my_list)  # give error called my_list is not defined

#Finding the index of the given value by index() method 
new_list=[2,5,8,6,2,4,1]
print(new_list.index(4)) 

#concatenation of two list - 2 ways 
# 1. using + 
second_list=[5,6,9,2,3]
third_list=new_list+second_list
print(third_list)

#2.using extend () -> this method expect single List as parameter and add as element
third_list.extend(["apple","Orange","pine apple"])
print(third_list)

#Nested list
nestedlist = [[2,4,6,8,10],[1,3,5,7,9]]

for item in nestedlist:
    for val in item:
        print(val , end=" ")
    print()
    
#List comphrension 
# formula - [new_value for item in iterable if condition1 if condition2]
# What to add      → new_value
# Loop variable    → item
# Collection       → iterable

# Example 1: Square Numbers
res=[val*val for val in range(1,6)]
print(res)
#Example 2: Copy a List
new1=[1,2,3,4]
new2=[val for val in new1] #shallow copy
print(new2)
new1.append(5)
print(new1) 
print(new2)

#Example 3: Convert Strings to Integers
# nums = ['1', '2', '3']
# result=[int(val) for val in nums]
# print(result)

#with condition
#formula:[new_value for item in iterable if condition]
#Example 4: Find even numbers
nums = [1, 2, 3, 4, 5, 6]
result=[val for val in nums if val%2 ==0]
print(result)

# Example 5: Length of Each Word
words = ["apple", "banana", "cat"]
res=[len(val) for val in words]
print(res)

# Example 6: Uppercase Words
words = ["apple", "banana"]
res=[val.upper() for val in words]
print(res)