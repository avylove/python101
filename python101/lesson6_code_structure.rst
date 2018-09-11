
.. _lesson6-code-structure:

=========================
Lesson 6 - Code Structure
=========================

Functions
=========

* Define a function with the :ref:`def <def>` keyword
* Define 0 or more parameters
* Use :ref:`return <return>` to return a value
* Accepts an optional docstring

    .. code-block:: python

        def add(num1, num2):
            """
            This is where I should describe what this function does
            """
            result = num1 + num2
            return result

    .. code-block:: pycon

        >>> add(1, 7)
        8


Functions - Multiple Returns
============================

* When multiple values are passed to ``return``, the result is a tuple

    .. code-block:: pycon

        >>> def add_and_multiply(num1, num2):
        ...     return num1 + num2, num1 * num2
        ... 
        >>> add_and_multiply(1, 7)
        (8, 7)
        >>> added, multiplied = add_and_multiply(1, 7)
        >>> print(added)
        8
        >>> print(multiplied)
        7


Functions - Arbitrary Arguments
===============================

* Functions can take an arbitrary number of arguments
* Useful for iteration or when passing options to another function

    .. code-block:: pycon

        >>> def add(num1, num2, *args):
        ...     result = num1 + num2
        ...     for num in args:
        ...             result += num
        ...     return result
        ...
        >>> add(1, 2, 3, 4, 5)
        15

        >>> def add_wrapper(*args):
        ...     return add(*args)
        ...
        >>> add_wrapper(1, 2, 3, 4, 5)
        15


Functions - Optional Arguments
==============================

.. spelling:: 
    args
    kwargs

* A default value can be set for optional arguments
* Optional arguments must come after non-optional arguments
* Optional arguments must come before \*args and \*\*kwargs

    .. code-block:: pycon

        >>> def word_game(name, noun1='gun', noun2='cannoli'):
        ...     print('%s: "Leave the %s, take the %s."' % (name, noun1, noun2))
        ...
        >>> word_game('Peter Clemenza')
        Peter Clemenza: "Leave the gun, take the cannoli."

        >>> word_game('Indiana Jones', 'snakes', 'ark')
        Indiana Jones: "Leave the snakes, take the ark."

        >>> word_game('Cookie Monster', noun2='cookies')
        Cookie Monster: "Leave the gun, take the cookies."


Functions - Keywords
====================

* Keyword arguments are preceded by an identifier
* Must come after positional arguments

    .. code-block:: pycon

        >>> word_game('Cookie Monster', noun2='cookies')
        Cookie Monster: "Leave the gun, take the cookies."

* Keywords which aren't formal parameters can be collected in a dictionary

    .. code-block:: pycon

        >>> def scores(game, **kwargs):
        ...     print(game.capitalize() + ' scores:')
        ...     for key, value in kwargs.items():
        ...             print('  %s : %d' % (key,value))
        ...
        >>> scores('jumprope', John=20, George=19, Paul=12, Ringo=126)
        Jumprope scores:
          Ringo : 126
          Paul : 12
          John : 20
          George : 19


Functions - Scope
=================

* When a function is called it has it's own namespace
* Variables in outer scopes can be read from within a function
* By default, non-local variables can not be changed

    .. code-block:: python

        ANSWER = 42

        def what_is_the_answer():
            return ANSWER

        def change_the_answer(answer):
            ANSWER = answer

    .. code-block:: pycon

        >>> change_the_answer(41)
        >>> what_is_the_answer()
        42


Functions - Scope
=================

