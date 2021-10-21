# PythonDevelopment

#### Command Line Interface - Mac
* python3
* python3 -m pip install requests

#### Mutability
* Whether data value contained can be changed

## Basic Data Types
1. Boolean
    * bool
    * immutable
    * True/False
    * Primitive data structure
2. Integer
    * int
    * immutable
    * 3
    * Primitive data structure
3. Floating Point
    * float
    * immutable
    * 3.45
    * Primitive data structure
4. Complex
    * complex
    * immutable
    * 5 - 3j
5. Text String
    * str
    * immutable
    * 'test string'
    * Primitive data structure
6. List
    * list
    * **mutable**
    * [2, 4, 8]
    * list([2, 4, 8])
        * list() function takes one argument
    * In-built non-primitive data structure
7. Tuple
    * tuple
    * immutable
    * (2, 4, 8)
    * tuple([2, 4, 8])
        * tuple() function takes one argument
    * In-built non-primitive data structure
8. Bytes
    * bytes
    * immutable
    * b'ab/xff'
    * In-built non-primitive data structure
9. ByteArray
    * bytearray
    * **mutable**
    * bytearray(...)
    * In-built non-primitive data structure
10. Set
    * set
    * **mutable**
    * {2, 4, 8}
    * set([2, 4, 8])
        * set() function takes one argument
    * In-built non-primitive data structure
    * Does not allow duplicates of elements
    * Unordered and not indexed
    * Perform following functions:
        * Union |
        * Intersection &
        * Differences -
        * Symmetrical differences ^
```python
# Union
x = {2, 4, 8}
y = {3, 5, 8}
xy = x | y
print(xy)
#{2, 3, 4, 5, 8}
```
```python
# Intersection
x = {2, 4, 8}
y = {3, 5, 8}
xy = x & y
print(xy)
#{8}
```
```python
# Differences
x = {2, 4, 8}
y = {3, 5, 8}
xy = x - y
yx = y - x
print(xy)
#{2, 4}
print(yx)
#{3, 5}
```
```python
# Symmetrical Differences
x = {2, 4, 8}
y = {3, 5, 8}
xy = x ^ y
print(xy)
#{2, 3, 4, 5}
```
11. Frozen Set
    * frozenset
    * immutable
    * frozenset([2, 4, 8])
    * set which cannot be changed
    * In-built non-primitive data structure
12. Dictionary
    * dict
    * **mutable**
    * {'game': 'bingo', 'dog': 'dingo'}
    * dict([('game', 'bingo',), ('dog', 'dingo')])
        * dict() function takes one argument
    * {key: value, key: value}
    * Unordered collection with key and value elements
    * In-built non-primitive data structure

## Integer operations
* \+ addition
* \- subtraction
* \* multiplication
* / floating-point division
```python
x = 7/2
print(x)
#3.5
```
* // integer (truncating) division
```python
x = 7//2
print(x)
#3
```
* % modulus (remainder)
```python
x = 7%3
print(x)
#1
```
* \*\* exponentiation

### Variable Name Conditions
* lowercase letters (a-z)
* uppercase letters (a-z)
* digits (0-9)
* underscore (_)
* case sensitive
* cannot begin with digit
* Python has reserved words (e.g. continue)

### Libraries
```Python
import webbrowser
import json
from urllib.request import urlopen
```
* Import all code from the Python standard library module called *webbrowser* and *json*
* Import only the urlopen function from the standard library module *urllib.request*

### Comments
* create comments with #
```python
# this is a comment line
```
* no multi-line comment within python

## if, elif, else Comparisons
* checks whether condition is a boolean **TRUE** value
* Python expects consistent spacing (tab, space, etc.)
```python
if TRUE:
    print("statement is true")
else:
    print("statement is false")
```
```python
if TRUE:
    print("statement is true")
elif TRUE:
    print("second statement is true")
else:
    print("statement is false")
```

### Comparison Operators
* equality ==
* inequality !=
* less than <
* less than or equal <=
* greater than >
* greater than or equal >=

### Multiple Comparisons
* and
* or
* not

### Considered FALSE
* boolean FALSE
* null None
* zero integer 0
* zero float 0.0
* empty string ''
* empty list []
* empty tuple ()
* empty dict {}
* empty set set()

