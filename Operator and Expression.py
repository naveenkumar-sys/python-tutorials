#operator - opeartor is nothing but a special symbol or word that perform specific operation 

#1.Arithmatic opearator 
num1=10
num2=20

print(num1+num2) #add
print(num1-num2) #sub
print(num1*num2) #multiple
print(num2/num1) #divide to find quotient 
print(num2%num1) #divide to find remainder
print(num1**num2) # expotential which multiply num=10 => 10*10*10 = 1000
print(num1//num2) # floor(round of) the value by down nearest number 


#2.comparison operator

print(num1>num2) # return true if 1 > 2
print(num1<num2) # retun true if 1<2
print(num1==num2) # return true if 1==2
print(num1!=num2) #retrun true if 1 not equal to 2
print(num1>=num2) #retun true if 1 is greater that or equal to 2 
print(num1<=num2) #retun true if 1 is lesser that or equal to 2 

#3.Logical operator
print(num1 and num2) # return true if 1 and 2 is true
print(num1 or num2) # return true if any one is true
print(not num1) # retun true if num1 is false 

#4.assignment operator
x=10 # assign the value
x+=5 # add and assignt the value to same variable
x-=2 # sub and assign the value to same variable
x*=5 # mutlipy and assign the value to same variable
x/=2 # divide and assign the value to same variable

#5.membership operator 
z=[1,2,3,4,5]

print(6 in z) #retun true if the 6 in present in that z list otherwise false

#6.Indetity operator - check the two value are same by reference 
a=10
b=10
list1=[1,2]
list2=[1,2]

print ( a is b) # true coz both reference are equal 
print (list1 is list2) #  false coz value are same but reference address will be different 
print (list1 is not list2) # True coz is will check reference and not will false so true 

#7.Bitwise operator
# &   # AND
# |   # OR
# ^   # XOR&   # AND
# |   # OR
# ^   # XOR
# ~   # NOT
# <<  # Left Shift
# >>  # Right Shift
# ~   # NOT
# <<  # Left Shift
# >>  # Right Shift