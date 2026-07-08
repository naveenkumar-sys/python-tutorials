a=10
b=a
print(a is b) # 10 is stored in memory (reference address) , we are assign the memory address of a so same reference address

c=20
d=20
print(c is d) # 20 object is created in one address , now for d is also same address because 20 is already created


list1=[1,2,3]
list2=list1 #hold copies of reference but both are same reference

list3=[1,2,3] #both are stored in different memory 
list4=[1,2,3]