### Membership Operator In
* using *in* to determine comparison within data object
```python
vowels = 'aeiou'
letter = 'o'
letter in vowels
#TRUE
```

## Text Strings
* Enclosed single of double quotes
    * ''
    * ""
* Allows to place quotes within strings
```python
print("'Nay!'")
#'Nay!'
```
* Use three single or double quotes for multiline stings
```python
x = """test multiline
string"""
print(x)
#test multiline
#string
```
* Difference between print() and automatic echoing
    * print() strips quotes from strings and prints their contents. Meant for human output
    * Interactive interpreter prints the string with quotes and escape characters \n
```python
x = 'hello world'
print(x)
#hello world
x
#'hello world'
```
* String conversion > str()
```python
str(98.6)
#'98.6'
```
* \n > new line
```python
palindrome = 'A man, \nA plan, \nA canal'
print(palindrome)
#A man,
#A plan,
#A canal
```
* \t > tab
```python
print('a\tbc')
#a   bc
```
* Combine strings by using +
```python
'Release the kraken! ' + 'No, wait!'
#'Release the Kraken! No wait!'
```
* Duplicate strings with *
```python
start = 'Na '*4 + '\n'
middle = 'Hey '*3 + '\n'
end = 'Goodbye'
print(start + middle + end)
#Na Na Na Na
#Hey Hey Hey
#Goodbye
```
* Get character with []
    * Members go from 0 to length -1
```python
letters = 'aeiou'
letters[0]
#'a'
letters[-1]
#'u'
letters[3]
#'o'
```
* Get substring with slice [:]
    * [*start* : *end* : *step*]
```python
letters = 'aeiou'
# three last characters
letters[-3:]
#'iou'
# every second character
letters[::2]
#'aiu'
```
* Get length with len()
```python
letters = 'aeiou'
len(letters)
#5
```
* Combine by using join()
    * Collapses a list of strings into a single string
    * *string.join(list)*
```python
letters = ['a', 'e', 'i', 'o', 'u']
newStr = ''.join(letters)
print(newStr)
#aeiou
secStr = ' '.join(letters)
print(secStr)
#a e i o u
```
* Substitute by using replace()
    * *string.replace(old substring, new substring, instances)*
    * If no instance count, replaces all instances
    * Does not change initial string (immutable)
```python
setup = 'a duck goes into a bar'
setup.replace('duck', 'cow')
#'a cow goes into a bar'
setup
'a duck goes into a bar'
```
* Strip with strip()
    * *strip()*, *lstrip()*, *rstrip*
    * Common to strip ' ', '\t', '\n'
```python
world = '    earth    '
world.strip(' ')
#'earth'
world.lstrip(' ')
#'earth    '
world.rstrip(' ')
#'    earth'
```
* Search and select
    * *find()*, *rfind()*, *index()*, *rindex()*, *startswith()*, *endswith()*
    * If substring cannot be found, find() returns -1 and index() raises an exception
    * If found, returns character count to substring
```python
poem = 'this is a poem sentence poem'
poem.find('poem')
#10
poem.rfind('poem')
#24
```
* Capitalize strings
    * *string.capitalize()*, *string.title()*, *string.upper()*, *string.lower*, *string.swapcase()*
    * These functions take no arguments
* Alignment
    * Layout alignment functions
    * Center *string.center()*
    * Left justify *string.ljust()*
    * Right justify *string.rjust()*
```python
setup = 'a duck goes into a bar'
setup.center(30)
#'    a duck goes into a bar    '
setup.ljust(30)
#'a duck goes into a bar        '
setup.rjust(30)
#'        a duck goes into a bar'
```
* f-strings formatting
    * letter f or F directly in front of initial quote
    * Include variable names and expressions within curly brackets {} to get their value in string
    * Can include expressions (*variable*:)
        * Option to include fill character (default ' ') to pad the value string if it's shorter than minwidth
        * Option alignment left < (default), right >, center ^
```python
name = 'Hector'
f'{name} says hello'
#'Hector says hello'
f'{name.lower()} says hello'
#'hector says hello'
f'{name:10} says hello'
#'Hector     says hello'
f'{name:!>10} says hello'
#'!!!!Hector says hello'
```
## For and While Loops
## While Loops
* Continue as long as condition is met
```python
count = 1
while count <= 5:
    print(count)
    count += 1
#1
#2
#3
#4
#5
```
* Cancel with **break**
    * To loop until something occurs, but not sure when that will happen, create infinite loop with break statement
