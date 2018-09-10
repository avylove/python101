
.. _lesson2-datatypes:

====================
Lesson 2 - Datatypes
====================

Dynamic Typing
==============

* Variables don't have to be declared before assignment
* Types are bound to values, not variables

    .. code-block:: pycon

        >>> var1 = 1
        >>> type(var1)
        <type 'int'>
        >>> var1 = "1"
        >>> type(var1)
        <type 'str'>


Mutability
==========

* Depending on an object's type it is mutable or immutable
* Immutable objects can't be changed, instead they are replaced
* Mutable objects can be changed
* Most data types are immutable
* Mutable types include:
    * list
    * set
    * dict
    * bytearray
* Mutability is important when considering references


References
==========

* Python is reference-based
* Garbage collection will free memory when a value is no longer referenced
    * Unreferenced count is 1, since the garbage collector keeps a reference

    .. code-block:: pycon

        >>> import sys
        >>> var1 = "somedata"
        >>> sys.getrefcount(var1)
        2
        >>> var2 = var1
        >>> sys.getrefcount(var1)
        3


References
==========

* References are to values, not to variables
    * This can be confusing

    .. code-block:: pycon

        >>> sys.getrefcount("somedata")
        4
        >>> var1 += "changes"
        >>> var1
        'somedatachanges'
        >>> var2
        'somedata'

        >>> var3 = [1, 2, 3]
        >>> var4 = var3
        >>> var3.append(4)
        >>> var3
        [1, 2, 3, 4]
        >>> var4
        [1, 2, 3, 4]


Sequences
=========

.. spelling::
    unicode

* Sequences are ordered collections of values
* Sequences include:
    * list (mutable)
    * tuple
    * str
    * unicode (Python 2 Only)
    * bytes
    * bytearray (mutable)
* Elements in a sequence can be accessed by index, starting with 0

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> myList[1]
        2

    * This can get fancy with slice notation (We cover this later)


Sequences Operations
====================

* Concatenate - Combine two sequences

    .. code-block:: pycon

        >>> [1, 2, 3] + [3, 4, 5]
        [1, 2, 3, 3, 4, 5]

* Repeat - Repeat a sequence n times

    .. code-block:: pycon

        >>> "Hodor! " * 3
        'Hodor! Hodor! Hodor! '

        >>> 2 * [1, 2, 3]
        [1, 2, 3, 1, 2, 3]


Sequences Operations
====================

* Index - Find index of first occurrence of a value

    .. code-block:: pycon

        >>> 'Hodor'.index('o')
        1


* Count - Count occurrences of a value

    .. code-block:: pycon

        >>> 'Hodor'.count('o')
        2


Mutable Sequences
=================

* Mutable sequences include:
    * list
    * bytearray

* Mutable sequences include operations that change data in place


Mutable Sequence Operations
===========================

* Assign - Change an value by index

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> myList[1] = "Two"
        >>> myList
        [1, 'Two', 3]

* Append - Add a value to the end of a sequence

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> myList.append(4)
        >>> myList
        [1, 2, 3, 4]

Mutable Sequence Operations
===========================

* Extend - Add a sequence to the end of another sequence

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> myList.extend([4, 5])
        >>> myList += [6, 7]
        >>> myList
        [1, 2, 3, 4, 5, 6, 7]


* Insert - Insert an value at a specific index

    .. code-block:: pycon

        >>> myList = [1, 2, 3, 4]
        >>> myList.insert(2, "The Spanish Inquisition")
        >>> myList
        [1, 2, 'The Spanish Inquisition', 3, 4]


Mutable Sequence Operations
===========================

* Reverse - Reverse sequence in place

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> myList.reverse()
        >>> myList
        [3, 2, 1]

* Delete - Delete an element by index

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> del myList[1]
        >>> myList
        [1, 3]


Mutable Sequence Operations
===========================

* Remove - Delete an element by value

    .. code-block:: pycon

        >>> myList = [1, 2, 3, 3, 4]
        >>> myList.remove(3)
        >>> myList
        [1, 2, 3, 4]

