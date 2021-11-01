<div id="top"></div>

![Python][python-shield]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- Project Logo -->
<br/>
<div align="center">
    <img src="Assets/images/readmelogo.png" alt="Logo" width="80" height="80">
    <h1 align="center">Python Development</h1>
</div>

<!-- Table of Contents -->
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li><a href="#basic-data-types">Basic Data Types</a></li>
        <li><a href="#integer-operators">Integer Operators</a></li>
        <ul>
            <li><a href="#variable-name-conditions">Variable Name Conditions</a></li>
            <li><a href="#libraries">Libraries</a></li>
        </ul>
        <li><a href="#if-elif-else-comparisons">if, elif, else Comparisons</a></li>
        <ul>
            <li><a href="#comparison-operators">Comparison Operators</a></li>
            <li><a href="#multiple-comparisons">Multiple Comparisons</a></li>
            <li><a href="#considered-false">Considered False</a></li>
            <li><a href="#membership-operator-in">Membership Operator In</a></li>
        </ul>
        <li><a href="#text-strings">Text Strings</a></li>
        <li><a href="#for-and-while-loops">For and While Loops</a></li>
        <ul>
            <li><a href="#while-loops">While Loops</a></li>
            <li><a href="#iterate-with-for-and-in">Iterate with For and In</a></li>
        </ul>
        <li><a href="#tuples-and-lists">Tuples and Lists</a></li>
        <ul>
            <li><a href="#tuples">Tuples</a></li>
            <li><a href="#lists">Lists</a></li>
        </ul>
        <li><a href="#dictionaries-and-sets">Dictionaries and Sets</a></li>
        <ul>
            <li><a href="#dictionaries">Dictionaries</a></li>
            <li><a href="#sets">Sets</a></li>
        </ul>
        <li><a href="#functions">Functions</a></li>
        <li><a href="#objects-and-classes">Objects and Classes</a></li>
        <ul>
            <li><a href="#classes">Classes</a></li>
        </ul>
        <li><a href="#testing">Testing</a></li>
        <li><a href="#data-structures-and-algorithms">Data Structures and Algorithms</a></li>
        <ul>
            <li><a href="#complexity-analysis">Complexity Analysis</a></li>
            <li><a href="#memory">Memory</a></li>
            <li><a href="#big-o-notation">Big O Notation</a></li>
            <li><a href="#logarithms">Logarithms</a></li>
            <li><a href="#arrays">Arrays</a></li>
            <li><a href="#linked-lists">Linked Lists</a></li>
            <li><a href="#stacks-and-queues">Stacks and Queues</a></li>
        </ul>
    </ol>
</details>
<br/>

#### Command Line Interface - Mac
```bash
python3
```
```bash
python3 -m pip install requests
```

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

<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>

### Variable Name Conditions
* lowercase letters (a-z)
* uppercase letters (a-z)
* digits (0-9)
* underscore (_)
* case sensitive
* cannot begin with digit
* Python has reserved words (e.g. continue)

<p align="right">(<a href="#top">back to top</a>)</p>

### Libraries
```Python
import webbrowser
import json
from urllib.request import urlopen
```
* Import all code from the Python standard library module called *webbrowser* and *json*
* Import only the urlopen function from the standard library module *urllib.request*

<p align="right">(<a href="#top">back to top</a>)</p>

### Comments
* create comments with #
```python
# this is a comment line
```
* no multi-line comment within python

<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>

### Comparison Operators
* equality ==
* inequality !=
* less than <
* less than or equal <=
* greater than >
* greater than or equal >=

<p align="right">(<a href="#top">back to top</a>)</p>

### Multiple Comparisons
* and
* or
* not

<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>

### Membership Operator In
* using *in* to determine comparison within data object
```python
vowels = 'aeiou'
letter = 'o'
letter in vowels
#TRUE
```

<p align="right">(<a href="#top">back to top</a>)</p>

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
    * _[start:end:step]_
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

<p align="right">(<a href="#top">back to top</a>)</p>

## For and While Loops

<p align="right">(<a href="#top">back to top</a>)</p>

