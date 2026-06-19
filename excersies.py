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
# # Exercise 6. Calculate the cube of all numbers from 1 to a given number
# gn_num=int(input("Enter the number:"))
# # print(gn_num*gn_num*gn_num)
# for i in range(1,gn_num+1):
#     print(f"current Nuumber is {i} and the cube is {i**3}")
    
# # Exercise 7. Display numbers from a list using a loop
# # The number must be divisible by five.
# # If the number is greater than 150, skip it and move to the next.
# # If the number is greater than 500, stop the loop entirely.

# numbers = [12, 75, 150, 180, 145, 525, 50]

# for num in numbers:
#     if(num%5==0):
#         if(num>500):
#             break
#         elif(num>150):
#             continue
#         print(num)

# #Exercise 8. Count occurrences of a specific element in a list
# list1 = [10, 20, 10, 30, 10, 40, 50]
# target = 10
# count=0
# for num in list1:
#     if(num==target):
#         count+=1
# print(count)

# #Exercise 9. Print elements from a list present at odd index positions

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# odd_list=[]

# # Expected Output: [20 40 60 80 100]
# for i,value in enumerate(my_list):
#     if(i%2!=0):
#         odd_list.append(value)

# print(odd_list)

# # Exercise 10. Print list in reverse order using a loop
# list1 = [10, 20, 30, 40, 50]
# reversed_list=[]
# for value in reversed(list1):
#     reversed_list.append(value)
# print(reversed_list)

# #method2
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])
    
# #Exercise 11. Reverse a string using a for loop (no slicing)
# # Original: Python
# # Reversed: nohtyP
# string="python"
# reversed_string=""
# for ch in reversed(string):
#     reversed_string+=ch
# print(reversed_string)

# #Exercise 12. Count vowels and consonants in a sentence
# new_string="Loops are Fun!"
# vowels=['a','e','i','o','u']
# vow_count=0
# cons_count=0

# for ch in new_string:
#     if ch ==" ":
#         continue
#     elif ch in vowels:
#         vow_count+=1
#     else:
#         cons_count+=1
# print(vow_count)
# print(cons_count)

# #Exercise 13. Count total number of digits in a number
# digit=75869
# count=0
# while digit!=0:
#     digit=digit//10
#     count+=1
# print(count)
    
# Exercise 14. Reverse an integer number
num =76542
new_list=[]
split = list(str(num))
print(split)
for i in reversed(split):
    new_list.append(i)

final=int("".join(new_list))
print(final)
print(type(final))
# print(type(new_list))