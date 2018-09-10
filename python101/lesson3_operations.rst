
.. _lesson3-operations:

=====================
Lesson 3 - Operations
=====================

Arithmetic Operators - Basic
============================

* Addition
    .. code-block:: pycon

        >>> 1 + 2
        3

* Subtraction
    .. code-block:: pycon

        >>> 1 - 2
        -1

* Multiplication
    .. code-block:: pycon

        >>> 1 * 2
        2

* Division
    .. code-block:: pycon

        >>> 4 / 2
        2

Arithmetic Operators - Division
===============================

* In Python 2, division of two integers is an integer

    .. code-block:: pycon

        >>> 3/2
        1

* In Python 3, division of two integers is a float

    .. code-block:: pycon

        >>> 3/2
        1.5

* To get a float result in Python 2, make one number a float

    .. code-block:: pycon

        >>> float(3) / 2
        1.5

* To get Python 3 behavior in Python 2

    .. code-block:: python

        from __future__ import division


Arithmetic Operators - Division
===============================

* To return only whole numbers, use // (floor division)
    .. code-block:: pycon

        >>> 1 // float(2)
        0.0
        >>> float(3) // 2
        1.0

* Modulus - Return the remainder
    .. code-block:: pycon

        >>> 1 % 2
        1
        >>> 7 % 5
        2

* Return whole number and remainder
    .. code-block:: pycon

        >>> divmod(1, 2)
        (0, 1)
        >>> divmod(7, 5)
        (1, 2)

Arithmetic Operators
====================

* Exponents
    .. code-block:: pycon

        >>> 2 ** 3
        8
        >>> pow(2, 3)
        8

* Absolute Value
    .. code-block:: pycon

        >>> abs(-1)
        1
        >>> abs(2j)
        2.0

* To do more complex math see the :py:mod:`math` module
* To do really complex math:
    * `NumPy <http://numpy.org>`_
    * `SciPy <http://scipy.org>`_


Arithmetic - Order of Operations
================================

* Python is PEMDAS compliant
    * P - Parentheses
    * E - Exponents
    * M - Multiplication
    * D - Division
    * A - Addition
    * S - Subtraction

    .. code-block:: pycon

        >>> 2 ** 2 + 10 / 2
        9
        >>> 2 ** (2 + 10) / 2
        2048

* Functions and lookups are completed before operations

    .. code-block:: pycon

        >>> 2 * abs(-2)
        4


Comparison Operators
====================

* Equal (==)

    .. code-block:: pycon

        >>> 1 == 1
        True
        >>> "morning" == "night"
        False

* Not Equal (!=)

    .. code-block:: pycon

        >>> 1 != 1
        False
        >>> "morning" != "night"
        True


Comparison Operators
====================

* Less than (<)

    .. code-block:: pycon

        >>> 1 < 2
        True

* Less than or equal (<=)

    .. code-block:: pycon

        >>> 2 <= 2
        True

* Greater than (>)

    .. code-block:: pycon

        >>> 2 > 1
        True

* Greater than or equal (>=)

    .. code-block:: pycon

        >>> 2 >= 2
        True


Comparison Operators
====================

* Identity (is / is not)

    .. code-block:: pycon

        >>> 1 is 1
        True
        >>> [1, 2] is [1, 2]
        False

        >>> 1 is not 1
        False
        >>> [1, 2] is not [1, 2]
        True

    * ``is`` tests if two objects are the same, not if they have the same value


Boolean Operators
=================

* OR
    .. code-block:: pycon

        >>> False or False
        False
        >>> False or True
        True

* AND
    .. code-block:: pycon

        >>> True and True
        True
        >>> True and False
        False

* NOT
    .. code-block:: pycon

        >>> not True
        False
        >>> not False
        True


Set Operators
=============

* Union - Create new set with elements from all sets

    .. code-block:: pycon

        >>> set([1, 2]) | set([2, 3]) | set([2, 3, 4])
        set([1, 2, 3, 4])

* Intersection - Create new set with elements common to all sets

    .. code-block:: pycon

        >>> set([1, 2]) & set([2, 3]) & set([2, 3, 4])
        set([2])