### While Loops
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

<p align="right">(<a href="#top">back to top</a>)</p>

### Iterate with For and In
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

<p align="right">(<a href="#top">back to top</a>)</p>

## Tuples and Lists

<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>

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
    * Named tuples can be a simple alternative to objects

<p align="right">(<a href="#top">back to top</a>)</p>

## Dictionaries and Sets

<p align="right">(<a href="#top">back to top</a>)</p>

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
* Combine dictionaries with _{**a, **b}_
    * Can pass more than two dictionaries _{**a, **b, **c}_
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

<p align="right">(<a href="#top">back to top</a>)</p>

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

<p align="right">(<a href="#top">back to top</a>)</p>

## Functions
* Can do two things with a function
    * *Define* it, with zero or more parameters
    * *Call* it, and get zero or more results
* Define a function with *def*
    * Function names have the same rules as variables (must start with a letter or _ and contain only letters, number, or _)
```python
def do_nothing():
    pass
```
* Call a function with parentheses
    * When you mak a call, Python runs the code inside its definition
```python
def make_a_sound():
    print('quack')

make_a_sound()
#quack
```
```python
def agree():
    return True

if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

#Splendid!
```
* Arguments and parameters
    * Parameters are placed within parentheses of defined function
    * Function can take any number of input arguments (including zero) of any type
    * Function can return any number of output results (also including zero) of any type
    * If function doesn't call *return* explicitly, the caller gets the result *None* (not the same as *False*)
    * Called arguments outside of the function, but parameters inside
    * For below function echo() was called with the argument string 'Rumplestiltskin', which was copied within echo() to the parameter *anything* and then returned to the caller
```python
def echo(anything):
    return anything + ' ' + anything

echo('Rumplestiltskin')
#'Rumplestiltskin Rumplestiltskin'
```
* Positional and keyword arguments
    * Values are copied to their corresponding parameters in order
    * Need to remember the meaning of each position
        * If we place the positional argument in the wrong place, the function will not work as intended
    * If function called with both positional and keyword arguments, the positional arguments need to come first
```python
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken', 'cake')
#{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}

menu('beef', 'bagel', 'bordeaux')
#{'wine': 'beef', 'entree': 'bagel', 'dessert': 'bordeaux'}

menu(entree='beef', dessert='bagel', wine='bordeaux')
#{'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagel'}

menu('frontenac', dessert='flan', entree='fish')
#{'wine': 'frontenac', 'entree': 'fish', 'dessert': 'flan'}
```
* Default parameter values
    * Default used if the caller does not provide a corresponding argument
    * *function(parameter=default):*
    * Default parameter values are calculated when the function is defined, not when it is run
```python
def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken')
#{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'pudding'}

menu('chardonnay', 'chicken', 'doughnut')
#{'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'doughnut'}
```
* (*) groups or explodes a variable number of positional arguments into a single tuple of parameter value
```python
def print_args(*args):
    print('Positional tuple: ', args)

print_args(3, 2, 1, 'wait')
#Positional tuples: (3, 2, 1, wait)

arg = (3, 2, 1, 'wait')
print_args(*args)
#Positional tuples: (3, 2, 1, wait)
```
* (**) groups or explodes keyword arguments into a dictionary, where the argument names are the keys, and their values are the corresponding dictionary values
```python
def print_kwargs(**kwargs):
    print('Keyword arguments: ', kwargs)

print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
#Keyword arguments: {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}

dicts = {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
print_kwargs(**dicts)
#Keyword arguments:  {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
```
* Argument order is:
    * Required positional arguments
    * Optional positional arguments (*args)
    * Optional keyword arguments (**kwargs)

* Keyword-only arguments
    * Single (*) in the function definition means that the following parameters must be provided as named arguments if we don't want their default values
```python
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)
#a
#b
#c
#d
#e
#f

print_date(data, start=4)
#e
#f

print_data(data, end=2)
#a
#b
```
* If argument is mutable, its value can be changed from inside the function
    * It's best practice to avoid this by either documenting that an argument may be changed or return the new value