* The :keyword:`global` and :keyword:`nonlocal` keywords can be used to change variables outside of a function
    * If you need this, you are probably doing something weird
        * (These are not the variables you're looking for)


Lambda Expressions
==================

* Lambda expressions are small functions that can be used in-line

    .. code-block:: pycon

        >>> add = lambda x, y: x + y
        >>> add(1, 2)
        3

        >>> def make_power_function(base):
        ...     return lambda x: base ** x
        ... 
        >>> pow2 = make_power_function(2)
        >>> pow2(3)
        8

        >>> ages = [('Jane', 20), ('Joe', 18), ('Jasmine', 26), ('John', 16)]
        >>> ages.sort(key=lambda age: age[1])
        >>> ages
        [('John', 16), ('Joe', 18), ('Jane', 20), ('Jasmine', 26)]


Filter
======

* :py:func:`filter` creates a list from an iterable when a function is true
    * In Python 3, an iterator is returned instead of a list
* Syntax: filter(function, iterable)

    .. code-block:: pycon

        >>> input = ["1", "2", "three", "banana", "6"]
        >>> filter(lambda x: x.isdigit(), input)
        ['1', '2', '6']

    * This is equivalent to:

        .. code-block:: pycon

            >>> [x for x in input if x.isdigit()]
            ['1', '2', '6']


Map
===

* :py:func:`map` creates a list by performing an operation on each member of an iterable
    * In Python 3, an iterator is returned instead of a list
* Syntax: filter(function, iterable [, iterable ...])
    * If multiple iterators are supplied, the function must take as many inputs

    .. code-block:: pycon

        >>> input = [1, 2, 3, 4, 5, 6]
        >>> map(lambda x: x ** 2, input)
        [1, 4, 9, 16, 25, 36]
        # Same as [x ** 2 for x in input]

    .. code-block:: pycon

        >>> input1 = [1, 2 , 3, 4, 5, 6]
        >>> input2 = [2, 4, 6, 8, 10, 12]
        >>> map(lambda x, y: x * y, input1, input2)
        [2, 8, 18, 32, 50, 72]
        # Same as [x * y for x, y in zip(input1, input2)]


Pass Statement
==============

* The :keyword:`pass` statement is a null operator
* It does nothing
* Useful as a placeholder for future code

    .. code-block:: pycon

        >>> if x == 0:
        ...     pass  # Tony Stark said he would handle this
        ... else:
        ...     print("x is not 0!")


Checking Datatypes
==================

* Sometimes you might want to perform an operation only on specific datatypes
* :py:func:`isinstance` can be used to test for specific instances types

    .. code-block:: pycon

        >>> if isinstance(var1, list):  # Test if var1 is a list
        ...     print("Lists are cool!")

        >>> if isinstance(var1, (list, tuple)):  # Test if var1 is a list or a tuple
        ...     print("I see you enjoy a good sequence.")

* To check against datatype categories use the :py:mod:`collections.abc` module.
    - :py:mod:`collections` before Python 3.3

    .. code-block:: pycon

        >>> from collections.abc import Sequence
        >>> isinstance([1, 2], Sequence)
        True


Decorators
==========

* At times it is useful to wrap a function in another function
    * Change arguments
    * Change return values
    * Additional functionality

* A function can be created that takes another function as an argument

    .. code-block:: python

        def force_string(func):
            """
            The main function, takes a function and wraps it
            """

            def wrapper(*args, **kwargs):
                """
                The wrapper function. This is what does the real work
                """
                return str(func(*args, **kwargs))

            return wrapper


Decorators
==========

* Wrapping a function is called "decorating"

    .. code-block:: python

        def multiply(num1, num2):
            """
            A simple multiple function
            """
            return num1 * num2

        multiply_wrapped = force_string(multiply)
        multiply_wrapped(2, 3)  # Returns "6" as a string

* If we wanted the wrapped function to have the same name

    .. code-block:: python

        multiply = force_string(multiply)
        multiply(2, 3)  # Returns "6" as a string


Decorators
==========

* Python provides a decorator syntax that can be applied to functions

    .. code-block:: python

        @force_string
        def multiply(num1, num2):
            """
            A simple multiple function
            """
            return num1 * num2

        multiply(2, 3)  # Returns "6" as a string


Generators
==========

* Generators support single use iteration
* Generators process an iteration only when an element is requested (lazy)
* The :py:keyword:`yield` statement returns a value and pauses processing
    * Processing resumes when ``__next__()`` is called
        * ``next()`` in Python 2

    .. code-block:: python

        def range2(start, end):
            current = start
            while current < end:
                yield current
                current += 1


Generators
==========

* When a generator is complete, a :py:exc:`StopIteration` exception is raised

    .. code-block:: pycon

        >>> numbers = range2(1, 10)
        >>> type(numbers)
        <type 'generator'>
        >>> numbers.next()
        1
        >>> numbers.next()
        2
        >>> # StopIteration is caught internally
        ... list(numbers)
        [3, 4, 5, 6, 7, 8, 9]
        >>> numbers.next()
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration


Dunder Main
===========
* All Python files are modules
    * Any code not in a function or class is executed at import
* Most code in a module should be contained within functions or classes
* Modules executed directly should use a dunder main test

    .. code-block:: python

        if __name__ == '__main__':
            # Running as the main program
            ...

* A common practice is to place the main logic in a function

    .. code-block:: python

        def main():
            # Do useful things here
            ...

        if __name__ == '__main__':
            main()


Modules - Creating
==================

* For a module that will never be executed directly
    * Do **NOT** include a shebang
    * Ensure it is not executable
    * Ensure all code is contained in functions or classes
    * Create docstrings


Modules - Creating
==================

.. spelling::
    mymath
    py

* A sample module
    * Create a file called mymath.py

    .. code-block:: python

        """
        Pretty much the best math module ever
        """

        def add(num1, num2):
            """
            Add two numbers
            """
            return num1 + num2

        def multiply(num1, num2):
            """
            Multiply two numbers
            """
            return num1 * num2


Modules - Creating
==================

* Run ``python`` in the same directory

    .. code-block:: pycon

        >>> import mymath
        >>> mymath.add(1, 3)
        4
        >>> mymath.multiply(2, 6)
        12

        >>> help(mymath)


Modules - Creating a Package
============================

* Packages require a directory with an ``__init__.py`` file
    * ``__init__.py`` files generally have very little, if any, code

    .. code-block:: console

        $ mkdir mypackage
        $ touch mypackage/__init__.py
        $ mv mymath.py mypackage/

    .. code-block:: pycon

        >>> import mypackage.mymath
        >>> mypackage.mymath.add(3, 4)
        7
        >>> mypackage.mymath.multiply(3, 4)
        12


Private Objects
===============

* Sometimes an object (variable, function, class, etc) is not intended for general use
* Private object names should begin with a single underscore
* Private objects are not imported with '*'
* Some linters will warn about using private objects

    .. code-block:: python

        def _multiply(num1, num2):
            return num1 * num2

        def _add(num1, num2):
            return num1 + num2

        def add_and_multiply(num1, num2):
            return _add(num1, num2), _multiply(num1, num2)