* Pop - Remove and return value by index, defaults to last element

    .. code-block:: pycon

        >>> myList = [1, 2, 3, 4, 5]
        >>> myList.pop()
        5
        >>> myList
        [1, 2, 3, 4]
        >>> myList.pop(2)
        3
        >>> myList
        [1, 2, 4]


Mutable Sequence Operations - Python 3
======================================

* Copy - Create a shallow copy of sequence (Python 3 only)
    * For Python 2 use the :py:mod:`copy` module or ``t = s[:]``

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> id(myList)
        139643169976904
        >>> myNewList = myList.copy()
        >>> id(myNewList)
        139643167505480

* Clear - Remove all values (Python 3 only)
    * For Python 2 use ``del s[:]``

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> myList.clear()
        >>> myList
        []


Iterable Types
==============
* Iterable types allow their contents to be iterated over programmatically
* Iterable types include an :py:meth:`~iterator.__iter__` method
* Iterable types include:
    * dict (mutable)
    * set (mutable)
    * frozenset
    * All Sequences

Iterable Operations
===================

* :ref:`for <for>` statements

    .. code-block:: pycon

        >>> ducks = ['Huey', 'Dewey', 'Louie']
        >>> for duck in ducks:
        ...     print(duck)
        ... 
        Huey
        Dewey
        Louie



Iterable Operations
===================

* :ref:`in <in>` and :ref:`not in <not in>` statements

    .. code-block:: pycon

        >>> myList = [1, 2, 3]
        >>> 1 in myList
        True
        >>> 4 in myList
        False

        >>> 4 not in myList
        True
        >>> 1 not in myList
        False


Iterable Operations
===================

* Length - Number of items in an iterable

    .. code-block:: pycon

        >>> len([1, 2, 3])
        3

* Minimum - Smallest value in a sequence

    .. code-block:: pycon

        >>> min([1, 2, 3])
        1

* Maximum - Largest value in a sequence

    .. code-block:: pycon

        >>> max([1, 2, 3])
        3


Iterable Operations
===================

* Sort - Create a new sorted list from the values in an iterable with :py:func:`sorted`
    * Takes an optional key (sorting method)
    * reversible with reverse keyword

    .. code-block:: pycon

        >>> sorted([1, 2, 3], reverse=True)
        [3, 2, 1]


* Sum - Add numbers in an iterable
    * Takes an optional starting value

    .. code-block:: pycon

        >>> sum([1, 2, 3])
        6

        >>> sum([1, 2, 3], 2)
        8



Data Types Summary
==================

.. image:: /_static/python_data_types.svg
    :height: 500px
    :align: center


Lists
=====

* Lists are mutable sequences
* Can contain any type of Python object
* Create a list with comma-separated values in square brackets

    .. code-block:: pycon
        
        myList = [1, "horse", ['another', list], 3, "Kitchen Sink", "spam"]

* Additional list operation
    * Sort - Sort a list in place
        * Note how this is different than using :py:func:`sorted`

    .. code-block:: pycon

        >>> myList = [2, 1, 5, 4, 3]
        >>> myList.sort()
        >>> myList
        [1, 2, 3, 4, 5]


Tuples
======

* Tuples are immutable sequences
* Can contain any type of Python object
* Tuples are more memory-efficient than lists
* Create a tuple with comma-separated values in parentheses

    .. code-block:: pycon

        >>> myTuple = (1, "spam", 4, "eggs", "spam and eggs", "spam")

* A tuple with one element requires a trailing comma

    .. code-block:: pycon

        >>> myTuple = (1)  # Wrong!
        >>> type(myTuple)
        <type 'int'>
        >>>
        >>> myTuple = (1,)
        >>> type(myTuple)
        <type 'tuple'>

Tuples
======

