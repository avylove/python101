
.. _lesson4-flow-control:

=======================
Lesson 4 - Flow Control
=======================

Conditional - if
================

* Execute a code block if a condition is true

    .. code-block:: pycon

        >>> x = 0
        >>> if x == 0:
        ...     print("Zero")
        ...
        Zero


Conditional - else
==================

* Provide a fallback code block using ``else``

    .. code-block:: pycon

        >>> x = 1
        >>> if x == 0:
        ...     print("Zero")
        ... else:
        ...     print("Non-zero number")
        ...
        Non-zero number


Conditional - elif
==================

.. spelling::
    elif

* Combine an  else and if statement with ``elif``

    .. code-block:: pycon

        >>> x = 2
        >>> if x == 0:
        ...     print("Zero")
        ... elif x % 2:
        ...     print("odd number")
        ... else:
        ...     print("Even number")
        ...
        Even number


Implicit Boolean
================

* Non-zero numbers and non-empty iterables are considered True
* These statements are equivalent for an iterable

    .. code-block:: python

        if len(myIterable) > 0:

        if len(myIterable):

        if myIterable:

* These statements are equivalent for a number

    .. code-block:: python

        if myNumber != 0:

        if myNumber


Implicit Boolean
================

* Return True if any elements in an iterable evaluate to True

    .. code-block:: pycon

        >>> any([0, 1, 0])
        True

* Return True if all elements in an iterable evaluate to True

    .. code-block:: pycon

        >>> all([True, 'string', [3, 4], 2])
        True

Conditional Loop - while
========================

* Loop until condition is false

    .. code-block:: pycon

        >>> x = 1
        >>> while x <= 3:
        ...     print(x)
        ...     x += 1
        ...
        1
        2
        3


Conditional Loop - break
========================

* :ref:`break <break>` is used to end a loop

    .. code-block:: pycon

        >>> x = 1
        >>> while True:
        ...     print(x)
        ...     x += 1
        ...     if x > 3:
        ...             break
        ...
        1
        2
        3


Conditional Loop - else
=======================

* An ``else`` statement can be used to execute code whenever a while condition is false
* Not executed when ``break`` is used

    .. code-block:: pycon

        >>> x = 1
        >>> while x <= 3:
        ...     print(x)
        ...     x += 1
        ... else:
        ...     print("I can only count to twee!")
        ...
        1
        2
        3
        I can only count to twee!


Iteration - for
===============

* Loop over all values in an Iterable

    .. code-block:: pycon

        >>> bears = ['Papa', 'Mama', 'Baby']
        >>> for bear in bears:
        ...     print(bear)
        ... 
        Papa
        Mama
        Baby


Iteration - continue
====================

* :ref:`continue <continue>` is used to continue with a loop

    .. code-block:: pycon

        >>> for num in [1, 2, 3]:
        ...     if num % 2:
        ...             continue
        ...     print(2, "Even!")
        ...
        2 Even!


Iteration - break
=================

* :ref:`break <break>` is used to end a loop before completion

    .. code-block:: pycon

        >>> deadly = ['hippo', 'aligator', 'python']
        >>> for animal in ['rabbit', 'horse', 'hippo', 'mouse']:
        ...     print('What a cute %s!' % animal)
        ...     if animal in deadly:
        ...             print('Oops!')
        ...             break
        ...
        What a cute rabbit!
        What a cute horse!
        What a cute hippo!
        Oops!


Iteration - else
================

* When a loop fails to iterate, else can be used to run fallback code
* This happens when a list is empty

    .. code-block:: pycon

        numbers = []
        >>> for num in numbers:
        ...     print(num)
        ... else:
        ...     print("Where are the numbers?")
        ...
        Where are the numbers?



Iteration - range
=================

* The :py:func:`range` function can be used to iterate over integers
* Format is range(start, stop[, step])

    .. code-block:: pycon

        >>> for num in range(1, 3):
        ...     print(num)
        ...
        1
        2
        >>> for num in range(2, 6, 2):
        ...     print(num)
        ...
        2
        4
        >>> for num in range(2, 0, -1):
        ...     print(num)
        ...
        2
        1

Iteration - enumerate
=====================

* The :py:func:`enumerate` function returns tuples with a count and items from an iterable
* Count starts at 0 by default
* Format is enumerate(iterable, start=0)

    .. code-block:: pycon

        >>> for num, entry in enumerate(['A', 'B', 'C'], 1):
        ...     print(num, entry)
        ...
        1 A
        2 B
        3 C


List Comprehension
==================

* List comprehension allows creating lists from inline :py:keyword:`for` loops

    .. code-block:: pycon

        >>> numbers = [-2, -1, 0, 1, 2, 3, 4]
        # Square all numbers in a list
        ... squares = [x**2 for x in numbers]
        >>> squares
        [4, 1, 0, 1, 4, 9, 16]

        # Square even numbers in a list
        ... evenSquares = [x**2 for x in myList if not x % 2]
        >>> evenSquares
        [4, 0, 4, 16]

