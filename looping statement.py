# for lopp in python we use when the we know the iteration count  , like untill this many iteration we have to run the loop
# Need only values?
# → for item in collection

# Need index + value?
# → enumerate(collection)

# Need numbers/counting? range(10)
# → range()
names=["sarvana","ramesh","nandhini","kamal"]
new_names=[]
#(range has three parameters which is start->where to start stop->where to stop step-> how will iterate ++ , -- , *2 )
for i in range(len(names)): #here we are looping with index with the name i to length of that names list , use when we want position 
   cap_names= names[i].upper()
   new_names.append(cap_names)

print(new_names)
   

for name in names: #here we are directly accessing the value in names list , use when we directly want the values to be iterated
    print(name.upper())
    
# #while loop in pyhton we use when we dont know the iteration count , like untill then then condtion is true we have to run the loop , we can able to condition
# #run or iterate untill given condition became false
# corect_password="naveen"
# password=''
# while password != corect_password:
#     password = input("Enter the password")

# print("password is correct")

#Break statement - break out the loop statement
target_name="nandhini"
for name in names:
    if name ==target_name:
        break
    print(name)      
    
#continue - skip the iteration 
for name in names:
    if name== target_name:
        continue
    print(name)  
    
#pass - placeholder , when it nothing in the body it does not skip or break an iteratin 

for i in range(10):
    if(i==5):
        pass  #when nothing to write we just use pass without leave as empty(error)
    print(i)


#while statement  using break 
# product is added untill user enter the products as done , if user enter done iteration break 
is_completed = "done"
cart=[]

while True:
    product = input("enter a product")
    if product=="done":
        break
    cart.append(product)

print(cart)

# contolling the loop 
# start from 1 and stop at 9
for i in range(1,10):
    print(i)

print("----------------")
    
#here we start with 10 and ends with 0 with step of reverse iteration -1
for i in range(10,0,-1):
    print(i)
print("----------------------")    

#here we start with 1 and end with 11-1=10 with step of iteration 2
for i in range(1,11,2):
    print(i)
print("---------------")
    
    
    
    
    
#nested forloop 
for i in range(5):
    for j in range(5,i,-1): #range has three parameter start , stop , step
        print("*",end=" ")
    print(end="\n")
print("----------------")
for i in range(6):
    for j in range(0,i):
        print("*",end=" ")
    print(end="\n")


# Real time example 
department = [
    {
        "name": "CSE",
        "students": ["A", "B"]
    },
    {
        "name": "IT",
        "students": ["C", "D"]
    }
]

# Direct iteration over values/items
for dept in department:
    for student in dept["students"]:
        print(student)

# Index-based iteration
for i in range(len(department)):
    for j in range(len(department[i]["students"])):
        print(department[i]["students"][j])
        
        
#looping the list 
my_list = [1, 2, 3, 4, 5]

for num in my_list:
    print(num)
    

#looping the string 
my_string = "Hello,World!"

for char in my_string:
    print(char)


# looping through ths dictionary  
#with key, value with item() method
my_dict = {"name": "John", "age": 30, "city": "New York"}

for key,value in my_dict.items():
    print(key,value)
    
#with key only
for key in my_dict:
    print(key)
    
#with valuesn only with using value() method
for key in my_dict.values():
    print(key,end=" ") 
    
#instead of using range for getting index(position ) we have enumerate will give index of each iteration
names=['naveen','kalai','kumar']
for i, name in enumerate(names):
    print(i, name)

#1.print value range 1 to 10
for i in range(11):
    print(i)
    
#2.print even number upto 20
for i in range(1,21):
    if(i%2==0):
        print(i)

#3.sum of numbers 
new_list=[1,2,3,4,5,6]
sum=0
for value in new_list:
    sum+=value
print(sum)
#4.vowels in string
name = "kavin"
count=0

for ch in name:
    if(ch in ["a","e","i","o","u"]):
        count+=1
print(count)
#5.Reverse the string
name = "naveen"
for i in reversed(name):
    print(i,end=" ")

#6.find the largest number in the array
numbers = [10, 45, 20, 100, 5]
largest=0

for num in numbers:
    for j in numbers:
        if(num>j):
            if(largest<num):
                largest = num
print(largest)

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if(numbers[i]>numbers[j]):
            if(largest<numbers[i]):
                largest=numbers[i]
print(largest)        
    
#7.print the dictinary key and values
student = {
    "name": "Naveen",
    "age": 22
}

for key,value in student.items():
    print(key,value)

#8.Nested Loop Pattern
for i in range(0,6):
    for j in range(0,i):
        print("*",end=" ")
    print(end="\n")
    
#9.count the student in all department 
departments = [
    {
        "name": "CSE",
        "students": ["A", "B"]
    },
    {
        "name": "IT",
        "students": ["C", "D","E"]
    }
]

count=0

for dept in departments:
    for student in dept["students"]:
        count+=1
print(count)

#10.print the Index and Value 
names = ["A", "B", "C"]

for i, name in enumerate(names):
    print(i,name)