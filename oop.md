# Python OOP - Class & Object (Complete Beginner Notes)

---

# 1. Why OOP?

Without OOP, we write separate variables and functions.

```python
name = "Naveen"
age = 22

def show(name, age):
    print(name, age)
```

This works for small programs.

But imagine:

* 100 students
* 50 functions
* Thousands of lines of code

It becomes difficult to organize and maintain.

## OOP Solution

OOP groups **related data** and **related functions** together.

---

# 2. What is a Class?

A **Class** is a **Blueprint** or **Template**.

It defines:

* What data an object should have (Attributes)
* What actions an object can perform (Methods)

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(self.name, "is studying")
```

A class itself stores **no actual student data**.

It only defines how every student should look.

---

# 3. What is an Object?

An **Object** is the actual thing created from a class.

```python
s1 = Student("Naveen", 22)
```

Here,

```
Student  → Class

s1       → Object (Instance)
```

The object stores actual values.

```
s1
------------
name = Naveen
age  = 22
```

---

# 4. Class vs Object

## Class

Blueprint of a house

```
House Blueprint

2 Bedrooms
1 Kitchen
1 Hall
```

No real house exists.

---

## Object

Actual house built using that blueprint.

```
House 1

2 Bedrooms
1 Kitchen
1 Hall
```

Exactly the same in Python.

```
Student Class

↓

Student Object 1
Student Object 2
Student Object 3
```

One class can create many objects.

---

# 5. Constructor (**init**)

Whenever you create an object,

```python
s1 = Student("Naveen",22)
```

Python automatically calls

```python
__init__()
```

Conceptually Python behaves like

```python
Student.__init__(s1,"Naveen",22)
```

So

```
self = s1
```

Then

```python
self.name = name
```

becomes

```python
s1.name = "Naveen"
```

The constructor stores data inside the object.

---

# 6. What is self?

`self` simply refers to **the current object**.

Example

```python
class Student:

    def show(self):
        print(self.name)
```

Calling

```python
s1.show()
```

Internally behaves like

```python
Student.show(s1)
```

So

```
self = s1
```

Then

```python
self.name
```

means

```python
s1.name
```

---

# 7. How Method Calls Work

Suppose

```python
student.study()
```

Python internally behaves approximately like

```python
Student.study(student)
```

The object is automatically passed as **self**.

You never pass `self`.

Python does it automatically.

---

# 8. Built-in Classes

Python already provides many classes.

Examples

```
int
str
list
dict
tuple
set
float
bool
```

These classes were written by Python developers.

You simply use them.

---

# 9. Built-in Object Creation

When you write

```python
x = 10
```

Python automatically creates an object.

Conceptually

```python
x = int(10)
```

Now

```
10

↓

Object of int class
```

You didn't explicitly create the object.

Python created it.

---

Another example

```python
name = "Python"
```

Conceptually

```python
name = str("Python")
```

---

List example

```python
nums = [1,2,3]
```

Conceptually

```python
nums = list([1,2,3])
```

Python hides these details from us.

---

# 10. User-defined Classes

Unlike built-in classes,

you create the object yourself.

Example

```python
s1 = Student("Naveen",22)
```

Here,

You explicitly created the object.

---

# 11. Built-in Methods

Example

```python
name.upper()
```

Python sees

```
name

↓

Object of str class
```

Then it finds

```
upper()
```

inside

```
str class
```

and executes it.

---

Another example

```python
nums.append(5)
```

Python sees

```
nums

↓

Object of list class
```

Then finds

```
append()
```

inside

```
list class
```

---

# 12. append() Parameters

Suppose

```python
nums.append(5)
```

Internally Python behaves approximately like

```python
list.append(nums,5)
```

Method definition

```python
def append(self,value):
```

Therefore

```
self  = nums
value = 5
```

---

# 13. Built-in Function vs Method

## Built-in Functions

```python
len(nums)
print(nums)
type(nums)
sum(nums)
```

Notice

```
No dot (.)
```

These belong to Python itself.

---

## Methods

```python
nums.append(5)

name.upper()

student.study()
```

Notice

```
Uses dot (.)
```

Methods belong to a class.

---

# 14. Module vs Method

## Module

```python
import math

math.sqrt(25)
```

```
math

↓

Module
```

`sqrt()` is a function inside the module.

---

## Method

```python
name.upper()
```

```
name

↓

Object

↓

Method of str class
```

---

# 15. Important Rule

Whenever you see

```python
object.method()
```

Python thinks

```
1. Which class does this object belong to?

↓

2. Find the method inside that class.

↓

3. Automatically pass this object as self.

↓

4. Execute the method.
```

---

# 16. Everything is an Object

In Python,

Everything is an object.

```
10

↓

Object of int class
```

```
"Python"

↓

Object of str class
```

```
[1,2,3]

↓

Object of list class
```

```
{"name":"Naveen"}

↓

Object of dict class
```

```
Student("Naveen")

↓

Object of Student class
```

Every object belongs to some class.

---

# 17. Built-in Classes vs User-defined Classes

## Built-in Classes

Created by Python.

Examples

```
int
str
list
dict
```

Objects are created automatically.

```python
x = 10
```

Python internally creates

```
Object of int class
```

---

## User-defined Classes

Created by the programmer.

Example

```python
class Student:
    ...
```

Objects are created explicitly.

```python
s1 = Student("Naveen")
```

---

# 18. Summary Table

| Concept            | Meaning                                                 |
| ------------------ | ------------------------------------------------------- |
| Class              | Blueprint / Template                                    |
| Object             | Actual thing created from a class                       |
| Instance           | Another name for object                                 |
| Attribute          | Data stored inside an object                            |
| Method             | Function inside a class                                 |
| self               | Current object                                          |
| **init**()         | Constructor (runs automatically when object is created) |
| Built-in Class     | Created by Python (`int`, `str`, `list`)                |
| User-defined Class | Created by Programmer                                   |
| Built-in Function  | `len()`, `print()`, `type()`                            |
| Method             | `append()`, `upper()`, `pop()`                          |

---

# 19. Final Mental Model

```
                    CLASS
          (Blueprint / Template)

             Attributes
         (name, age, mark)

                 +

              Methods
        (show(), study())

                    │
                    ▼

       student = Student("Naveen",22)

                    │
                    ▼

           OBJECT (Instance)

          name = "Naveen"
          age  = 22

                    │
                    ▼

          student.show()

Python internally behaves like

Student.show(student)

↓

self = student

↓

print(self.name)

↓

Naveen
```

---

# One-Line Memory Notes

* Class → Blueprint
* Object → Actual thing
* Instance → Same as Object
* self → Current object
* Method → Function inside class
* Constructor → Initializes object data
* Built-in Classes → Python creates objects automatically
* User-defined Classes → Programmer creates objects explicitly
* Built-in Functions → No dot (`len()`, `print()`)
* Methods → Use dot (`append()`, `upper()`)