* Can be used in other expressions

    .. code-block:: pycon

        >>> sum([x**2 for x in numbers])
        35


Set and Dictionary Comprehension
================================

* In Python 2.7 and later, set and dictionary comprehension are available
* Set comprehension

    .. code-block:: pycon

        >>> numbers = [-2, -1, 0, 1, 2, 3, 4]  
        >>> {x**2 for x in numbers}
        {0, 1, 4, 9, 16}

    * Notice the new set syntax introduced in Python 2.7

* Dictionary comprehension

    .. code-block:: pycon

        >>> {x : x**2 for x in numbers}
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, -2: 4, -1: 1}


Exceptions
==========

* When an error occurs, an exception is raised

    .. code-block:: pycon

        >>> int('A')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        ValueError: invalid literal for int() with base 10: 'A'

* Exceptions include:
    * The type of exception
    * An error message
    * A traceback showing what code was being executed

* Exceptions are not always bad, sometimes they are expected behavior


Common Exceptions
=================

.. hlist::
    :columns: 2

    * AttributeError
    * EOFError
    * ImportError
    * IndexError
    * IOError
    * KeyError
    * KeyboardInterrupt
    * MemoryError
    * NameError
    * NotImplementedError
    * OSError
    * SystemExit
    * TimeoutError
    * Type Error
    * ValueError
    * ZeroDivisionError


* For a more complete list
    * see :ref:`bltin-exceptions` in the Python documentation
    * ``pydoc exceptions``

* All built-in exceptions are children of the :py:exc:`Exception` class

Catching Exceptions
===================

* Common use cases
    * Validation
        * When errors are uncommon, it is faster to catch errors than check all data
    * Calling an external function
        * Smoothly handle unexpected issues that may arise calling external code
    * External environments
        * Unpredictable and can change without notification
            * Operating system - Unsupported operations, resources unavailable
            * Filesystems - Permission issues, file doesn't exist
            * Network resource - Network or resource down


Catching Exceptions
===================

* Exceptions can be caught using a ``try``-``except`` statement

    .. code-block:: pycon

        >>> try:
        ...     int('A')
        ... except ValueError:
        ...     print('That value is invalid, please provide an integer')
        ... 
        That value is invalid, please provide an integer

* Tips
    * Very general exceptions may catch something unexpected
    * Put only the code that will raise an exception in the try block


Catching Exceptions - Multiple Exceptions
=========================================

* Multiple exceptions can be listed in a tuple

    .. code-block:: python

        try:
            os.listdir(someDirectory)
        except (OSError, IOError):
            print("Error opening %s" % someDirectory)


* Multiple ``except`` statements can be used to handle different conditions

    .. code-block:: python

        try:
            ...
        except IOError:
            ...
        except RuntimeError:
            ...
        except KeyError
            ...


Catching Exceptions - else
==========================

* An else block can be used to execute code when no exception is raised

    .. code-block:: python

        def divide(num1, num2):
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Nope, still can't divided by zero")
            else:
                print("Result is %f" % result)


Catching Exceptions - finally
=============================

* A ``finally`` can be included to execute code under all conditions
* ``finally`` blocks are executed after all other code
* If an unhandled exception occurs, the ``finally`` block will be executed before it is raised
* Useful for closing files, releasing locks, or other cleanup tasks

    .. code-block:: python

        lock.acquire()

        try:
            ...
        except IOError:
            ...
        finally:
            lock.release()


Catching Exceptions - Reuse
===========================

* In Python 2.6+ the exception can be caught with the ``as`` keyword

    .. code-block:: pycon

        >>> try:
        ...     1/0
        ... except ZeroDivisionError as e:
        ...     print('An error occured: %s' % e)
        ... 
        An error occured: division by zero

* To write code compatible with older versions of Python, use :py:func:`sys.exc_info`

    .. code-block:: pycon

        >>> try:
        ...     1/0
        ... except ZeroDivisionError:
        ...     e = sys.exc_info()[1]
        ...     print('An error occured: %s' % e)
        ... 
        An error occured: division by zero


Catching Exceptions - Reuse
===========================

* Exceptions can be re-raised after they are caught
* :keyword:`raise` with no arguments will re-raise the last exception

>>> try:
...     1/0
... except ZeroDivisionError:
...     print('Seriously, stop trying to divide by zero!')
...     raise
... 
Seriously, stop trying to divide by zero!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero


Exceptions - Raising
====================

* Exceptions can be raised with the :keyword:`raise` keyword

    .. code-block:: pycon

        >>> raise RuntimeError("This parrot is no more! ")
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        RuntimeError: This parrot is no more! 


Exceptions - Creating
=====================

* Here are simple examples for creating custom exceptions
    * Class will be covered in another lesson

    .. code-block:: python

        class CustomException(Exception):
            """
            Custom exception description
            """
            pass


        class CustomExceptionChild(CustomException):
            """
            Child of Custom exception description
            """
            pass

* Custom exceptions should be created hierarchically

