# exception handling - Exception handling is a mechanism to catch runtime errors so the program does not terminate unexpectedly. Once an exception is caught,
#  we can decide what action to take—such as showing a custom message, using a default value, retrying the operation, logging the error, or continuing the program.


# basic syntax
# try:
#     # code that may raise an exception
# except ExceptionType1:
#     # code to handle ExceptionType1
# except ExceptionType2:
#     # code to handle ExceptionType2


#basic exception handling 

try:
    user_input =int(input("Enter a input:"))
    print(user_input)
except:
    print("value is not integer provide integer value...")
    try:
        try_again=int(input("Enter again input:"))
        print("You have entered correct input")
    except:
        print("chance are completed")
