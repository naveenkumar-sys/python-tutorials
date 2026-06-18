# # Exercise 1. Print first 10 natural numbers using while loop
# num=1

# while num<11:
#     print(num)
#     num+=1
# print("-------------")
# #Exercise 2. Display numbers from -10 to -1 using for loop
# for i in range(-10,0):
#     print(i)
# print("---------------")
# #Exercise 3. Display a message “Done” after successful execution of for loop
# for i in range(0,5):
#     print(i)
# print("done")
# print("-------------------")
# #Exercise 4. Calculate the sum of all numbers from 1 to N
# num=int(input("Enter a Number:"))+1
# sum=0
# for i in range(1,num):
#     sum+=i
# print(sum)
# print("-----------------")
# #Exercise 5. Print multiplication table of a given number
# my_num=int(input("Enter a number:"))

# for i in range(1,11):
#     print(i*my_num)
# Exercise 6. Calculate the cube of all numbers from 1 to a given number
gn_num=int(input("Enter the number:"))
# print(gn_num*gn_num*gn_num)
for i in range(1,gn_num+1):
    print(f"current Nuumber is {i} and the cube is {i**3}")
    