* Difference - New set with elements appearing only in first set

    .. code-block:: pycon

        >>> set([1, 2]) - set([2, 3, 4])
        set([1])

* Symmetric Difference - New set with unique elements from each set

    .. code-block:: pycon

        >>> set([1, 2]) ^ set([2, 3, 4])
        set([1, 3, 4])


Set Operators
=============

* Subset - True if every element in first set is in second set

    .. code-block:: pycon

        >>> set([1, 2, 3]) <= set([1, 2, 3, 4])
        True

* Proper Subset - True if subset and sets are not equal

    .. code-block:: pycon

        >>> set([1, 2, 3, 4]) < set([1, 2, 3, 4])
        False

* Superset - True if every element in second set is in first set

    .. code-block:: pycon

        >>> set([1, 2, 3, 4]) >= set([1, 2, 3])
        True

* Proper Superset - True if superset and not equal

    .. code-block:: pycon

        >>> set([1, 2, 3, 4]) > set([1, 2, 3, 4])
        False


Assignment Operators
====================

* The basic assignment operator is the equal sign

    .. code-block:: pycon

        >>> var1 = 2

* There is an assignment shortcut for basic math operators

    .. code-block:: pycon

        >>> var1 = 2
        >>> var1 += 1
        >>> var1
        3
        >>> var2 = 7
        >>> var2 %= 5
        >>> var2
        2

Assignment Operators
====================

* For sequences, concatenation and assignment can be combined

    .. code-block:: pycon

        >>> mylist = [1, 2]
        >>> mylist += [3, 4]
        >>> mylist
        [1, 2, 3, 4]

* Works for set operations too

    .. code-block:: pycon

        >>> mySet = set([1, 2, 3])
        >>> mySet ^= set([2, 3, 4])
        >>> mySet
        set([1, 4])


Objects as Strings
==================

* All Python objects can be represented as strings
* The implementation varies across object types
* There are two formats for objects strings: representation and display
* Representation string
    * Defined by the object's :py:meth:`~object.__repr__` method
    * Shown with the :py:func:`repr` function or in the Python console
    * Intended to be valid syntax to recreate object
* Display string
    * Defined by the object's :py:meth:`~object.__str__` method
    * Defaults to representation string
    * Shown with the :py:func:`str` function or when treating a non-string object as a string
    * Intended to be a user-friendly representation of an object


Objects as Strings
==================

* For example, the str and repr output for an exception is different

    .. code-block:: pycon

        >>> e = RuntimeError("Something went wrong")
        >>> repr(e)
        "RuntimeError('Something went wrong',)"
        >>> str(e)
        'Something went wrong'

* In Python 3, the :py:func:`ascii` function returns the :py:func:`repr` output with non-ASCII characters escaped


String Formatting
=================

* The ``%`` operator can be used to format strings
* The format is similar to ``sprintf()`` in C
* Values can be specified in a tuple or dictionary

    .. code-block:: pycon

        >>> "Hi! My name is %s. I can count to %d" % ('George', 732)
        'Hi! My name is George. I can count to 732'

        >>> "Hi! My name is %(name)s. I can count to %(number)d" % \
        ... {'name' : 'George', 'number' : 732}
        'Hi! My name is George. I can count to 732'

* Single values can be on their own

    .. code-block:: pycon

        >>> 'Hello, %s' % 'world'
        'Hello, world'

String Formatting
=================

.. image:: /_static/string_formatting.svg
   :align: center

* Flags
    * ``#`` -- "Alternate form" (non-decimal numbers have prefix)
    * ``0`` -- Pad number with 0's
    * ``-`` -- Adjust left
    * ``(space)`` -- Space before positive number
    * ``+`` -- '+' or '-' before number


String Formatting
=================

* Conversion Types
    * ``d`` or ``i`` -- Signed integer (decimal)
    * ``o`` -- Signed integer (octal)
    * ``x`` or ``X`` -- Signed integer (hex)
    * ``e`` or ``E`` -- Float in exponential format
    * ``f`` or ``F`` -- Float in decimal format
    * ``g`` or ``G`` -- Float in decimal or exponential depending on size
    * ``c`` -- Single character (converts positive integer)
    * ``r`` -- Python object converted with :py:func:`repr`
    * ``s`` -- Python object converted with :py:func:`str`


