
.. _lesson5-io:

==============
Lesson 5 - I/O
==============

Command Line Arguments
======================

* To obtain command line arguments for a Python script use :py:data:`sys.argv`
* :py:data:`sys.argv` is a list where :py:data:`sys.argv[0] <sys.argv>` is the script name

    .. code-block:: python

        #!/usr/bin/env python

        import sys

        for argument in sys.argv:
            print(argument)


    .. code-block:: console

        $ ./test.py arg1 arg2 "string with spaces"
        ./test.py
        arg1
        arg2
        string with spaces

* For a framework for command line options, see the :py:mod:`argparse` module


Advanced Command Line Arguments
===============================

* To write Python scripts which take more complicated options use the :py:mod:`argparse` module
    * :py:mod:`argparse` supports short (-o) or long (--option) options
    * Automatically generates help output
    * Checks for required arguments and mutually-exclusive arguments
    * Highly configurable

    .. code-block:: python

        import argparse
        parser = argparse.ArgumentParser(description='Best program, ever!')
        parser.add_argument('-n', '--number', metavar='NUMBER', type=int,
                            required=True, help='Number of time to shout')

        options = parser.parse_args()
        print('Shout! ' * options.number)


User Input
==========

* To get user input, use :py:func:`raw_input` (Python 2) or :py:func:`input` (Python 3)

* Python 2

    .. code-block:: python

        name = raw_input("What is your name? ")
        print "Hi, %s" % name

* Python 3

    .. code-block:: python

        name = input("What is your name? ")
        print("Hi, %s" % name)

* Result

    .. code-block:: console

        What is your name? Avram
        Hi, Avram

User Input
==========

* For version-agnostic user input

    * Standard Library only

        .. code-block:: python

            import sys
            if sys.version_info[0] > 2:
                INPUT = input
            else:
                INPUT = raw_input

            name = INPUT("What is your name? ")

    * Using the `six <https://pythonhosted.org/six/>`_ module

        .. code-block:: python

            from six.moves import input
            name = input("What is your name? ")

File I/O
========

* Open a file with the :py:func:`open` function
    * Supports the following modes:
        * ``r`` -- read (default)
        * ``w`` -- write, truncates file
        * ``x`` -- open for exclusive creation, fails if exists
        * ``a`` -- append to end of a file if it exists
        * ``b`` -- binary mode - read and write as bytes
        * ``t`` -- text mode - read and write as strings (default)
        * ``+`` -- read and write
    * Modes are combined, for example ``r+b`` would open a a file in binary mode without truncation
    * returns a :term:`file object`


File I/O - Close
================

* It is important to make sure file are closed when you are finished with them
* One method of doing this is a ``try``-``finally`` statement
    * Ensures a file is closed even if there is an issue

    .. code-block:: python

        fileObject = open('filename')
        try:
            pass # Do many fancy file things
        finally:
            fileObject.close()

* In Python 2.5 and later, files can be opened using a :keyword:`with` statement
* The file will automatically be closed when the :keyword:`with` statement completes

    .. code-block:: python

        with open('filename') as fileObject:
            pass # Do many fancy file things


File I/O - Read
===============

* Open a file in text mode and read contents as a single string

    .. code-block:: pycon

        >>> with open('/etc/redhat-release') as releaseFile:
        ...     releaseFile.read()
        ... 
        'Fedora release 24 (Twenty Four)\n'

* Open a file in text mode and read contents line by line

    .. code-block:: pycon

        >>> with open('/etc/group') as groupFile:
        ...     groupFile.readline()  # Read the first line
        ...     for line in groupFile:  # Read the rest of the lines
        ...         print(line.strip())
        ... 
        'root:x:0:\n'
        bin:x:1:
        daemon:x:2:
        sys:x:3:


File I/O - Write
================

* When writing to a file object, newline characters must be explicitly added
* Open a file and write a series of random numbers

    .. code-block:: pycon

        >>> import random
        >>> randomGen = random.SystemRandom()
        >>> with open('/tmp/random', 'w') as randomFile:
        ...     for num in range(1, 100):
        ...             randomNum = randomGen.randint(0, 100000)
        ...             randomFile.write('%d\n' % randomNum)
        ... 

    .. code-block:: console

        $ cat /tmp/random
        42380
        30569
        43790
        76564
        ...


File I/O - Combined
===================

* Open multiple files at once

    .. code-block:: pycon

        >>> with open('/etc/group') as groupFile, open('/tmp/group', 'w') as newFile:
        ...     for line in groupFile:
        ...             groupname = line.split(':')[0]
        ...             newFile.write('%s\n' % groupname)
        ... 

* NOTE:
    When using ``write()`` on the Python 3 console, a series of numbers will be printed to the screen.
    This is the number of bytes written.


Standard Streams
================

* The :py:mod:`sys` module includes three special file objects
    * :py:data:`sys.stdin` - Standard In
    * :py:data:`sys.stdout` - Standard Out
    * :py:data:`sys.stderr` - Standard Error

* Write to stdout
    * Use instead of :py:func:`print` when Python <=2.5 must be supported

    .. code-block:: pycon

        >>> sys.stdout.write("Hello, from sunny standard out\n")
        Hello, from sunny standard out

* Write to standard error

    .. code-block:: pycon

        >>> sys.stderr.write("Hello, from the cold depths of standard error\n")
        Hello, from the cold depths of standard error


Standard Streams
================

* Read from standard in

    .. code-block:: python

        #!/usr/bin/env python

        import sys
        input = sys.stdin.readlines()
        input.sort()
        for line in input:
            sys.stdout.write(line.upper())

    .. code-block:: console

        $ cat /etc/group | ./capitalize.py
        ABRT:X:173:
        ADM:X:4:
        AUDIO:X:63:
        AVAHI-AUTOIPD:X:170:
        AVAHI:X:70:
        ...


Exiting
=======

* A Python script will exit with a returncode of 0 if no unhandled exceptions occur
* To exit explicitly, use :py:func:`sys.exit`
    * No arguments or :py:data:`None`, returncode is 0

    .. code-block:: python

        sys.exit()

    * If an integer is given, it will be used as the returncode

    .. code-block:: python

        sys.exit(11)

    * If another object type is given, it is printed using :py:class:`str` to standard error
        * Returncode will be 1

    .. code-block:: python

        if not len(sys.argv) > 1:
            sys.exit("Where are your arguments?")

