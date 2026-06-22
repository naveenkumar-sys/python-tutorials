# #Numeric data type as three type 
# #1.Int - integer either [postive or negative]
# a=10
# print(a)
# print(type(a))

# val=int("10")
# print(val)
# print(type(val))

# #2.float - decimal value [positive or negative]

# b=34.66
# print(type(b))

# b1=float("67.88")
# print(type(b1))

# #3.complex-mixed wiht digit and number simply imaginary value
# num=5+9j
# print(num)
# print(type(num))

# c=complex(5,9)
# print(type(c))

# #4type casting
# #1.implicit type casting -automatic by doing operation
# a=24
# b=34.55
# c=a+b
# print(c)
# print(type(c))
# #2.explicit type casting - manually we change the type
# num2=float(46) 
# print(num2)

# print(str(100) + str(20))
# print(int(float("45.99")))
# print(bool(0))
# print(bool(1))

# print(bool("")) #false
# print(bool(" ")) #True
# print(int("0010"))
# print(bool("False")) #True


# Math module method in numeric data type 
# #1.Math.ceil and Math.floor  
# import math as m

# a = 1.4
# print(m.ceil(a)) #round off near greatest value
# print(m.floor(a)) #round off near smallest value

# #2.degree() and radian()
import math
# pi=math.pi
# print(pi)

# #degree of pi
# print("Degree of pi is:",math.degrees(pi))

# #radian od 90 degree
# print("The radian od 90 degres is:",math.radians(90))

# #factorial
# import math 
# a=5
# print(math.factorial(a))

#Fabs and tranc
#Fabs-float absolute value , give value as floating absolute value and remove negative sign
print(math.fabs(10))
print(math.fabs(-34))

#trunc-transcate the value and trunc() -> Remove decimal part
print(math.trunc(4.367)) #round off the value

#pow-find power of the value , it expect two parameter
val=math.pow(2,3) #for finding power
print(math.trunc(val)) #round of the value 
#log-TO find log of the given number
print(math.log(3))
#isfinite() -> check the number is finite or not -> if finit it return true if not finite it return false 
print(math.isfinite(45))
#isinf ->check the value is infinite or not -> if infinit it return true if not infinite it return false 
print(math.isinf(43)) 

#checking whether it is a number or not  -> return true is not a number and return false if it is number 
print("IS a number or not::", math.isnan(math.nan)) #true
print("IS a number or not::", math.isnan(5)) #false

# math.isclose()

# isclose() is used to check whether two numbers are almost equal.

# Why do we need it?

# Because floating-point numbers sometimes have tiny precision errors.

print(math.isclose(0.2+0.10, 0.3))

# Square root, GCD, Power, and Exponentials of a Number
#finding sqrt
print("The square root of 25 is ::", math.sqrt(25))
print("The square root of 10 is ::", math.sqrt(10))

#Greatest Common Divisor
print("The greatest common divisor is ::", math.gcd(6,12))

#exponential value
print("The value os e(x) is::", math.exp(-2))

#Number raised to power
print("The value of 9^3 is ::", math.pow(9, 3))


#finding max value - max() find the maximum value 
print(max(1,2,3,4,5))
#finding min value - min() find the minimum value
print(min(1,2,3,4,5))
#round of the value - round() round of the value
print(round(4.7))
#abs value - abs() find the absolute value and if negative then remove the negative sign
print(abs(-5))