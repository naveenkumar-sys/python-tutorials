# List comprehension
# [expression for item in iterable if condtion]

# Dictionary comprehension
# {key: value for item in iterable if codition}

# both are will used in list and dict inside 


#1. Create a list of squares from 1 to 5
new_list=[i*i for i in range(1,6)]
print(new_list)

#2. Create a list of even numbers from 1 to 10
even_list=[i for i in range(1,11) if i%2==0]
print(even_list)

#3. From this list, create a new list with all values multiplied by 2
nums = [1, 2, 3, 4]
multy_list=[i*2 for i in nums]
print(multy_list)
#4. From this list, keep only strings with length greater than 4
words = ["apple", "cat", "banana", "dog", "orange"]
string_list=[val for val in words if len(val)>4]
print(string_list)
#5. Convert all words to uppercase
words = ["python", "java", "django"]
upper=[val.upper() for val in words]
print(upper)

#Dictionary comphrension
#6. Create a dictionary where key is number and value is square
new_dict={i:i*i for i in range(1,6)}
print(new_dict)
#7. Create a dictionary where key is number and value is cube
cube_dict={i:i**3 for i in range(1,5)}
print(cube_dict)
#8. From this list, create a dictionary with word as key and length as value
words = ["apple", "dog", "banana"]
new2_list={val:len(val) for val in words}
print(new2_list)
#9. Create a dictionary from numbers 1 to 5, but only include even numbers
even_dict={i:i*i for i in range(1,6) if i%2==0}
print(even_dict)
#10. From this list, create a dictionary where key is word and value is uppercase word
words = ["red", "blue", "green"]
upper_dict={val:val.upper() for val in words}
print(upper_dict)

#11. From this list, create:
# a) A list of lengths
words = ["apple", "cat", "banana"]
length=[len(i) for i in words]
print(length)
# b) A dictionary of word → length
length_dict={val:len(val) for val in words}
print(length_dict)