String Formatting - Examples
============================

* Pad integer with zeros

    .. code-block:: pycon

        >>> '%03d' % 12
        '012'

* Float precision to 3 decimals

    .. code-block:: pycon

        >>> '%.3f' % 12.1236
        '12.124'

* Float precision as a variable

    .. code-block:: pycon

        >>> '%.*f' % (3, 12.1236)
        '12.124'


String Formatting - Examples
============================

* Left pad string to 15 characters

    .. code-block:: pycon

        >>> '%15s' % 'hello'
        '          hello'

* Right pad string to 15 characters

    .. code-block:: pycon

        >>> '%-15s' % 'hello'
        'hello          '

* Print representation string for an object

    .. code-block:: pycon

        >>> '%r' % Exception("something bad Happened")
        "Exception('something bad Happened',)"


str.format()
============

* In Python 2.6, the :py:meth:`str.format` method was introduced
* Preferred method in newer versions of Python
* More flexible than the old format
* By default, objects are converted using their own ``__format__()`` method
* Falls back to :py:func:`str` and then :py:func:`repr`

    .. code-block:: pycon

        >>> # In Python 2.7+, no name or index is required
        ... "Hi! My name is {}. I can count to {}".format('George', 732)
        'Hi! My name is George. I can count to 732'

        >>> "Hi! My name is {1}. I can count to {0}".format(732, 'George')
        'Hi! My name is George. I can count to 732'

        >>> "Hi! My name is {name}. I can count to {number}".format(
        ... name='George', number=732)
        'Hi! My name is George. I can count to 732'

str.format()
============

.. spelling::
    formatSpec

.. image:: /_static/str_format.svg
   :align: center

* Conversion
    * ``!s`` -- Convert using :py:func:`str`
    * ``!r`` -- Convert using :py:func:`repr`
    * ``!a`` -- Convert using :py:func:`ascii` (Python 3 Only)

* The format specification (formatSpec) is a mini-language
    * Can be object-specific
    * Most objects use a common language
        * See :py:class:`datetime.datetime` for an object with special formatting

Format Specification Mini-Language
==================================

.. image:: /_static/formatspec.svg
   :align: center

* Fill
    * Any character

* Align
    * ``<`` -- Left-aligned (default for most objects)
    * ``>`` -- Right-aligned (default for numbers)
    * ``=`` -- Force padding after any sign for numbers
    * ``^`` -- Center is available space

* Sign
    * ``+`` -- Include sign for both positive and negative numbers
    * ``-`` -- Include sign only for negative numbers (default)
    * ``(space)`` -- Include a space for positive numbers and sign for negative numbers

Format Specification Mini-Language
==================================

.. image:: /_static/formatspec.svg
   :align: center

* #
    * Use "alternate form" (non-decimal numbers have prefix)

* 0
    * Equivalent to fill character of '0' with an alignment type of '='

* ,
    *  Use comma for thousands separator

* Conversion Types
    * Supports the same types as classic string formatting
    * ``b`` -- Integer (binary)
    * ``n`` -- Same as 'd' or 'g', but use locale to determine separator
    * ``%`` -- Float as a percentage
    

str.format() - Examples
=======================

* Pad integer with zeros

    .. code-block:: pycon

        >>> '{:03d}'.format(12)
        '012'

* Float precision to 3 decimals

    .. code-block:: pycon

        >>> '{:.3f}'.format(12.1236)
        '12.124'

* Float precision as a variable

    .. code-block:: pycon

        >>> '{1:.{0}f}'.format(3, 12.1236)
        '12.124'


str.format() - Examples
=======================

* Left pad string to 15 characters

    .. code-block:: pycon

        >>> '{:>15}'.format('hello')
        '          hello'

* Right pad string to 15 characters

    .. code-block:: pycon

        >>> '{:<15}'.format('hello')
        'hello      

* Print representation string for an object

    .. code-block:: pycon

        >>> '{!r}'.format(Exception("something bad Happened"))
        "Exception('something bad Happened',)"


str.format() - Examples
=======================

* Center within 15 characters with underscores

    .. code-block:: pycon

        >>> '{:_^15}'.format('hello')
        '_____hello_____'