* Tuples can also be created without parentheses

    .. code-block:: pycon

        >>> myTuple = 1, "spam", 4, "eggs", "spam and eggs", "spam"
        >>> myTuple
        (1, 'spam', 4, 'eggs', 'spam and eggs', 'spam')

    * Commonly used for pass-through tuples (such as return statements)
    * Use parentheses for general use


Strings
=======

* To create strings use quotes
    * Single, double, triple-double, and triple-single quotes are accepted
    * Escape special characters with backslashes
    * Single quotes do not have to be escaped in double quotes
    * Double quotes do not have to be escaped in single quotes
    * Triple quotes can span multiple lines

    .. code-block:: pycon

        >>> 'I\'m in single quotes'
        "I'm in single quotes"
        >>> "I'm in double quotes"
        "I'm in double quotes"
        >>> """I am on more
        ... than one line"""
        'I am on more\nthan one line'
        >>> '''What? There are
        ... "triple single" quotes too!'''
        'What? There are\n"triple single" quotes too!


Unicode
=======

* In Python 2, there are two types of strings: strings and Unicode strings
* In Python 3, all strings are Unicode
* To make a Unicode string in Python 2, used :py:func:`unicode` or prepend ``u`` or ``U``

    .. code-block:: pycon

        >>> u"unicode string"
        u'unicode string'
        >>> unicode("unicode string")
        u'unicode string'
        >>> type(u"unicode string")
        <type 'unicode'>
        >>> type("plain string")
        <type 'str'>


Unicode
=======

* Non-ASCII characters can be entered in Unicode or escaped Unicode

    .. code-block:: pycon

        >>> avram = u"אַבְרָם"
        >>> avram_escaped = u'\u05d0\u05b7\u05d1\u05b0\u05e8\u05b8\u05dd'
        >>> avram == avram_escaped
        True

* When including non-ASCII characters in a source file, include an encoding header

    .. code-block:: python

        #!/usr/bin/env python 
        # -*- coding: utf-8 -*-


Bytes
=====

* Python 3 includes the :py:class:`bytes` datatype for byte strings
* Byte strings are immutable sequences for binary data
* Contents are 8-bit values (integers between 0 and 255)

    .. code-block:: pycon

        >>> eString = b'encoded string'
        >>> type(eString)
        <class 'bytes'>
        >>> print(eString)
        b'encoded string'
        >>> print(eString.decode())
        encoded string
        >>>
        >>> # Python 3 includes a from_bytes() method for int
        ... int.from_bytes(b'\x00\x10', byteorder='big')
        16

* In Python 2.6 and 2.7, bytes is an alias to str


String Types
============

.. image:: /_static/python_strings.svg
    :height: 500px
    :align: center


Byte Arrays
===========

* Byte arrays are mutable sequences (Like lists)
* Contents are 8-bit values (Like bytes)

    .. code-block:: pycon

        >>> b = bytearray(b'abcd')
        >>> b.append(101)
        >>> print(b.decode())
        abcde

* Byte arrays are useful when modifying larger chunks of binary data


Raw Strings
===========

* Prepending an ``r`` (or ``R``) to a string prevents interpretation of escape sequences
* Useful with regular expressions

    .. code-block:: pycon

        >>> r"I\'m not interpreted\n"
        "I\\'m not interpreted\\n"

* To create raw unicode strings, prepend ``ur``

    .. code-block:: python

        >>> ur"I\'m not interpreted\n"
        u"I\\'m not interpreted\\n"

* To create raw byte strings, prepend ``br``

    .. code-block:: python

        >>> br'\x00\x10'
        b'\\x00\\x10'
        >>> int.from_bytes(br'\x00\x10', byteorder='big')
        6663128632962593072


String Operations
=================