* Docstrings are used to provide documentation to a functions definition by including a string at the beginning of the function body
```python
def echo(anything):
    'echo returns its input arguments'
    return anything

help(echo)
#Help on function echo in module __main__:

#echo(anything)
#   echo returns its input arguments

print(echo.__doc__)
#echo returns its input arguments
```
* Functions can be assigned to variables, used as arguments to other functions, and returned from functions
* Names that begin and end with two underscores (__) are reserved for use within Python, so they should not be used in variables
    * *function.\_\_name\_\_* name of the function
    * *function.\_\_doc\_\_* documentation string
* Recursion - calling same function within itself
```python
def binSearch(arr, low, high, val):

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            return binSearch(arr, low, mid-1, val)
        else:
            return binSearch(arr, mid+1, high, val)

    else:
        return -1

array = [2, 6, 9, 10, 15]
searVal = 15

print(binSearch(array, 0, len(array)-1, searVal))
```
* Async functions - functions can "give up control" rather than running to completion
* Handle errors with *try* and *excep*
```python
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, 'but got', position)
#Need a position between 0 and 2 but got 5
```

<p align="right">(<a href="#top">back to top</a>)</p>

## Objects and Classes
### Classes
* Define a class with *class*
    * To create a new object that no one has ever created before, you first define a class that indicates what it contains
    * *pass* is the bare minimum to create an object
```python
class cat:
    pass
```
* Initialization using *\_\_init\_\_()*
    * *self* argument specifies that it refers to the individual object itself
    * *\_\_init\_\_()* method is not required in every class definition; it's used to do anything that's needed to distinguish this object from others created from the same class
```python
class cat:
    def __init__(self, name):
        self.name = name

furball = cat('Grumpy')
```
* The above code conducts the following:
    * Looks up the definition of the *cat* class
    * Instantiates (creates) a new object in memory
    * Call the object's \_\_init\_\_() method, passing the newly created object as *self* and the other argument ('Grumpy') as *name*
    * Stores the value of *name* in the object
    * Returns the new object
    * Attaches the variable *furball* to the object
* *name* value passed is now saved with the object as an attribute
```python
print('Our latest addition: ', furball.name)
#Our latest addition: Grumpy
```
* Methods for comparison:
    * \_\_eq\_\_(self, other) -> self == other
    * \_\_ne\_\_(self, other) -> self != other
    * \_\_lt\_\_(self, other) -> self < other
    * \_\_gt\_\_(self, other) -> self > other
    * \_\_le\_\_(self, other) -> self <= other
    * \_\_ge\_\_(self, other) -> self >= other
* Methods for math:
    * \_\_add\_\_(self, other) -> self + other
    * \_\_sub\_\_(self, other) -> self - other
    * \_\_mul\_\_(self, other) -> self * other
    * \_\_floordiv\_\_(self, other) -> self // other
    * \_\_truediv\_\_(self, other) -> self / other
    * \_\_mod\_\_(self, other) -> self % other
    * \_\_pow\_\_(self, other) -> self ** other
* Other methods:
    * \_\_str\_\_(self) -> str(self)
    * \_\_repr\_\_(self) -> repr(self)
        * echo variables to output
    * \_\_len\_\_(self) -> len(self)
```python
class word:
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'word("' + self.text + '")'

first = word('ha')
first   # uses __repr__
#word("ha")

print(first)    # uses __str__
#ha
```

## Testing
* Test with *unittest*
    * Standard library
    * Decide what outcome you want from a certain input, submit the input to the function, and check whether it returned the expected results
    * def setUp(self) -> test case setup can be repetitive, but we an factor set-up code by implement method setUp
    * Expected results are called *assertion*
        * self.assertEqual()
        * self.assertTrue()
        * self.assertFalse()
        * self.assertRaises()
```python
# Initial file: cap.py

def just_do_it(text):
    return text.title()
```
```python
# Test file: test_cap.py

import unittest as ut
import cap as c

class TestCap(ut.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'duck'
        result = c.just_do_it(text)
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = c.just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')

if __name__ == '__main__':
    ut.main()
```
* *setUp()* method is called before each test method, and the *tearDown()* method is called after each
    * Purpose to allocate and free external resources needed by the tests, such as a database connection or some test data

