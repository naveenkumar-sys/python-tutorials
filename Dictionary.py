# Dictionaries are ordered collections of unique values stored in (Key-Value) pairs.

#3 ways to create 
#1.By enclosing elements in the curly brackets {}
new_list={
    "name":"Baleno",
    "Brand": "Suzuki",
    "Model":2021,
    "Price":1000000
}

# print(new_list)
# for key ,value in new_list.items():
#     print(key,value)
#2.By using dict() class
new1_list=(dict({"naveen":20,"age":21,"marks":80}))
print(new1_list)
#3.By using a dictionary literal


#sorted the dict using sorted()
dict_1={"b":1,"a":2,"c":3}
print(sorted(dict_1.items())) #sorting dictionary by keys

print(sorted(dict_1.values())) #sorted values in the dictionary by values()
 