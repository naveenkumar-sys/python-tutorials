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

#3.Itertating the List -> 2 type
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
#append-add the element in end of the List , it only accept one element
my_list.append("Emma")
print(my_list)

#insert - add the element/sequence in particular index of the element , It expect two arguement(index,element)
my_list.insert(2,25)
my_list.insert(3,[45,46,47,89])
print(my_list)

#extend - add the seqence of element at the end of the list
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
my_list[1:4]=["apple","Orange","Grapes"] #modifying element which is in 1 index tt untill 3rd index
print(my_list)

my_list[3:]=["banana","pineapple"]
print(my_list)

# my_list[::2]=["True"]
# print(my_list)