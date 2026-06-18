#Mainly 5 types of data types 
#1.Numeric -> int, float,complex
#2. Sequence -> string , list , tuple
#3. boolean
#4. set
#5. Dictionary 

#1.Numeric
#int
num =10
print(num)
num = int(20)  # assign the value using int() keyword
print(num)
print(type(num)) 
#float
num1=23.456
print(num1) 
print(type(num1))
#complex
num2 = 2 + 9j
print(num2)
print(type(num2))

#2.sequence
#string
name="Naveen"
print(name)
print(type(name))
print(name[2])
for name in name:  #directly iterate the value
    print(name)
for i in range(len(name)): #wants to find position 
    print(i)
    
#list - ordered collection (also known as a sequence ) of elements , Its is mutable we can change the value
# The list can contain data of all data types such as  int, float, string
# Duplicates elements are allowed in the list
# The list is mutable which means we can modify the value of list elements
# By enclosing elements in the parenthesis ()
# Using a tuple() class


# note : list can be created in two ways 
# 1.using []
my_list = ["Jessa", "Kelly", 20, 35.75]
# display list
print(my_list)  # ['Jessa', 'Kelly', 20, 35.75]
print(type(my_list))  # class 'list'

# Accessing first element of list
print(my_list[0])  # 'Jessa'

# slicing list elements
print(my_list[0:2]) #['jessa','kelly']

# modify 2nd element of a list
my_list[1] = "Emma"
print(my_list[1])  # 'Emma'

# 2. using list()
# create list using a list class
my_list2 = list(["Jessa", "Kelly", 20, 35.75])
print(my_list2)  # ['Jessa', 'Kelly', 20, 35.75]

#Tuple -Tuples are ordered collections of elements that are unchangeable. 
# The tuple is the same as the list, except the tuple is immutable means we can’t modify the tuple once created.

#creation of tuple
# 1.By enclosing elements in the parenthesis ()
my_tuple = (1,2,3,4,5,6)
print(my_tuple)
print(type(my_tuple))

#accessing the element
print(my_tuple[2])

#slice the value
print(my_tuple[2:7])

#modify the value - we can not modify it
# my_tuple[0]=29


# 2. Using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)  # (10, 20, 30, 40)


#3.boolean
is_active=True
print(type(is_active))

#4.Dictionary - value are stored in key and value pairs and value are mutable (like json object)
#unless the js here we only use [] to modify or access 

#By enclosing key and values in the curly brackets {}
my_dict ={
    "name":"naveen",
    "age":24,
}
print(my_dict)
print(type(my_dict))

#access the value
print(my_dict["name"])
#modify the value
my_dict["age"]=23
print(my_dict)
#adding the value
my_dict["degree"]="cse"
print("After adding:",my_dict)
# Using a dict() class.
my_dict2=dict({"name":"naveen", "age":24,})
print(my_dict2)


#5.set -In Python, a set is an unordered collection of data items that are unique. 
# In other words, Python Set is a collection of elements (Or objects) that contains no duplicate elements.
# It is mutable which means we can change set items
# Duplicate elements are not allowed
# Heterogeneous (values of all data types) elements are allowed
# Insertion order of elements is not preserved, so we can’t perform indexing on a Set

# By enclosing values in the curly brackets {}
# create a set using curly brackets{,}
my_set = {100, 25.75, "Jessa"}
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'
# add element to set
my_set.add(300)
print(my_set)  # {25.75, 100, 'Jessa', 300}
# remove element from set
my_set.remove(100)
print(my_set)  # {25.75, 'Jessa', 300}

# Using a set() class.
# create a set using set class
my_set = set({100, 25.75, "Jessa"})
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'
