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
    
# # Exercise 14. Reverse an integer number
# num =76542
# new_list=[]
# split = list(str(num))
# print(split)
# for i in reversed(split):
#     new_list.append(i)

# final=int("".join(new_list))
# print(final)
# print(type(final))
# print(type(new_list)) 
# #Exercise 15. Find largest and smallest digit in a number
# num = str(273491)
# largest_num=0
# smallest_num=int(num[0])
# print(type(num))
# for n in num:
#     for j in num:
#         n=int(n)
#         j=int(j)
#         if(n>j):
#             if(largest_num<n):
#                 largest_num=n
#         else:
#             if(smallest_num>n):
#                 smallest_num=n         
# print(largest_num)
# print(smallest_num)

# #Exercise 16. Check if a number is a palindrome
# number = str(121)
# reverse =""
# # print(type(number))
# for ch in reversed(number):
#     reverse+=ch

# if number==reverse:
#     print("yes")
# else:
#     print("No")

# # Exercise 17. Find factorial of a number
# num = 5
# factorial=1;
# for i in range(1,num+1):
#     factorial*=i
# print(factorial)

# #Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1
# # Practice Problem: The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. 
# # Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.
# n = 6
# res=[n]
# while n!=1:
#     if(n%2==0):
#         n=n//2  #round of the value will be floor(like math.floor(n/2) in js)
#         res.append(n)
#     else:
#         n=(n*3)+1
#         res.append(n)
# print(res)

# # Exercise 19. Armstrong Number Check
# num = str(153)
# value=0
# # print(type(num))
# num = 153
# num_str = str(num)
# power = len(num_str)
# total = 0

# for digit in num_str:
#     total += int(digit) ** power

# if total == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")

# #Exercise 20. Print right-angled triangle Number Pattern using a Loop

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ");
#     print()

# #Exercise 21. Print the decreasing pattern

# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

# # Exercise 22. Print the alternate numbers pattern

# for i in range(1,20,2):
#     print(i, end=" ")

# # Exercise 23. Print Alphabet pyramid (A, AB, ABC) pattern
# import string

# for i in range(1,6):
#     for ch in string.ascii_uppercase[:i]:
#         print(ch,end=" ")
#     print()

# #Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern
# # method1
# import string

# for i in range(5): #outer loop , which is for rows 
#     for ch in string.ascii_uppercase[i]: # to find the chr
#         for j in range(i+1): #how many the char will print , for columns
#             print(ch,end=" ")
#     print()

# #method2
# # print(chr(66)) #B
# rows = 5
# ascii_value = 65 # Starting with 'A'

# for i in range(rows):
#     # Calculate current letter
#     letter = chr(ascii_value + i)
#     # Print the letter (i + 1) times
#     for j in range(i + 1):
#         print(letter, end=" ")
#     print()

# #Exercise 24. Hollow square pattern

# for i in range(1,6):
#     for j in range(1,6):
#         if (i == 1 or i == 5) or (j == 1 or j == 5):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# #Exercise 25. Print pyramid pattern of stars

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# #Exercise 26. Print full multiplication table (1 to 10)
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end=" ")
#     print()

#Exercise 27. List Cumulative Sum: Each element is the sum of all previous
my_list=[1, 2, 3, 4]
res=[];
# Cumulative Sum: [1, 3, 6, 10]
# for value in my_list:
#     curr_value+=value
#     res.append(curr_value)
    
# print(res)
for i in range(len(my_list)): #3
    final=0
    for j in range(i+1):
        final+=my_list[j]
    res.append(final)
print(res)


# Exercise 1: List Comprehension Mastery

words = ["apple", "bat", "cherry", "dog", "elderberry"]

# Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']

cap_words=[fruit.upper() for fruit in words  if len(fruit)>4]
print(cap_words)

# Exercise 2: Dictionary Merging with Logic

dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

# Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}

dict_c=dict_a|dict_b   #union operator
dict_a.update(dict_b)
dict_d={**dict_a, **dict_b}
print(dict_a)
print(dict_c)
print(dict_d)

# Exercise 3: Frequency Map with Counter

text = "Python Programming"
dict_res={} #dictionary should not allow duplicate key 

for i in  text:
    count=0
    for j in text:
        if i==j and i !=" ":
            count+=1
    if count !=0:
         dict_res[i]=count

print(dict_res)

#method-2 
from collections import Counter 

def frq_map(text):
    clean_text=text.lower().replace(" ","")
    return Counter(clean_text)

print(frq_map("Python Programming"))

# Exercise 4: Anagram Checker
word1 = "listen".lower()
word2 = "silent".lower()

if sorted(word1)==sorted(word2): #sor the alphabetic order
    print("True")
else:
    print("False")