* Print as a percentage to two decimal places

    .. code-block:: pycon

        >>> '{:.2%}'.format(0.56)
        '56.00%'

* Perform multiple substitutions with the same value

    .. code-block:: pycon

        >>> '{0}-di, {0}-da'.format('ob-la')
        'ob-la-di, ob-la-da'


F-Strings
=========

* Introduced in Python 3.6
* Allow expressions to be embedded in strings
* Faster than other formatting options

* No backslashes in expressions (OK in string)
* No comments in expressions
* Curly braces are escaped with more curly braces

    .. code-block:: pycon

        >>> name = 'George'
        >>> limit = 732
        >>> f"Hi! My name is {name}. I can count to {max(10, limit)}"
        'Hi! My name is George. I can count to 732'


F-Strings
=========

.. spelling::
    formatSpec

.. image:: /_static/f_strings.svg
   :align: center

* Conversion - same as str.format()
    * ``!s`` -- Convert using :py:func:`str`
    * ``!r`` -- Convert using :py:func:`repr`
    * ``!a`` -- Convert using :py:func:`ascii` (Python 3 Only)

* The format specification (formatSpec) same as str.format()
    * Can be object-specific
    * Most objects use a common language
        * See :py:class:`datetime.datetime` for an object with special formatting

* Raw f strings can be created by prepending **fr**

    .. code-block:: pycon

        >>> interpreted = 'Nope'
        >>> fr'I\'m not interpreted? {interpreted}'
        "I\\'m not interpreted? Nope"


Slicing Sequences
=================

.. spelling::
    len

* Slicing is a flexible method for operating on parts of sequences
* Basic format: sequence[start:end:step]
    * An empty value is interpreted as the default
        * start: 0 (first item)
        * end: 'len(sequence)' (last item)
        * step: 1 (increment index by 1)
    * Does not include the ``end`` value
    * ``:step`` is optional
    * A negative step causes the start to default to the last item


Slicing Sequences - Basic
=========================

* Basic slice

    .. code-block:: pycon

        >>> myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> myList[2:5]
        [2, 3, 4]

        >>> myList[4:]
        [4, 5, 6, 7, 8, 9]

        >>> myList[-3:]
        [7, 8, 9]

        >>> myList[:4]
        [0, 1, 2, 3]

        >>> myList[:]  # Creates a shallow copy of a list
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


Slicing Sequences - Extended
============================

* Extended Slice

    .. code-block:: pycon

        >>> myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> myList[2:8:2]
        [2, 4, 6]
        >>> myList[::-3]
        [9, 6, 3, 0]


Slicing Mutable Sequences
=========================

* Slices of mutable sequences can be changed or deleted

>>> myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del myList[::2]
>>> myList
[1, 3, 5, 7, 9]

>>> myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del myList[:]  # Clear a list
>>> myList
[]

>>> myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> myList[3:5] = ['A', 'B']
>>> myList
[0, 1, 2, 'A', 'B', 5, 6, 7, 8, 9]


Zip
===

* :py:func:`zip` creates a list of tuples with an element from each iterable
    * In Python 3, an iterator of tuples is returned instead of a list
    * Result is only as long as the shortest iterable
* Syntax: zip([iterable, ...])

    .. code-block:: pycon

        >>> input1 = [1, 2 , 3, 4, 5, 6]
        >>> input2 = [2, 4, 6, 8, 10]
        >>> zip(input1, input2)
        [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]


Deep Copying
============

* Some objects like, dictionaries, have a :py:meth:`~dict.copy` method
    * Shallow copy method, does not make copies of the contents

    .. code-block:: pycon

        >>> myDict = {'aList' : [1, 2]}
        >>> newDict = myDict.copy()
        >>> newDict['aList'].append(3)
        >>> myDict['aList']
        [1, 2, 3]

* To copy an object and it's contents, use :py:func:`~copy.deepcopy` from the :py:mod:`copy` module

    .. code-block:: pycon

        >>> import copy
        >>> myDict = {'aList' : [1, 2]}
        >>> newDict = copy.deepcopy(myDict)
        >>> newDict['aList'].append(3)
        >>> myDict['aList']
        [1, 2]