<p align="right">(<a href="#top">back to top</a>)</p>

## Data Structures and Algorithms
* Data structures are a way to organize and manage data. Data values put together with relationships between them

<p align="right">(<a href="#top">back to top</a>)</p>

### Complexity Analysis
* Complexity analysis -> process of determining how efficient an algorithm is. Complexity analysis usually involves finding both the time complexity and the space complexity of an algorithm
* Time complexity -> A measure of how fast an algorithm runs, time complexity is a central concept in the field of algorithms and in coding interviews
* Space complexity -> A measure of how much auxiliary memory an algorithm takes up, space complexity is a central concept in the field of algorithms and in coding interviews

<p align="right">(<a href="#top">back to top</a>)</p>

### Memory
* Bit -> short for binary digit, is a fundamental unit of information that represents a state with one of two values: 0 or 1
* Byte -> a group of eight bits (e.g. 01101000). A single byte can represent up to 256 data values (2<sup>8</sup>). A byte can effectively represent all of the numbers between 0 and 255, inclusive, in binary format.
The following represent the numbers 1, 2, 3, 4, 255 in binary format:
    * 1: 00000001
    * 2: 00000010
    * 3: 00000011
    * 4: 00000100
    * 255: 11111111
* Fixed-width integers -> An integer represented by a fixed amount of bits. For example, a 32-bit integer is an integer represented by 32 bits (4 bytes), and a 64-bit integer is an integer represented by 64 bits (8 bytes)
* Memory -> foundational layer of computing, where all data is stored.
    * Data stored in memory is stored in bytes and, by extension, bits
    * Bytes in memory can "point" to other bytes in memory, so as to store references to other data
    * The amount of memory that a machine has is bounded, making it valuable to limit how much memory an algorithm takes up
    * Accessing a byte or a fixed number of bytes (like 4 bytes or 8 bytes in the case of 32-bit and 64-bit integers) is an elementary operation, which can be loosely treated as a single unit of operational work
* Want algorithm to take up as few free memory slots as possible because memory is finite. One memory slot can hold 8-bits (i.e. 1 byte)
* Each letter in a string is mapped to a number, which is then mapped to a bit for storage
* Pointer -> a memory slot which stores the memory address of a separate memory slot. Just points to another memory slot with relevant piece of data
* Machine can access memory slots very quickly

<p align="right">(<a href="#top">back to top</a>)</p>

### Big O Notation
* Notation used to describe the time and space complexity of algorithms
* Measures the size and speed of the algorithm, as the size of the input increases
    * **Measuring the change in size/speed with respect to the change in the size of the output**
    * Variables used in Big O notation denote the sizes of inputs to algorithms
    * n -> size of the input
    * Following are examples of common complexities ordered from fastest to slowest:
        * <strong>Constant</strong>: O(1)
        * <strong>Logarithmic</strong>: O(log(n))
        * <strong>Linear</strong>: O(n)
        * <strong>Log-linear</strong>: O(nlog(n))
        * <strong>Quadratic</strong>: O(n<sup>2</sup>)
        * <strong>Cubic</strong>: O(n<sup>3</sup>)
        * <strong>Exponential</strong>: O(2<sup>n</sup>)
        * <strong>Factorial</strong>: O(n!)
* Biggest factors that affect Big O are the number of steps and the number of iterations the program takes in repeating structures like a for loop
* What is the Big O of your solution:
    * Binary tree -> O(log n) > logarithmic complexity
    * One for loop -> O(n) > linear complexity
    * Sorting -> O(n log n) > log linear complexity
    * Don't want anything slower than above three
* For fixed-sized inputs, the complexity will be constant O(1)

a = [...] } n

* f<sub>1</sub>(a) => 1 + a[0]
    * O(1) or constant time complexity (O of 1)
    * As n increases, the speed of f<sub>1</sub>(a) remains constant
