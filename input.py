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
    
#Only accept a number as input - when the user type number related and float related will be accept and stop the loop and otherwise it will run 
while True:
    input_val=input("Enter the value:")
    try:
        val=int(input_val)
        print(f"The given Input {val} is Interger")
        break;
    except ValueError:
        try:
            val=float(input_val)
            print(f"The give input {val} is float")
            break;
        except ValueError:
            print("The given value is String")
        


