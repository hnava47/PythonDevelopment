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