* String and string-like objects support a number of useful methods
    * :py:meth:`~str.lower` -- Return a copy with all lowercase characters
    * :py:meth:`~str.upper` -- Return a copy with all uppercase characters
    * :py:meth:`~str.capitalize` -- Return a copy with only the first character capitalized
    * :py:meth:`split([sep[, maxsplit]]) <str.split>` -- Split string on separator
    * :py:meth:`strip([chars]) <str.strip>` -- Return a copy with leading trailing characters removed
    * :py:meth:`join(iterable) <str.join>` -- Return concatenation of iterable with string as separator
    * :py:meth:`find(sub[, start[, end]]) <str.find>` -- Return the index of the first occurrence of a substring
    * :py:meth:`startswith(prefix[, start[, end]]) <str.startswith>` -- Return the True if string starts with prefix
    * :py:meth:`endswith(suffix[, start[, end]]) <str.endswith>` -- Return the True if string ends with suffix

Integers (Python 2)
===================

* In Python 2 there are plain integers and long integers
    * int: ``1``
    * long: ``1L``
* Don't use longs explicitly, there are very few valid reasons to
* Plain integers are automatically converted to long integers

    .. code-block:: pycon

        >>> sys.maxint
        9223372036854775807
        >>> type(sys.maxint)
        <type 'int'>
        >>> sys.getsizeof(sys.maxint)
        24
        >>> type(sys.maxint + 1)
        <type 'long'>
        >>> sys.getsizeof(sys.maxint + 1)
        36


Integers (Python 3)
===================

* In Python 3, there is only one type of integer
    * int: ``1``

    .. code-block:: pycon

        >>> type(1)
        <class 'int'>
        >>> sys.getsizeof(1)
        28
        >>> sys.maxsize
        9223372036854775807
        >>> type(sys.maxsize)
        <class 'int'>
        >>> sys.getsizeof(sys.maxsize)
        36
        >>> type(sys.maxsize * sys.maxsize)
        <class 'int'>
        >>> sys.getsizeof(sys.maxsize * sys.maxsize)
        44


Other Number Types
==================

* float: ``1.0``

* complex: ``1j``

    * "j" is used instead of "i" as a stand-in for √-1


Non-decimal numbers
===================

* No separate types for binary, hex, decimal, octal

    .. code-block:: pycon

        >>> 1 + 0x1 + 0b0001 + 0o01
        4

* Display numbers in other bases using display functions

    .. code-block:: pycon

        >>> hex(100)
        '0x64'
        >>> bin(100)
        '0b1100100'
        >>> oct(100)
        '0o144'

* Note the prefix for octal numbers changed in Python 3 from "0" to "0o".
  Always use "0o", even in Python 2, but you may see "0" sometimes.


Numbers From Strings
====================

* Convert strings to numbers using :py:func:`int`, :py:func:`float`, and :py:func:`complex`

    .. code-block:: pycon

        >>> # For decimal, no base is required
        ... int("100")
        100
        >>> # For binary include base 2
        ... int("1100100", 2)
        100
        >>> # For octal include base 8
        ... int("144", 8)
        100
        >>> # For hex include base 16
        ... int("64", 16)
        100
        >>> float("2")
        2.0
        >>> complex("1j")
        1j


Sets
====

* Sets are unordered collections of unique objects
* Not a sequence, but is an iterable
* A frozenset is an immutable set
* Sets can be created empty or from a sequence

    .. code-block:: pycon

        >>> set()
        set([])
        >>> set([1, 2, 2, 2, 3])
        set([1, 2, 3])

* Starting in Python 2.7, a non-empty set can also be defined with curly braces

    .. code-block:: pycon

        >>> {1, 2, 1}
        set([1, 2])


Set Operations
==============

* Add an item to a set

    .. code-block:: pycon

        >>> mySet = set([1, 2, 3])
        >>> mySet.add("four")

* Add multiple items to a set

    .. code-block:: pycon

        >>> mySet = set([1, 2, 3])
        >>> mySet.update([3, 4, 5])

* Remove an item

    .. code-block:: pycon

        >>> mySet.remove("four")

Dictionaries
============

* Mapping object, collection of key-value pairs
* Keys can be any :term:`hashable` object
    * Any built-in immutable object can be used as a key
    * strings are most common
* Values can be any object

