# string = "hello how are you!"
# arr= string.split(" ")  #here splite same as js but join will differ  , split is used to convert array to string 
# print("".join(arr[0]))

# promo_code = "use Zomato100 to get off on your first order"

# code = "Zomato100"

# # splited_code = promo_code.split(" ")
# # print(splited_code)
# # for i in range(len(splited_code)):
# #     if(splited_code[i] == code ):
# #         print(i)

# if(code in promo_code):  #in will check whether the value is exist in collection  
#     print("yes")
    
# if(code is "Zomato100"): # is will check whether the given string is same or not , it check by reference 
#     print("yes")
# else:
#     print("No")
    
# #taking first name first letter and last name last letter
# name = "naveen kumar"
# # print(name.split(" "))
# first=name.split(" ")[0]  # this split will split as string with where is space
# last=name.split(" ")[1]
# # print(first)
# # print(last)
# f_letter = list(first)[0].upper() # in js we use spit("") but here we use list(name)
# l_letter = list(last)[0].upper()
# print(f_letter)
# print(l_letter)


name = "naveen kumar"
#lower()
print(name.lower())
# upper()
print(name.upper())
#3.titlecase - change first character every word into capital
print(name.title())
#capitalize() - only first letter will change in capital
print(name.capitalize())
# strip() - act like trim() in js , remove unwanted white spaces
print(name.strip())
# split() - change string into list(array)
print(name.split(" "))
# join() - change list into string
print("".join(name))
# replace() - replace old word into new word 
print(name.replace("naveen","Naveen"))
# startswith() - return true if the given word is startswith or else return false
print(name.startswith("naveen"))
# endswith() - return true if the given word is endswith or else return false
print(name.endswith("kumar")) 
# find() - find the first position of the word or character
print(name.find("a"))
# count() - count the char or word of occurence in the string
print(name.count("k"))
#isalpha() - check only has character in the string
print("Naveen".isalpha())
#isdigit() - check if the given string is digit 
print("123".isdigit())
#isalnum() - check the string consist of number and char
print("Naveen123".isalnum())



