# #hardcode the value
# num1=10  #value are harcoded 
# num2=20

# print(num1+num2)

# #getting input from user -> cons  -> input will asked to the user after program runned , here if we use scheducler means it will able to give manual input 
# num3=int(input("enter a num3 value: "))   # why int means in terminal the value is always comes as string so we here type casting 
# num4 = int((input("enter a num4 value: ")))

# print(num3+num4)

# import sys

# #handling input (sys.argv[]) 
# full_name = " ".join(sys.argv[1:]) #terminal act as array so we take input  1 st index and above  and join is convert array to string in js we arr.join(" ")

# print(full_name)
    
    
# #check the user input is string od number
# #checking type of the input -> note that the user input method always return string  
# num1=input("Enter a value:")
# print(type(num1))

# #function that convert input string as int and float 
# def check_user_input(input_val):
#     try:
#         val=int(input_val)
#         print(f"The given Input {val} is Interger")
#     except ValueError:
#         try:
#             val=float(input_val)
#             print(f"The give input {val} is float")
#         except ValueError:
#             print("The given value is String")
        
# input_val=input("Enter the value:")
# check_user_input(input_val)



# #checking the  number using string method called isdigit()
# val=input("Enter a number:")
# if val.isdigit():
#     print("The value is number")
# else:
#     print("The given value is string")
    
# #Only accept a number as input - when the user type number related and float related will be accept and stop the loop and otherwise it will run 
# while True:
#     input_val=input("Enter the value:")
#     try:
#         val=int(input_val)
#         print(f"The given Input {val} is Interger")
#         break;
#     except ValueError:
#         try:
#             val=float(input_val)
#             print(f"The give input {val} is float")
#             break;
#         except ValueError:
#             print("The given value is String")

# #Python take a list as input from a user
# # Using the Python input() function, we can directly accept strings, numbers, and characters from the user.
# # However, to take a list as input from a user, we need to perform some parsing on user input to convert it into a list        

# # How to Get a list of numbers as input from a user in Python

# #Example: Get a list of numbers as input from a user and calculate the sum of it
# values=input("Enter a list of numbers with:").split(" ")
# new_list=[]
# # print(values)
# for val in values:
#     new_value=int(val)
#     new_list.append(new_value)

# print(new_list)
# print(type(new_list))


# #Example:Input a list using input() and range() function in Python
# # number_list=[]
# # size=int(input("Enter the size of the list:"))

# # for i in range(0,size):
# #     val=int(input(f"Enter index {i} value:"))
# #     number_list.append(val)
# # print(number_list)

# #Example:Input a list using a list comprehension in Python
# size=int(input("Enter a size of thwe list:"))

# # new_list=list((2,3,4,5,6,7))
# # print(new_list)

# new_list=list(int(num) for num in input("Enter the value:").strip().split(" "))[:size] #We are running for loop to get user input and remove the white space , and split into array, now each value beace number and pass the number in the list() method to convert that into list again
# print(new_list)

# #Example:Input a list using the map function
# n=int(input("Enter the size of List:"))

# new_list=list(map(float,input("Enter a number:").strip().split()))[:n]
# print(new_list)

# #Example:Get a list of strings as input from a user
# family_name=input("Enter family member name follwed with witeSpace:").strip().split(" ")
# # family_name=list((input("Enter a name:"))) it will split into "n" "a" "v" "e" "e" "n"
# # print(family_name)

# for name in family_name:
#     print(name)

# #Example:Accept a nested list as input
# outer=[]
# size=int(input("Enter the size:"))

# for i in range(0,size):
#     new_list=list(map(int,input("Enter a List of number:").strip().split()))
#     outer.append(new_list)
    
# print(outer)

#Enter the inner list input line by line
outer=[]
outer_size=int(input("Enter the Outer list size:"))
inner_size=int(input("Enter inner list size:"))

for i in range(0,outer_size):
    inner=[]
    for j in range(0,inner_size):
        val=int(input(f"Enter {i} list of {j} value :"))
        inner.append(val)
    outer.append(inner)
    print("--------------")
print(outer)
    