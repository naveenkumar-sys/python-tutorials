#creating a tuple -> 2 ways 
#1.By enclosing elements in the parenthesis ()
my_tuple = (1,2,3,4,5,6)
print(my_tuple)
print(type(my_tuple))
#2. Using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)

#if add one element in tuple it show type as string and add comma it show type as tuple
my_tuple3 = (1)
print(type(my_tuple3))
my_tuple4 = (1,)
print(type(my_tuple4))

#packing and unpacking
#packing - tuple
tuple1=1,2,3,4,5
print(tuple1)
print(type(tuple1))
#unpacking - list
i,j,k,l,m=tuple1
print(i,j,k,l,m)

#length of tuple
tuple1=1,2,3,4,5
print(len(tuple1))

#iteration
tuple1=1,2,3,4,5
for i in tuple1:
    print(i)

#tuple inside tuple
tuple1=1,2,3,4,5
tuple2=6,7,8,9,10
tuple3=tuple1,tuple2
print(tuple3)

#acess the tupes-2ways
# 1.Indexing
tuple1=1,2,3,4,5
print(tuple1[2])
# 2. Slicing
tuple1=1,2,3,4,5
print(tuple1[1:4])

#ieration
tuple1=1,2,3,4,5
for i in tuple1:
    print(i)

#modification and add is not possible
#if want to change the value of tuple we have to convert it into list and change the value and convert it into tuple
tuple3=(4,5,6,7)
change_list=list(tuple3)
print(change_list)
change_list[2]=32
print(change_list)
tuple1=tuple(change_list)
print(tuple1)

#remove the item in the tuple

