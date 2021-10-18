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
2. Integer
    * int
    * immutable
    * 3
3. Floating Point
    * float
    * immutable
    * 3.45
4. Complex
    * complex
    * immutable
    * 5 - 3j
5. Text String
    * str
    * immutable
    * 'test string'
6. List
    * list
    * **mutable**
    * [2, 4, 8]
7. Tuple
    * tuple
    * immutable
    * (2, 4, 8)
8. Bytes
    * bytes
    * immutable
    * b'ab/xff'
9. ByteArray
    * bytearray
    * **mutable**
    * bytearray(...)
10. Set
    * set
    * **mutable**
    * {2, 4, 8}
    * set([2, 4, 8])
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
12. Dictionary
    * dict
    * **mutable**
    * {'game': 'bingo', 'dog': 'dingo'}
    * dict([('game', 'bingo',), ('dog', 'dingo')])
    * {key: value, key: value}
    * Unordered collection with key and value elements

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
