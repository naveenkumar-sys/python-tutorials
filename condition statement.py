#conditional statements - whenever we want to check if this true we we enter if not we dont enter like real life secenario
#In signal - if green-> we go , if yellow - get ready , if red - stop

# signle if or else statement 
age=25
if(age>=18):
    print("you will enter")
else:
    print("you will not enter")

# elif statement 
men="no"
women="yes"

if(men=="yes"):
    print("you will  not enter")
elif(women=="yes"):
    print("you will Enter")
else:
    print("Not Allowed")

#if inside if (nested if) - suppose we have if true then check another condition
mark =12
attendance = 65

if(mark >=35):
    if(attendance>=75):
        print("pass")
    else:
        print("attendance is not enough")
else:
    print("mark is not enough")

# using logical operator to check multiple condition
current_recharge =349
current_internet ="1 gb"
if current_internet >= "1.5 gb" or current_recharge >=349:
    print("you have bonus offer")
else:
    print("you dont have any offer")


order_amount = 1000
order_day = "sunday"
is_member = "no"

# if order_amount >= 1000 and (order_day == "saturday" or order_day == "sunday") and is_member == "yes":
if order_amount>=1000 and order_day in ("saturday" , "sunday") and is_member == "yes":  #here in will check any like "is this value present in list/string/anyting in ja like includes() method"
    print("You will get coupon")
else:
    print("You are not valid for this coupon")
    
    