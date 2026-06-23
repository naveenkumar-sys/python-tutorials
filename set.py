
# A Set in Python is a collection that stores unique values only. ->no duplicate and un order which has not index
#In Python, a Set is an unordered collection of data items that are unique. In other words, Python Set is a collection of elements (Or objects) that contains no duplicate elements.
set1={"Apple","Orange","pineapple"}

nums = [1, 2, 2, 3, 3, 4]
print(list(set(nums)))

#Adding the element
#1.Add()
set1.add("Grapes")
print(set1)
#2.Remove()
set1.remove("Orange")  #if not present it throws a error 
print(set1)
#3.discard()
set1.discard("build") #if not present means it shoulds not throw error
print(set1)

#Looping through the set
for fruits in set1:
    print(fruits)
    
#Convert List to Set
new_set=set(nums)
print(new_set)

#Important Set Operations
#union - combine two sets value
a={1,2,3,4}
b={5,4,3,8}
print(a|b) 
#Intersection - commn elements
print(a&b)
#Difference - check if the all the first set element in the secnd set
print(a-b)
#pop()-remove random element
a.pop()
print(a)

| Feature    | List | Tuple | Set  | Dictionary    |
| ---------- | ---- | ----- | ---- | ------------- |
| Syntax     | `[]` | `()`  | `{}` | `{key:value}` |
| Ordered    | ✅    | ✅     | ❌    | ✅             |
| Duplicates | ✅    | ✅     | ❌    | Keys ❌        |
| Mutable    | ✅    | ❌     | ✅    | ✅             |
| Indexing   | ✅    | ✅     | ❌    | By key        |
| Key-Value  | ❌    | ❌     | ❌    | ✅             |
