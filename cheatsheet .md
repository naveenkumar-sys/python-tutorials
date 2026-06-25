1) What is an object in Python?
Very simple answer:

An object is a real usable value/thing in Python.

Examples:

10
"hello"
[1, 2, 3]
{"name": "Naveen"}

All of these are objects in Python.

So yes — object can be data/value.

x=10  #10 is object of class int 
print(type(10))

<class int>

That means:

10 is an object
its class/type is int

# ---------------------------
Final short memory note
Remember like this:
Class

design / blueprint / type

Object

actual thing / value / data created from class

Example
int → class
10 → object
str → class
"hello" → object
Student → class
s1 = Student("Naveen") → object

# ------------------------------


# Python Must-Remember Cheat Sheet

## 1) Number

### Type Conversion

* `int("10")` → `10`
* `float("10.5")` → `10.5`
* `str(100)` → `"100"`

### Important Number Functions

* `abs(-10)` → `10`
* `round(10.567, 2)` → `10.57`
* `pow(2, 3)` → `8`
* `max(10, 20, 30)` → `30`
* `min(10, 20, 30)` → `10`

### Important `math` Functions

```python id="vxkk3d"
import math
```

* `math.ceil(10.2)` → `11`
* `math.floor(10.9)` → `10`
* `math.sqrt(25)` → `5.0`
* `math.factorial(5)` → `120`
* `math.gcd(12, 18)` → `6`

### Must Remember

* `int(45.9)` → `45`
* `int("45")` works
* `int("45.7")` ❌ error
* `float("45.7")` works

---

## 2) String

### Important String Methods

* `upper()` → uppercase
* `lower()` → lowercase
* `strip()` → remove spaces from start/end
* `split()` → string → list
* `join()` → list → string
* `replace(old, new)` → replace text
* `find()` → position of character/word
* `count()` → number of occurrences
* `isdigit()` → check only digits
* `startswith()` / `endswith()`

### Examples

```python id="nqvjlwm"
name = "  naveen  "

print(name.strip())       # naveen
print(name.upper())       # NAVEEN
print("10 20 30".split()) # ['10', '20', '30']
print("-".join(['a','b'])) # a-b
```

### Must Remember

* Strings are **immutable** → cannot change a single character directly
* `"apple" * 2` → `"appleapple"`
* `"apple" + "2"` → `"apple2"`

---

## 3) List

### Important List Methods

* `append(x)` → add one item at end
* `extend([..])` → add multiple items
* `insert(index, value)` → add at specific position
* `remove(value)` → remove by value
* `pop()` / `pop(index)` → remove by index
* `clear()` → remove all
* `index(value)` → find index
* `count(value)` → count occurrences
* `sort()` → ascending sort
* `reverse()` → reverse list
* `copy()` → copy list

### Examples

```python id="rr1v8o"
nums = [1, 2, 3]
nums.append(4)       # [1,2,3,4]
nums.pop()           # removes last
nums.remove(2)       # removes value 2
nums.sort()
```

### Accessing List

* `nums[0]` → first item
* `nums[-1]` → last item
* `nums[1:4]` → slicing

### Looping

```python id="wpy98g"
for item in nums:
    print(item)

for i in range(len(nums)):
    print(nums[i])
```

### Must Remember

* List is **ordered**
* List is **mutable**
* Allows duplicates
* Access by **index**
* `range(len(list))` gives **indexes**, not values

---

## 4) Tuple

A tuple is similar to a list, but it is **immutable**.

```python id="n7v3fi"
data = (10, 20, 30)
```

### Important Points

* Ordered ✅
* Allows duplicates ✅
* Access by index ✅
* Immutable ❌ (cannot change after creation)

### Accessing Tuple

```python id="xv1s0v"
data = (10, 20, 30, 40)

print(data[0])    # 10
print(data[-1])   # 40
print(data[1:3])  # (20, 30)
```

### Important Tuple Methods

* `count(value)` → count occurrences
* `index(value)` → find position

### Example

```python id="t2x83e"
data = (10, 20, 20, 30)

print(data.count(20))   # 2
print(data.index(30))   # 3
```

### Must Remember

* Tuple uses **round brackets `()`**
* Good for fixed data that should not change
* Cannot use `append()`, `remove()`, `pop()`
* Faster than list in some cases

---

## 5) Set

A set stores **unique values only**.

```python id="u7vjlwm"
nums = {1, 2, 3}
```

### Important Set Methods

* `add(x)` → add one item
* `update([...])` → add multiple items
* `remove(x)` → remove item (error if not found)
* `discard(x)` → remove item safely
* `pop()` → remove a random item
* `clear()` → remove all

### Set Operations

* `set1.union(set2)` → combine all unique values
* `set1.intersection(set2)` → common values
* `set1.difference(set2)` → values in set1 not in set2

### Example

```python id="7v1chm"
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))         # {1,2,3,4,5}
print(a.intersection(b))  # {3}
print(a.difference(b))    # {1,2}
```

### Must Remember

* Set is **unordered**
* Set stores **unique values only**
* No indexing like `set[0]`
* Useful for removing duplicates

---

# Quick Comparison

## Number

* Used for calculations
* Learn: `int()`, `float()`, `abs()`, `round()`, `pow()`

## String

* Used for text
* Learn: `split()`, `join()`, `strip()`, `replace()`, `find()`

## List

* Ordered collection of values
* Learn: `append()`, `pop()`, `remove()`, `sort()`

## Tuple

* Ordered fixed collection
* Learn: indexing, slicing, `count()`, `index()`

## Set

* Collection of unique values
* Learn: `add()`, `remove()`, `union()`, `intersection()`

---

# Top 5 Must-Remember From Each

## Number

1. `int()`
2. `float()`
3. `abs()`
4. `round()`
5. `math.sqrt()`

## String

1. `split()`
2. `join()`
3. `strip()`
4. `replace()`
5. `isdigit()`

## List

1. `append()`
2. `pop()`
3. `remove()`
4. `sort()`
5. `for item in list`

## Tuple

1. `count()`
2. `index()`
3. indexing
4. slicing
5. immutability

## Set

1. `add()`
2. `remove()`
3. `discard()`
4. `union()`
5. `intersection()`






