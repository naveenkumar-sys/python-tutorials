# for lopp in python we use when the we know the iteration count  , like untill this many iteration we have to run the loop
names=["sarvana","ramesh","nandhini","kamal"]
new_names=[]
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