* f<sub>2</sub>(a) => sum(a)
    * O(n) or linear time complexity (O of n)
    * As n increases, the speed of f<sub>2</sub>(a) increases linearly
* f<sub>3</sub>(a) => pair(a) # 2 for loops together
    * O(n<sup>2</sup>) or quadratic time complexity (O of n squared)
    * Traverses through n inputs 2 times (2 for loops)
* Only care about the very significant factors in our algorithm
    * Meaning, if our program has all the above functions f<sub>4</sub>(a) = O(n<sup>2</sup> + n + 1), it would be simplified to f<sub>4</sub>(a) = O(n<sup>2</sup>)
    * Even if we run f<sub>3</sub>(a) twice in the program, the function complexity f<sub>4</sub>(a) = O(2n<sup>2</sup> + n + 1), but the constant is insignificant, so the program complexity remains f<sub>4</sub>(a) = O(n<sup>2</sup>)
* How to calculate Big O
    1. Break your algorithm/function into individual operations
    2. Calculate the Big 0 of each operation
    3. Add up the Big O of each operation together
    4. Remove the constants
    5. Find the highest order term - this will be what we consider the Big O of our algorithm/function
* Big O notation for data structures:
    1. Array: Insert - O(1) Retrieve - O(1)
    2. Linked List: Insert at head - O(1) Insert at tail - O(n) Retrieve - O(n)
    3. Binary Search: Retrieve - O(n) Retrieve - O(n)
    4. Dynamic Array: Retrieve - O(1) Retrieve - O(1)
    5. Stack: Retrieve - O(1) Retrieve - O(1)
    6. Hash Table: Retrieve - O(n) Retrieve - O(n)
* Big O notation for sorting algorithms
    1. Bubble Sort: Worst case - O(n<sup>2</sup>)
    2. Insertion Sort: Worst case - O(n<sup>2</sup>)
    3. Selection Sort: Worst case - O(n<sup>2</sup>)
    4. Quick Sort: Worst case - O(n<sup>2</sup>)
    5. Merge Sort: Worst case - O(n log(n))
    6. Heap Sort: Worst case - O(n log(n))
* Although worst case quick sort performance is quadratic O(n<sup>2</sup>), in practice quick sort is often used for sorting since its average case is logarithmic O(n log(n))
* When taking into consideration two different inputs/arrays, you need to factor that additional input in the form of O(n + m). With multiple inputs, you would not drop the lowest if inputs are different (i.e. O(m<sup>2</sup> + n))

![Big-O][bigo-screenshot]

<p align="right">(<a href="#top">back to top</a>)</p>

### Logarithms
* log<sub>b</sub>(x) = y if and only if (iif) b<sup>y</sup> = x
* Usage always implies a logarithm of base 2 (log(n) = y iif 2<sup>y</sup> = n) - _binary logarithm_
    * If an algorithm has a logarithmic time complexity of O(log(n)), where n is the size of the input, then whenever the algorithm's iput doubles in size (i.e. whenever n doubles), the number of operations needed to complete the algorithm only increases by one unit
    * An algorithm with linear complexity would see its number of operations double if its input size doubled
* If I'm doubling my input, is there only one additional operation performed?
* Am I eliminating half of the input at every step of the function?

<p align="right">(<a href="#top">back to top</a>)</p>

### Arrays
* A linear collection of data values that are accessible at numbered indices, starting at index 0
* Python refers to arrays as _lists_
* The following are an array's standard operations and their corresponding time complexities:
    * __Accessing a value at a given index__: O(1)
    * __Updating a value at a given index__: O(1)
    * __Inserting a value at the beginning__: O(n)
    * __Inserting a value in the middle__: O(n)
    * __Inserting a value at the end__:
        * amortized O(1) when dealing with a __dynamic array__ (lot of popular programming languages like JavaScript and Python implement arrays as dynamic arrays)
        * O(n) when dealing with a __static array__
    * __Removing a value at the beginning__: O(n)
    * __Removing a value in the middle__: O(n)
    * __Removing a value at the end__: O(1)
    * __Copying the array__: O(n)
