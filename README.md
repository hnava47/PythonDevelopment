# PythonDevelopment

Mutability
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
    * set([2, 4, 8])
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
