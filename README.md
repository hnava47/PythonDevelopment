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
    * "test string"
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
```python
x = {2, 4, 8}
y = {3, 5, 8}
xy = x | y
print(xy)
{2, 3, 4, 5, 8}
```
        * \Intersection &
```python
x = {2, 4, 8}
y = {3, 5, 8}
xy = x & y
print(xy)
{8}
```
        * \Differences -
```python
x = {2, 4, 8}
y = {3, 5, 8}
xy = x - y
yx = y - x
print(xy)
{2, 4}
print(yx)
{3, 5}
```
        * \Symmetrical differences ^
```python
x = {2, 4, 8}
y = {3, 5, 8}
xy = x ^ y
print(xy)
{2, 3, 4, 5}
```
11. Frozen Set
    * frozenset
    * immutable
    * frozenset(['elsa', 'otto'])
    * set which cannot be changed
12. Dictionary
    * dict
    * **mutable**
    * {"game": "bingo", "dog": "dingo"}
    * {key: value, key: value}
    * key must be unique for dictionary

## Integer operations
* \+ addition
* \- subtraction
* \* multiplication
* / floating-point division
```python
x = 7/2
print(x)
3.5
```
* // integer (truncating) division
```python
x = 7//2
print(x)
3
```
* % modulus (remainder)
```python
x = 7%3
print(x)
1
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
* no multipline comment within python

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
* using *in* to determine comparison within data
```python
vowels = 'aeiou'
letter = 'o'
letter in vowels
TRUE
```

## Text Strings
* Enclosed single of double quotes
    * ''
    * ""
* Allows to place quotes within strings
```python
print("'Nay!'")
'Nay!'
```
* Use three single or double quotes for multiline stings
```python
x = """test multiline
string"""
print(x)
test multiline
string
```
* Difference between print() and automatic echoing
    * print() strips quotes from strings and prints their contents. Meant for human output
    * Interactive interpreter prints the string with quotes and escape characters \n
```python
x = 'hello world'
print(x)
hello world
x
'hello world'
```
* String conversion > str()
```python
str(98.6)
'98.6'
```
* \n > new line
```python
palindrome = 'A man, \nA plan, \nA canal'
print(palindrome)
A man,
A plan,
A canal
```
* \t > tab
```python
print('a\tbc')
a   bc
```
* Combine strings by using +
```python
'Release the kraken! ' + 'No, wait!'
'Release the Kraken! No wait!'
```