* _Static Array_: implementation of an array that allocates a fixed amount of memory to be used for storing the array's values. Appending values to the array therefore involves copying the entire array and allocating new memory for it, accounting for the extra space needed for the newly appended value (linear-time complexity)
* _Dynamic Array_ (can change in size): implementation of an array that preemptively allocates double the amount of memory needed to store the array's values. Appending values to the array is a constant-time operation until the allocated memory is filled up, at which point the array is copied and double the memory is once again allocated for it. This implementation leads to an amortized constant-time insert-at-end complexity
* [1, 2, 3]
    * assuming 64-bit integers, each integer requires 8 bytes of memory (8 memory slots) and they need to be stored back-to-back. Therefore, machine needs to find 24 slots of free memory next to each other (assuming array is static)
    * get (return a value at an index)=> O(1) space and time (ST)
    * set (overriding a value at specific index) => O(1) ST
    * init (create and store array) => O(n) ST
    * traverse (for loop) => O(n) T, O(1) S
    * copy (keeping both arrays) => O(n) ST
    * _static array_ insert at the end of array => O(n) T, O(1) S
        * Needs to adjust memory to make room for new value. Will copy array and allocate enough memory to include additional value
        * Removing old array and creating new array, so space complexity is constant
    * _dynamic array_ insert at the end of array => O(1) TS
        * Dynamic array stores arrays with double required memory, therefore inserting a new value performs at constant complexity
        * Once all memory is used, the operating system will copy, and allocate double the memory again
        * Why is time complexity O(n) for inserting in the middle, since it only affects a portion of the array? Although it may only affect a portion, it's still a constant value (i.e. O(.25n)), which still simplifies to O(n)
    * pop (removing last value) => O(1) ST
    * pop (removing first or middle value) => O(n) T, O(1) S


<p align="right">(<a href="#top">back to top</a>)</p>