```python
while True:
    stuff = input('String to capitalize [type q to quit]: ')
    if stuff == 'q':
        break
    print(stuff.capitalize())
#String to capitalize [type q to quit]: hello
#Hello
#String to capitalize [type q to quit]: q
```
* Skip ahead with **continue**
    * When you don't want to break the loop, but to just skip to next iteration
```python
while True:
    value = input('Integer, please [q to quit]: ')
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, 'squared is', number*number)
#Integer, please [q to quit]: 1
#1 squared is 1
#Integer, please [q to quit]: 2
#Integer, please [q to quit]: q
```
* Check break use with **else**
    * If while loop ends normally (no break call), control passes to an optional **else**
```python
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: #no break called
    print('No even number found')
#No even number found
```
## Iterate with For and In
* Explicitly define iteration sequence using **for**
```python
word = 'thud'
for letter in word:
    print(letter)
#t
#h
#u
#d
```
* Cancel with **break**
    * break in a for loop breaks out of the loop before defined iterations are complete
```python
word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)
#t
#h
```
* Skip to **continue** and check break with **else**
* Leverage number sequences with range()
    * *range(start, stop, step)*
    * If *start* is omitted, range begins at 0
    * *Stop* is the only required value
    * Default value for *step* is 1, but you can go backward with -1
```python
for x in range(0,3):
    print(x)
#0
#1
#2
```
```python
for x in range(2, -1, -1):
    print(x)
#2
#1
#0
```
```python
list = [2, 4, 8]
for x in range(len(list)):
    print(list[x])
#2
#4
#8
```
## Tuples and Lists
### Tuples
* Create with commas and ()
* *('Groucho')* is considered a string. Need to include comma to make it a tuple > ('Groucho',)
```python
empty_tuple = ()
#()
one_marx = ('Groucho',)
#('Groucho',)
marx_tuple = ('Groucho', 'Chico', 'Harpo')
#('Groucho', 'Chico', 'Harpo')
```
* Tuples allow you to assign multiple variables at once (unpacking)
```python
marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
a
#'Groucho'
b
#'Chico'
c
#'Harpo'
```
* Convert a list into a tuple using *tuple()*
```python
marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)
#('Groucho', 'Chico', 'Harpo')
```
* Combine tuples using *+*
```python
('Groucho',) + ('Chico', 'Harpo')
#('Groucho', 'Chico', 'Harpo')
```
* Duplicate items with *
```python
('yada',) * 3
#('yada', 'yada', 'yada')
```
* Can compare as well as iterate with for and in
* You cannot modify a tuple! Tuples are immutable
    * You can't change the existing object
    * You can create a new object and concatenate tuples
```python
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
id(t1)
#4409105136
t1 += t2
id(t1)
#4408702160
```
### Lists
* Create with []
    * Tracks objects by their order
    * Lists are mutable and can change
    * Same value can occur more than once in a list
```python
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
first_names = ['John', 'Terry', 'Terry', 'Michael']
```
* Create or convert with *list()*
* list() converts other iterable data types to lists
```python
list('cat')
#['c', 'a', 't']
list(['cat'])
#['cat']
```
* Create lits from string using *split()*
```python
date = '9/19/2019'
date.split('/')
#['9', '19', '2019']
```
* Get item by *[offset]*
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0]
#'Groucho'
marxes[1]
#'Chico'
marxes[2]
#'Harpo'
marxes[-1]
#'Harpo'
marxes[-2]
#'Chico'
marxes[-3]
#'Groucho'
```
* Get items with *slice*
* [*start*:*end*:*steps*]
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[:2]
#['Groucho', 'Chico']
marxes[::-2]
#['Harpo', 'Groucho']
marxes[::-1]
#['Harpo', 'Chico', 'Groucho']
```
* Difference between *list[::-1]* and *list.reverse()*
    * reverse() function changes the list but doesn't return the value