* There are several ways to define a dictionary

    .. code-block:: pycon

        >>> a = {'one': 1, 'two': 2, 'three': 3}
        >>> b = dict(one=1, two=2, three=3)
        >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
        >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
        >>> e = dict({'three': 3, 'one': 1, 'two': 2})
        >>> a == b == c == d == e
        True

Dictionary Operations
=====================

* Accessing a value by key

    .. code-block:: pycon

        >>> myDict = {'name' : 'Lancelot', 'quest' : 'Holy Grail', 'color' : 'blue'}

        >>> myDict['name']
        'Lancelot'

        >>> myDict.get('name')
        'Lancelot'

* The :py:meth:`~dict.get` method accepts a fallback value

    .. code-block:: pycon

        >>> myDict.get('hometown', 'Camelot')
        'Camelot'


Dictionary Operations
=====================

* Add a key-value pair

    .. code-block:: pycon

        >>> myDict['hometown'] = 'Camelot'
    
* Deleting a key-value pair

    .. code-block:: pycon

        >>> del myDict['hometown']

* Adding multiple values

    .. code-block:: pycon

        >>> myDict.update({'hometown': 'Camelot', 'fancies': 'Guinevere', 'color': 'navy'})

    * If a key already exists, it's value will be updated


Dictionary Operations
=====================

* List all keys
    .. code-block:: pycon

        >>> myDict.keys()
        ['color', 'quest', 'name']

* List all values
    .. code-block:: pycon

        >>> myDict.values()
        ['navy', 'Holy Grail', 'Lancelot']

* List all key-value pairs
    .. code-block:: pycon

        >>> myDict.items()
        [('color', 'navy'), ('quest', 'Holy Grail'), ('name', 'Lancelot')]

* The behavior of :py:meth:`~dict.keys`, :py:meth:`~dict.values`, and :py:meth:`~dict.items` is slightly different in Python 3
    * Instead of lists, a dictionary view object is returned
        * Dynamic, so contents update when dictionary updates
        * More memory efficient


Dictionary Operations
=====================

* Get a value or set a value if it doesn't exist

    .. code-block:: pycon

        >>> myDict['weapon']
        KeyError: 'weapon'
        >>> myDict.get('weapon', 'lance')
        'lance'
        >>> myDict.setdefault('weapon', 'sword')
        'sword'
        >>> myDict['weapon']
        'sword'

* Make a shallow copy

    .. code-block:: pycon

        >>> id(myDict)
        140719862222472
        >>> myNewDict = myDict.copy()
        >>> id(myNewDict)
        140719862223208


Dictionary Operations
=====================

* Remove a key-value pair and return it

    .. code-block:: pycon

        >>> myDict.pop('color')
        'navy'
        >>> 'color' in myDict
        False

* Remove a random key-value pair and return it

    .. code-block:: pycon

        >>> myDict.popitem()
        ('fancies', 'Guinevere')

    - Useful for destructively consuming a dictionary


NoneType
========

* A common object for null definitions
* Often used in place of an undefined value
* When testing for None, use ``is`` and never ``==``
    - Faster
    - Behavior of "==" can be customized

    .. code-block:: pycon

        >>> var1 = None
        >>> var1 is None
        True

Boolean Object
==============

* Has two values: True and False
* Subclass of :py:class:`int`
    * True is 1
    * False is 0
* Set in assignment

    .. code-block:: pycon

        >>> a = True
        >>> a is True
        True

* Set with :py:class:`bool`
    * None, values of 0, and empty sequences are False

    .. code-block:: pycon

        >>> bool([])
        False

Additional Datatypes
====================

* The :py:mod:`collections` module provides additional useful datatypes
    * :py:func:`~collections.namedtuple` -- Tuple with named fields
    * :py:class:`~collections.deque` -- double-ended queue
    * :py:class:`~collections.Counter` -- Dictionary optimized for managing counts
    * :py:class:`~collections.OrderedDict` -- Dictionary that maintains item order
    * :py:class:`~collections.defaultdict` -- Dictionary that takes a function to supply missing values