### Linked Lists
* Differs from arrays in how the data is stored in memory
    * Arrays (lists) require storage in slots back-to-back. Meaning they are store in memory slots which have to be next to each other (4 64-bit integers in an array requires 32 bytes/slots of free memory back-to-back)
    * Linked lists do __NOT__ require back-to-back memory slots. Operating system will store values anywhere in memory. Values are connected together through pointers which point to the next node in the list (by storing the next node's memory address)
    * Linked lists memory is stored together in groups of two. One stores the value, the other stores the pointer
* 3 -> 1 -> 4 -> 2 -> null
    * get => O(i) T, O(1) S
    * set => O(i) T, O(1) S
    * init => O(n) ST
    * copy => O(n) ST
    * Traverse => O(n) T, O(1) S
    * Insert/delete (depends on head, tail, or in the middle)
* Python creates linked lists through custom class method. No standard function to initialize
#### Singly Linked List
* A data structure that consists of nodes, each with some value and a pointer to the next node in the linked list
* Linked list node's value and next node are typically store in _value_ and _next_ properties, respectively
* First node in a linked list is referred to as the __head__ of the linked list, while the last node in the linked list, whose _next_ property points to the _null_ value, is known as the __tail__ of the linked list
* Example:
```
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> null
```
* Singly linked list typically exposes its head to its user for easy access
* Finding a node in a singly linked list involves traversing through all of the nodes leading up to the node in question (as opposed to instant access with an array)
* Adding or removing nodes simply involves _next_ pointers
* Following are a singly linked list's standard operations and their corresponding time complexities:
    * __Accessing the head__: O(1)
    * __Accessing the tail__: O(n)
    * __Accessing a middle node__: O(n)
    * __Inserting/removing the head__: O(1)
    * __Inserting/removing the tail__: O(n) to access + O(1)
    * __Inserting/removing a middle node__: O(n) to access + O(1)
    * __Searching for a value__: O(n)

```python
# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val
```
```python
# Linked list constructor
class LinkedList:
    def __init__(self):
        self.head = None
```
```python
# Iterating over the list
def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
```
```python
# Adding to the linked list
def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)
```
```python
# Removing from the linked list
def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp
```
```python
# Print the linked list
def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
```
```python
# Using the linked list
linked_list = LinkedList()
linked_list.add_to_tail(Node("1"))
linked_list.add_to_tail(Node("4"))
linked_list.add_to_tail(Node("6"))
print("ll:", linked_list)
first = linked_list.remove_from_head()
print("removed:", first)
print("ll:", linked_list)
```
#### Doubly Linked List
* Each node in a double linked list also has a pointer to the previous node in the linked list
* Previous node is typically stored in a _prev_ property
* Both _next_ (__tail__) and _prev_ (__head__) properties points to _null_
```
null <- 0 <-> 1 <-> 2 <-> 3 <-> 4 <-> 5 -> null
```
* Exposes both its head and tail to user, as opposed to just its head in the case of singly linked list
* Following are a doubly linked list's standard operations and their corresponding time complexities:
    * __Accessing the head__: O(1)
    * __Accessing the tail__: O(1)<sup>* differs from singly linked list</sup>
    * __Accessing a middle node__: O(n)
    * __Inserting/removing the head__: O(1)
    * __Inserting/removing the tail__: O(1)<sup>* differs from singly linked list</sup>
    * __Inserting/removing a middle node__: O(n) to access + O(1)
    * __Searching for a value__: O(n)
#### Circular Linked List
* A linked list that has no clear head or tail, because its "tail" points to its "head", effectively forming a closed circle
* A circular linked list can be either a singly circular linked list or a doubly circular linked list

<p align="right">(<a href="#top">back to top</a>)</p>

### Hash Tables
* Data structure that provides fast insertion, deletion, and lookup of key/value pairs
* Python creates hash tables through standard _dictionaries_
* Uses a dynamic array of linked lists to efficiently store key/value pairs
* Similar to arrays, looking up keys/indexes operate at constant O(1) complexity (on average). However, hash tables allow for non-integer keys
* Behind the scenes, there is a hashing functions which transforms the key into an index
    * If two keys map to the same integer index (collide), linked list leveraged to reference correct key/value pair
    * Example: (value2, key2) -> (value3, key3) -> (value4, key4)
    * This collision causes O(n) time complexity
* When inserting a key/value pair, a hash function first maps the key, which is typically a string, to an integer value and, by extension, to an index in the underlying dynamic array
* Value associated with the key is added to the linked list stored at the index in they dynamic array, and a reference to the key is also stored with the value
* Hash tables rely on highly optimized hash functions to minimize the number of collisions that occur when storing values: cases where two keys map to the same index
* Below is an example of what a hash table might look like under the hood:
```
[
    0: (value1, key1) -> null
    1: (value2, key2) -> (value3, key3) -> (value4, key4)
    2: (value5, key5) -> null
    3: (value6, key6) -> null
    4: null
    5. (value7, key7) -> (value8, key8)
    6: (value9, key9) -> null
]
```
* Keys key2, key3, and key4 collided by all being hashed to 1, and the keys key7 and key8 collided by both being hashed to 5
* The following are a hash table's standard operations and their corresponding time complexities:
    * Inserting a key/value pair: O(1) on average; O(n) in the worst case
    * Removing a key/value pair: O(1) on average; O(n) in the worst case
    * Looking up a key: O(1) on average; O(n) in the worst case
* The worst-case linear-time operations occur when a hash table experiences a lot of collisions, leading to long linked lists internally, which takes O(n) time to traverse
* We typically assume that the hash functions employed by hash tables are so optimized that collisions are extremely rare and constant-time operations are all but guaranteed

<p align="right">(<a href="#top">back to top</a>)</p>

### Stacks and Queues
#### Stack
* An array-like data structure whose elements follow the __LIFO__ rule: Last In, First Out
* A stack is often compared to a stack of books on a table: the last book that's placed on the stack of books is the first one that's taken off the stack
* The following are the stack's standard operations and their corresponding time complexities:
    * __Pushing an element onto a stack__: O(1) ST
    * __Popping an element off the stack__: O(1) ST
    * __Peeking at the element on the top of the stack__: O(1) ST
    * __Searching for an element in the stack__: O(n) T, O(1) S
* A stack is typically implemented with a dynamic array or with a singly linked list
```python
ls = [1, 2, 3, 4]

# Last in
ls.append(5)
print(ls)
# [1, 2, 3, 4, 5]

# First out
ls.pop()
# 5
print(ls)
# [1, 2, 3, 4]
```
#### Queue
* An array-like data structure whose elements follow the __FIFO__ rule: First In, First Out
* A queue is often compared to a group of people standing in line to purchase items at a store: the first person to get in line is the first one to purchase items and to get out of the queue
* The following are the queue's standard operations and their corresponding time complexities:
    * __Enqueuing an element into the queue__: O(1) ST
    * __Dequeueing an element out of the queue__: O(1) ST
    * __Peeking at the element at the front of the queue__: O(1) ST
    * __Searching for an element in the queue__: O(n) T, O(1) S
* A queue is typically implemented with a doubly linked list
```python
ls = [1, 2, 3, 4]

# First in
ls.append(5)
print(ls)
# [1, 2, 3, 4, 5]

# First Out
ls.pop(0)
# 1
print(ls)
# [2, 3, 4, 5]
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Strings
* Strings are stored in memory as arrays of integers, where each character in a given string is mapped to an integer via some character-encoding standard like __ASCII__
* Strings are __immutable__, meaning that they can't be edited after creation
* Simple operations like appending a character to a string are more expensive than they might appear
* The following are string common operations and their corresponding time complexities:
    * traverse => O(n) T, O(1) S
    * copying => O(n) ST
    * get => O(1) ST
    * Adding two strings together => O(n + m) where n and m are different strings
* Best practice when having to manipulate strings is to convert the string to an array and manipulate the array by appending in constant time, then concatenate. Lists are mutable, and therefore isn't recreated when a new character is added
```python
string = 'this is a string'
string = list(string)
# ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']

# O(1)
string.append('x')

# O(1)
newString = ''

# O(n)
for value in string:
    newString += value

print(newString)
# this is a stringx
```
* Below operation has a time complexity of __O(n<sup>2</sup>)__ where n is the length of _string_, because each addition of a character to _newString_ creates an entirely new string and is itself an __O(n)__ operation
```python
string = "this is a string"
newString = ""

for character in string:
    newString += character
```
### Graphs
* __Graph__: A collection of nodes or values called _vertices_ that might be related; relations between vertices are called _edges_
    * Examples: social network where vertices are users and whose edges are friendships between users, or a city map whose vertices are locations in the city and whose edges are roads between the locations
* __Graph Cycle__: Cycle occurs in a graph when three or more vertices in the graph are connected so as to form a closed loop
* __Acyclic Graph__: A graph that has no cycles
* __Cyclic Graph__: A graph that has at least one cycle
* __Directed Graph__: A graph whose edges are directed, meaning they can only be traversed in one direction, which is specified
    * In the case of a directed graph, the graph is:
        * strongly connected if there are bidirectional connections between the vertices of every pair of vertices (i.e. for every vertex-pair (u, v) you can reach v and u and u from v)
        * weakly connected if there are connections (but not necessarily bidirectional ones) between the vertices of every pair of vertices
    * Example: a graph of airports and flights would likely be directed, since a flight specifically goes from one airport to another (i.e. it has a direction), without necessarily implying the presence of a flight in the opposite direction
* __Undirected Graph__: A graph whose edges are undirected, meaning that they can be be traversed in both directions
    * Example: a graph of friends would likely be undirected, since friendship is, by nature, bidirectional
* __Connected Graph__: A graph is connected if for every pair of vertices in the graph, there's a path of one or more edges connecting the given vertices
```python
# Space -> O(v + e)
# Time of traversal -> O(v + e)
# v -> number of vertices
# e -> number of edges
graphDict = {1: [2, 4, 8, 9], 2: [5, 7], 3: [6], 4: [11], 5: [7]}
# {vertices: [list of edges]}
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hector-nava-mba
[bigo-screenshot]: Assets/images/bigO.jpeg
