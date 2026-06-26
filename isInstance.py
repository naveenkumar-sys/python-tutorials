# isinstance= is check the object/varibale is depend on that class/data type or not , this function expect two paraameter(a,int)

print(isinstance(10,int)) #print Tre if the val/obj is particular class/data type
 
 
#with mutliple class
print(3.5,(int,float))

#Check if an element of a list is a nested list
sampleList = ['Emma', 'Stevan', ['Jordan', 'Donald', 'Sam']]

for i in sampleList:
    # print(type(i))
    if isinstance(i,list):
        print("True")
    else:
        print("Flase")

#3.check and updated the value in the list
sample_list = ['Emma', 'Stevan', 12, 45.6, 1 + 2j, "Eric", ]
num_list=[]
str_list=[]

for val in sample_list:
    if(isinstance(val,(int,float,complex))):
        num_list.append(val)
    elif(isinstance(val,str)):
        str_list.append(val)

print(num_list)
print(str_list)

# isinstance() function With Inheritance
# The object of the subclass type is also a type of parent class. 
# For example, If Car is a subclass of a Vehicle, then the object of Car can be referred to by either Car or Vehicle.
# In this case, the isinstance(carObject, Vehicle) will return True.
