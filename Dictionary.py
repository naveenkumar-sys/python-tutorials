# Dictionaries are ordered collections of unique values stored in (Key-Value) pairs.

#3 ways to create 
#1.By enclosing elements in the curly brackets {}
new_list={
    "name":"Baleno",
    "Brand": "Suzuki",
    "Model":2021,
    "Price":1000000,
    "varient":{
        "color":"Black",
        "price": 1200000,
        "Model":2023
    }
}
print(new_list)

# print(new_list)
# for key ,value in new_list.items():
#     print(key,value)
#2.By using dict() class
new1_list=(dict({"naveen":20,"age":21,"marks":80}))
print(new1_list)
#3.By using a dictionary literal
new2_list=dict([("name","Mark"),("country","America"),("telephone","6467873212")])
print(new2_list)

#Accessing the dictionary value
#1.using[]key 
print(new_list["name"])
print(new_list["varient"]["price"]) #nested access
#2.get method
print(new_list.get("name"))
print(new_list.get("varient").get("color"))
#get all keys and value

#1.get all keys
for key in new_list.keys():
    print(key)
#2.get all values
for value in new_list.values():
    print(value)
#3.get all keys and values
for key,value in new_list.items():
    print(key,":",value)

#check the value is present in dict or not with the help of values()
if "Baleno" in new_list.values():
    print("yes")

#finding the  length og the dictionary
print(len(new_list))

#update or adding th value in the dictionary 
#1.using []
new_list["color"]="Blue"
print(new_list)
new_list["varient"]["retail"]="High"  #nested adding
print(new_list)

#2.using update() method
new1_list.update({"country":"India" ,"status":"single"}) # adding the value as {}
print(new1_list)

new1_list.update([("sex","male"),("degree","BE.CSE")]) #adding element with list of tuples
print(new1_list)

#modify the value in the list 
#1.using []
new1_list["age"]=23
print(new1_list)
new_list["varient"]["model"]=2026 #nested key value modification
print(new_list)
#2.using update() method
new1_list.update({"marks":90 , "major":True}) #modify and new value
print(new1_list)

#setDefault() is used to assign default value created key if there is not 
new1_list.setdefault("key") #add the key name as key and value for key is None
print(new1_list) 

#--> remove item in dictionary
#1.popitem()->remove last key and value in dict
new1_list.popitem()
# print(new1_list.pop()) give length of the dict
print(new1_list)
#2.pop()-> expect a value and remove that
new1_list.pop("major")
print(new1_list)
# print(len(new1_list)) find length
#3.del key ->remove or delete that particular key and value
del new1_list["sex"] 
print(new1_list)
#4.clear ->clear entire key , value pairs
new1_list.clear()
print((new1_list))
#5.del -> delete entire dictionary
#def new1_list
#print(new1_list)

#--> Join two dictionary
# 1.update() method 
dict1={"a":1,"b":2,"c":3} 
dict2={"d":4,"e":5,"f":6}
dict1.update(dict2) #like modify we can merge two dictionary
print(dict1)
# 2.** arbitrary keyword operation
student_dict1 = {'Aadya': 1, 'Arul': 2, }
student_dict2 = {'Harry': 5, 'Olivia': 6}
student_dict3 = {'Nancy': 7, 'Perry': 9}

# join three dictionaries 
student_dict = {**student_dict1, **student_dict2, **student_dict3}
# printing the final Merged dictionary
print(student_dict)
# Output {'Aadya': 1, 'Arul': 2, 'Harry': 5, 'Olivia': 6, 'Nancy': 7, 'Perry': 9}

#copy the dictionary
# 1.copy() -> swallow copy does not affect another copy 
dict1 = {'Jessa': 70, 'Emma': 55}
dict2=dict1.copy() #make copy
dict1.update({"kamal": 45}) #adding new item in the dict and it does not make affect on dict2
print(dict1)
print(dict2)

#2.dict() ->swallow copy does not affect another copy 
dict1 = {'billa': 70, 'valla': 55}
dict2=dict(dict1)
dict1["kala"]=69
print(dict1)
print(dict2)

#3.= -> assignment operator but it is deep copy
dict1 = {'billa': 70, 'valla': 55}
dict2=dict1
dict2.update({"billa":75})
print(dict1)
print(dict2)

#Nested dict
# address dictionary to store person address
address = {"state": "Texas", 'city': 'Houston'}

# dictionary to store person details with address as a nested dictionary
person = {'name': 'Jessa', 'company': 'Google', 'address': address}

print(person)

for key,value in person.items():
    if key=="address":
        for j,val in person["address"].items():
            print(j,":",val)


# each dictionary will store data of a single student
jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

# Outer dictionary to store all student dictionaries (nested dictionaries)
class_six = {'student1': jessa, 'student2': emma, 'student3': kelly}

print(class_six)

for key , value in class_six.items():
    # print(key,":",value)
    for j , val in class_six[key].items(): # for j , val in value.item()
        print(j,":",val)
    print("------------------")

for value in class_six.values():
    print(value)
# output
# {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
# {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
# {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}

for key in class_six.keys():
    print(key)
# output
# student1
# student2
# student3

#sort()
dict1 = {'c': 45, 'b': 95, 'a': 35}

# sorting dictionary by keys
print(sorted(dict1.items()))
# Output [('a', 35), ('b', 95), ('c', 45)]

# sort dict eys
print(sorted(dict1))
# output ['a', 'b', 'c']

# sort dictionary values
print(sorted(dict1.values()))
# output [35, 45, 95]

#Dictionary comprehension 
#formula -output_dictionary = {key : value for key,value in iterable [if key,value condition1]}
# calculate the square of each even number from a list and store in dict
numbers = [1, 3, 5, 2, 8]
dict_res={val:val**2 for val in numbers  if val%2==0}
print(dict_res)

telephone_book = [1178, 4020, 5786]
petelephone_book = [1178, 4020, 5786]
persons = ['Jessa', 'Emma', 'Kelly']

telephone_Directory = {key: value for key, value in zip(persons, telephone_book)}
print(telephone_Directory)
# Output {'Jessa': 1178, 'Emma': 4020, 'Kelly': 5786}