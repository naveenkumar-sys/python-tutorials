#function - block of code that is executed only when it is called , it can be reused many times
#Example 3: Sum of numbers from 1 to n using recursion

# def sum(n):
#     if(n==1):
#         return 1
#     return n + sum(n-1) 
# print(sum(4))

# def total(n):
#     if n == 1:
#         return 1
#     return n + total(n - 1)

# print(total(5))
total=0
def t(n):
    # print(total)
    global x
    total+=n

print(total,"hello")    
for i in range(1,6):
    t(i)  