* Add an item to the end with *append()*
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
marxes
#['Groucho', 'Chico', 'Harpo', 'Zeppo']
```
* Add an item by offset with *insert()*
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
marxes
#['Groucho', 'Chico', 'Gummo', 'Harpo']
```
* Combine lists by using *extend()* or *+*
```python
marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes.extend(others)
marxes
#['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']

marxes = ['Groucho', 'Chico', 'Harpo']
others = ['Gummo', 'Karl']
marxes += others
marxes
#['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
```
* Change an item by *[offset]*
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
marxes
#['Groucho', 'Chico', 'Wanda']
```
* Change items with a slice
```python
numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
numbers
#[1, 8, 9, 4]
```
* Delete an item by offset with *del* before reference
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Karl']
del marxes [-1]
marxes
#['Groucho', 'Chico', 'Harpo']
```
* Delete an item by value with *remove()*
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Karl']
marxes.remove('Karl')
marxes
#['Groucho', 'Chico', 'Harpo']
```
* Get an item by offset and delete it with *pop()*
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop()
#'Zeppo'
marxes
#['Groucho', 'Chico', 'Harpo']
marxes.pop(1)
#'Chico'
marxes
#['Groucho', 'Harpo']
```
* LIFO (last in first out) - using *append()* and *pop()*
    * Also referred to as **Stack**
    * append() adds value to end of list
    * pop() removes value from end of list
* FIFO (first in first out) - using *append()* and *pop(0)*
    * Also referred to as **Queue**
    * append() adds value to end of list
    * pop(0) removes value from beginning of list
* Delete all items with *clear()*
```python
work_quotes = ['Working hard', 'Quick question', 'Number one']
work_quotes.clear()
work_quotes
#[]
```
* Find an item's offset by value with *index()*
    * If there are multiple values, index() returns the first value
```python
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.index('Chico')
#1
simpsons = ['Lisa', 'Bart', 'Marge', 'Homer', 'Bart']
simpsons.index('Bart')
#1
```
* Test for a value with *in*
```python
marxes = ['Groucho', 'Chico', 'Harpo']
'Groucho' in marxes
#True
'Bob' in marxes
#False
```
* Count occurrences of a value with *count()*
```python
marxes = ['Groucho', 'Chico', 'Harpo', 'Groucho']
marxes.count('Groucho')
#2
marxes.count('Bob')
#0
```
* Reorder items with *sort()* or *sorted()*
    * List method sort() sorts the list itself, in place
    * function sorted() returns a sorted **copy** of the list
```python
marxes = ['Groucho', 'Chico', 'Harpo']
sorted(marxes)
#['Chico', 'Groucho', 'Harpo']
marxes.sort()
marxes
#['Chico', 'Groucho', 'Harpo']
```
* Get length with *len()*
```python
marxes = ['Groucho', 'Chico', 'Harpo']
len(marxes)
#3
```
* Assign with =
    * Changing the list in one place also changes in the other
```python
a = [1, 2, 3]
b = a
b
#[1, 2, 3]
a[0] = 'surprise'
a
#['surprise, 2, 3]
b
#['surprise', 2, 3]
```
* Create independent copy using *copy()*, *list()*, or slice
    * This does not factor for imbedded lists
```python
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 0
a
#[0, 2, 3]
b
#[1, 2, 3]
c
#[1, 2, 3]
d
#[1, 2, 3]
```
* Create independent copy of everything with *deepcopy()*
```python
a = [1, 2, [8, 9]]
b = a.copy()
a[2][0] = 10

a = [1, 2, [10, 9]]
a
#[1, 2, [10, 9]]
b
#[1, 2, [10, 9]]

import copy as c
a = [1, 2, [8, 9]]
c = c.deepcopy(a)

a = [1, 2, [10, 9]]
a
#[1, 2, [10, 9]]
c
#[1, 2, [8, 9]]
```
* Create a list with a comprehension
    * [expression for item in iterable]
    * [expression for item in iterable if condition]
```python
numberList = [number for number in range(1, 6)]
numberList
#[1, 2, 3, 4, 5]

aList = [number for number in range(1, 6) if number % 2 ==1]
aList
#[1, 3, 5]

rows = [num for num in range(1, 4)]
cols = [num for num in range(1, 3)]
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
        print(cell)
#(1, 1)
#(1, 2)
#(2, 1)
#(2, 2)
#(3, 1)
#(3, 2)

for row, col in cells:
    print(row, col)
#1 1
#1 2
#2 1
#2 2
#3 1
#3 2
```
* Tuples versus lists
    * Tuples cannot be modified (append(), insert(), etc.) after creation (immutable)
    * Tuples use less space
    * You can't clobber tuple items by mistake
    * You can use tuples as dictionary keys
    * Named tuples can be a simple alternative to objects`
## Dictionaries and Sets
### Dictionaries
* Specify unique *key* to associate with each *value*
* Create with *{}*
```python
empty_dict = {}
empty_dict
#{}

