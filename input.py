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


# #here input is always right 
# name = input("enter your name:")
# print(type(name))

num5 =int(input("Enter a number1:"))
num6=float(input("Enter number2:"))

if num5 and num6:
    print(num5*num6)