bierce = {
    'day': 'A period of twenty-four hours, mostly misspent',
    'positive': 'Mistaken at the top of ones voice',
    'misfortune': 'The kind of fortune that never misses'
}
bierce
#{'day': 'A period of twenty-four hours, mostly misspent', 'positive': 'Mistaken at the top of ones voice', 'misfortune': 'The kind of fortune that never misses'}
```
* Create with *dict()*
    * Limitation of this method is the argument names need to be legal variable names (no spaces, no reserved words)
```python
acme_customer = dict(first='Wile', middle='E', last='Coyote')
acme_customer
#{'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
```
* Convert with *dict()*
```python
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
dict(lol)
#{'a': 'b', 'c': 'd', 'e': 'f'}

los = ['ab', 'cd', 'ef']
dict(los)
#{'a': 'b', 'c': 'd', 'e': 'f'}
```
* Add or change an item by *[key]*
```python
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric'
}
pythons['Gilliam'] = 'Gerry'
pythons['Idle'] = 'Terry'
pythons
#{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Terry', 'Gilliam': 'Gerry'}
```
* Get an item by *[key]* or with *get()*
    * If the key is not present in the dictionary, using *[key]* will return error
    * Avoid error by using *in* or *get()*
    * *get(key to search, displayed message if not returned)*
    * If no message is provided with *get()* and key is not present in dict, then method returns **None**
```python
pythons['Chapman']
#'Graham'

'hector' in pythons
#False

pythons.get('hector', 'No value')
#'No value'
```
* Get all keys with *keys()*
    * Python3 returns dict_keys() which is an iterable view
    * Does not create and store a list
    * To create a store a list, use *list(dict.keys())*
```python
signals = {
    'green': 'go',
    'yellow': 'go faster',
    'red': 'stop'
}
signals.keys()
#dict_keys(['green', 'yellow', 'red'])

list(signals.keys())
#['green', 'yellow', 'red']
```
* Get all values with *values()*
```python
list(signals.values())
#['go', 'go faster', 'stop']
```
* Get all key-value pairs with *items()*
```python
list(signals.items())
#[('green', 'go'), ('yellow', 'go faster'), ('red', 'stop')]
```
* Get length with *len()*
    * Counts number of keys
```python
len(signals)
#3
```
* Combine dictionaries with *{**a, **b}*
    * Can pass more than two dictionaries *{**a, **b, **c}*
    * If both dictionaries have the same key, the value from the second dictionary wins
```python
first = {
    'a': 'agony',
    'b': 'bliss'
}
second = {
    'b': 'bagels',
    'c': 'candy'
}

{**first, **second}
#{'a': 'agony', 'b': 'bagels', 'c': 'candy'}
```
* Combine dictionaries with *update()*
    * Copies the keys and values from one dictionary to the other
    * If both dictionaries have the same key, the value from the second dictionary wins
```python
first.update(second)
first
#{'a': 'agony', 'b': 'bagels', 'c': 'candy'}
```
* Delete an item by key with *del*
```python
del first['a']
first
#{'b': 'bagels', 'c': 'candy'}
```
* Get an item by key and delete it with *pop()*
    * Combines *get()* and *del*
    * If key exists, it returns the matching value and deletes the key-value pair
    * If key doesn't exist, it raises an exception
```python
first.pop('b')
#'bagels'
first
#{'c': 'candy'}
```
* Delete all items with *clear()*
```python
pythons.clear()
pythons
#{}
```
* Assign with *=* versus copy with *copy()*
    * As with lists, assign with *=* will reflect any changes made to original dict
    * With *copy()*, a separate ID is created
```python
test1 = {
    'a': 'hand',
    'b': 'made'
}

test2 = test1
id(test1)
#4413656192
id(test2)
#4413656192

test3 = test1.copy()
id(test3)
#4413656512
```
* Copy everything with *deepcopy()*
* Compare dictionaries with *==*
    * Python compares the keys and values one by one. If a key's value is not the same, returns *False*
```python
a = {1: [1, 2], 2: [1], 3: [1]}
b = {1: [1, 1], 2: [1], 3: [1]}
a == b
#False
```
* Iterate with *for* and *in*
    * Can iterate over the keys *keys()*, values *values()*, or both *items()*
```python
first = {'a': 'agony', 'b': 'bagels', 'c': 'candy'}
for key in first.keys():
    print(key)
#a
#b
#c

for value in first.values():
    print(value)
#agony
#bagels
#candy

for item in first.items():
    print(item)
#('a', 'agony')
#('b', 'bagels')
#('c', 'candy')

#unpacking
for item, value in first.items():
    print(item, value)
#a agony
#b bagels
#c candy
```
* Dictionary comprehensions
    * *{key_expression: value_expression for expression in iterable}*
    * *{key_expression: value_expression for expression in iterable if condition}*
```python
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts
#{'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
vowel_counts
#{'o': 4, 'i': 1, 'a': 2, 'e': 1}
```
### Sets
* Similar to a dictionary without the values. The elements of a set must be unique
    * Sets can use union and intersection operators
    * Sets are unordered
    * Cannot create empty set with *{}* as this creates an empty dict. Must use *set()*
* Create with *set()*
```python
empty_set = set()
empty_set
#set()

even_numbers = {0, 2, 4, 6, 8}
even_numbers
#{0, 2, 4, 6, 8}
```
* Convert with *set()*
```python
set('letters')
#{'l', 'r', 't', 's', 'e'}

set([1, 4, 6, 5, 6])
#{1, 4, 5, 6}

set((1, 4, 6, 5))
#{1, 4, 5, 6}

set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'})
#{'apple', 'cherry', 'orange'}
```
* Get length with *len()*
```python
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
len(reindeer)
#4
```
* Add an item with *add()*
```python
s = set((1, 2, 3))
s
#{1, 2, 3}
s.add(4)
s
#{1,2, 3, 4}
```
* Delete an item with *remove()*
```python
s = set((1, 2, 3))
s.remove(3)
s
#{1, 2}
```
* Iterate with *for* and *in*
```python
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)
#table
#ottoman
#sofa
```
* Combinations and operators
    * Intersection (members common to both sets) with *&* or *intersection()*
    * Union (members of either set) with | or *union()*
    * Difference (members of the first set but not the second) with *-* or *difference()*
    * Symmetric difference (items in one set or the other, but not both) with *^* or *symmetric_difference()*
    * Subset (all members of the first set are also in the second set) with *<=* or *issubset()*
    * Proper subset (the second set needs to have all the members of the first and more) with *<*
    * Superset (all members of the second set are also members of the first) with *>=* or *issuperset()*
    * Proper superset (the first set has all members of the second, and more) with *>*
```python
a = {1, 2}
b = {2, 3}

a & b
#{2}

a.intersection(b)
#{2}

a | b
#{1, 2, 3}

a.union(b)
#{1, 2, 3}

a - b
#{1}

a.difference(b)
#{1}

a ^ b
#{1, 3}

a.symmetric_difference(b)
#{1, 3}

a <= b
#False

a.issubset(b)
#False

a >= b
#False

a.issuperset(b)
#False
```
* Create an immutable set with *frozenset()*
    * Set that cannot be changed
```python
frozenset([3, 2, 1])
#frozenset({1, 2, 3})

frozenset(set([2, 1, 3]))
#frozenset({1, 2, 3})

frozenset({3, 1, 2})
#frozenset({1, 2, 3})

frozenset((2, 3, 1))
#frozenset({1, 2, 3})
```
* Big data structures
    * Lists within a list
    * Lists within a tuple
    * Lists within a dictionary
```python
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuple_of_lists = marxes, pythons, stooges
tuple_of_lists
#(['Groucho', 'Chico', 'Harpo'], ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], ['Moe', 'Curly', 'Larry'])

list_of_lists = [marxes, pythons, stooges]
list_of_lists
#[['Groucho', 'Chico', 'Harpo'], ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], ['Moe', 'Curly', 'Larry']]

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
#{'Marxes': ['Groucho', 'Chico', 'Harpo'], 'Pythons': ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin'], 'Stooges': ['Moe', 'Curly', 'Larry']}
```
