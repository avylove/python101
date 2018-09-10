
.. _lesson1-intro:

=======================
Lesson 1 - Introduction
=======================

Why Python?
===========

.. image:: /_static/xkcd_python_flying.png
   :height: 500px
   :align: center
   :target: https://xkcd.com/353/

`XKCD #353 <https://xkcd.com/353/>`_

Why Python?
===========

* Python is consistently ranked among the top programming languages
    * Currently `second on GitHub`_ (active projects) behind JavaScript
        * Overtook Java in 2017
    * Heavily used in data science and scientific computing
* Extensive ecosystem
    * PyPI contains over 151,000 packages (September 2018)
* Simple
    * Or as complicated as you need
* Integrates with C libraries
    * `C API`_, `ctypes`_, `CFFI`_, `Cython`_, etc
* In demand
    * 67% increase in Python jobs on `Indeed.com <http://www.indeed.com/jobs?q=python&l=>`_ between 2012 and 2016

.. _second on GitHub: https://www.benfrederickson.com/ranking-programming-languages-by-github-users/
.. _C API: https://docs.python.org/c-api/index.html
.. _ctypes: https://docs.python.org/library/ctypes.html
.. _CFFI: http://cffi.readthedocs.org/
.. _Cython: http://cython.org/

History
=======

* Created by `Guido van Rossum <https://en.wikipedia.org/wiki/Guido_van_Rossum>`_
    * From the Netherlands
    * At Dropbox since December 2012
    * Formally at Google, NIST, CNRI
    * Resigned as BDFL (Benevolent Dictator For Life) in July 2018
* Started in December 1989
    * Guido was trying to stay busy while his office was closed for Christmas
    * Named after Monty Python's Flying Circus
        * Python documentation has a lot of references to Monty Python.
            * "eggs" and "spam" is commonly used instead of "foo" and "bar"
            * Example from :ref:`tut-io` in the official Python :ref:`tutorial <tutorial-index>`

                .. code-block:: pycon

                    >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
                    We are the knights who say "Ni!"

Interpreters & Compilers
========================

* `CPython <https://www.python.org/>`_
    * Most popular
    * Reference Implementation
* `PyPy <https://pypy.org/>`_
    * Fast version of Python written in RPython
        - statically-typed subset of CPython
* `Jython <http://www.jython.org/>`_
    * Python that runs on a JVM
* `IronPython <http://ironpython.net/>`_
    * Python for .NET
* `Cython <http://cython.org/>`_
    * Compiles Python code to C
    * Not to be confused with CPython
* Several others


Versions
========

* The current version is 3.7 (3.8 scheduled for October 2019)
    * Python 3 is not backwards compatible with Python 2
    * Compatible code can be written, easier with the `six <https://pythonhosted.org/six/>`_ module

* Python 2.7 was released in July 2010
    * Slated for retirement in 2020
    * Only receives bugfixes and backports to assist in transition to Python 3
    * A lot of code is still Python 2, so we'll see it for a long time
    * `Tauthon <https://github.com/naftaliharris/tauthon>`_ is a project to create an unofficial Python 2.8

Versions in Enterprise Linux
============================

* EL6: 2.6.6
    * Later versions available with `Software Collections <https://www.softwarecollections.org>`_
    * Python 3.4 available in `EPEL <https://fedoraproject.org/wiki/EPEL>`_
* EL7: 2.7.5
    * Later versions available with `Software Collections <https://www.softwarecollections.org>`_
    * Python 3.4 available in `EPEL <https://fedoraproject.org/wiki/EPEL>`_
* EL8: 3.x
    * RHEL 8 will be `Python 3 only <https://www.phoronix.com/scan.php?page=news_item&px=RHEL-8-No-Python-2>`_

Coding Style
============

* `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ is the official style Guide
    * Covers naming, indentation, spacing, etc
    * Some areas are up for interpretation
    * The goal is consistency and readability, not strict adherence

* Summary
    * Indent with 4 spaces, no tabs
    * Constants in UPPERCASE
    * Class names in CapWords
    * Almost everything else in lowercase_with_underscores


Tools - Text Editors
====================

* Console
    * `vim <https://www.vim.org/>`_
        * Set tab to 4 space in .vimrc

            .. code-block:: text

                set tabstop=4
                set shiftwidth=4
                set expandtab
    * `Emacs <https://www.gnu.org/software/emacs/>`_

* GUI
    * `gedit <https://wiki.gnome.org/Apps/Gedit>`_
    * `Atom <https://atom.io/>`_
    * `Sublime Text <https://www.sublimetext.com/>`_

Tools - IDEs
============

* `VSCode <https://code.visualstudio.com/>`_ with Python extension
    - Written in Typescript
    - By Microsoft (Open source)
* `Spyder <https://www.spyder-ide.org/>`_
    - Written in Python
    - Targeted at the scientific community
* `PyCharm <https://www.jetbrains.com/pycharm/>`_
    - Written in Java
    - Commercial and community versions
* `IDLE <https://docs.python.org/library/idle.html>`_
    - Written in Python
    - Basic IDE include with Python


Tools - Linters
===============

* `pylint <https://www.pylint.org/>`_
    * Dynamic linter (Loads code)
    * Looks for style and functional errors
* `pyflakes <https://pypi.org/project/pyflakes/>`_
    * Static style checker
* `pycodestyle <https://pypi.org/project/pycodestyle/>`_
    * Checks code for `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ compliance
* `pydocstyle <https://pypi.org/project/pydocstyle/>`_
    * Checks docstrings for `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_ compliance
* `mccabe <https://pypi.org/project/mccabe/>`_
    * Checks code complexity
* `flake8 <https://pypi.org/project/flake8/>`_
    * Wrapper for pyflakes, pycodestyle, and mccabe

Tools - Other
=============

.. spelling::
    Eval

* Debuggers
    * `pdb <https://docs.python.org/library/pdb.html>`_
        - Built in debugger
    * Most IDEs have graphical debuggers
* Documentation
    * `Sphinx <http://www.sphinx-doc.org>`_
        - Tool for creating documentation from reStructuredText
        - Used (with `Hieroglyph <https://pypi.org/project/hieroglyph/>`_) to create these slides
        - Easy API documentation with `autodoc`_

* Shells
    * REPL (Read–Eval–Print Loop)
        - Built-in console
    * IPython
        - Feature-rich console

.. _autodoc: http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html

Resources
=========

.. spelling::
    Exercism

* Python Documentation
   * https://docs.python.org 
* PEP 8 Style Guide
    * https://www.python.org/dev/peps/pep-0008/
* Python Package Index (PyPI)
    * https://pypi.python.org
* Talk Python to Me Podcast
    * https://talkpython.fm
* Exercism - Coding exercises (beginner to intermediate)
    * http://exercism.io/languages/python
* CheckIO - Coding Game (intermediate to advanced)
    * https://py.checkio.org/


Our First Script
================

* See which version of Python you're running

    .. code-block:: console

        $ python -V
        Python 2.7.12

* Python 2:

    .. code-block:: python

        #!/usr/bin/env python

        # This is a comment
        print "Hello, world"

* Python 3:

    .. code-block:: python

        #!/usr/bin/env python

        # This is a comment
        print("Hello, world")

Our First Script
================

* Execute script

    .. code-block:: console

        $ chmod +x first_script.py
        $ ./first_script.py
        Hello, world
        $ python first_script.py
        Hello, world

Shebang
=======

* Tells the shell where to find the Python interpreter
* ``#!/usr/bin/env python``
    * Uses first ``python`` in $PATH
* ``#!/usr/bin/python``
    * Uses the system default ``python``
* ``#!/usr/bin/python3.6``
    * Uses a specific ``python``
* All options are valid, just different

Using the Python Console
========================

* Enter Console

    .. code-block:: pycon

        $ python
        Python 2.7.12 (default, Aug  9 2016, 15:48:18) 
        [GCC 6.1.1 20160621 (Red Hat 6.1.1-3)] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>>

* Exit Console
    * :py:func:`exit` or ``ctrl-d``

    .. code-block:: pycon

        >>> exit()
        $

* Enter console after running script
    - Useful for troubleshooting

    .. code-block:: console

        $ python -i first_script.py


Using the Python Console
========================

* Hello, world

    * Python 2:

        .. code-block:: pycon

            >>> print "Hello, world"
            Hello, world

    * Python 3:

        .. code-block:: pycon

            >>> print("Hello, world")
            Hello, world

Print: Statement vs Function
============================

* In Python 2 ``print`` is a statement
    - No parentheses
* In Python 3, :py:func:`print` is a function
    - Requires parentheses
* To use the :py:func:`print` in Python 2, hop in a Delorean

        .. code-block:: pycon

            >>> from __future__ import print_function
            >>> print("Hello, world")
            Hello, world

* Bonus Question:
    - Why does ``print("Hello, world")`` produce the same output in Python 2 and 3?
    - Hint: Try ``print(1, 2)``

White Space
===========

* In Python, white space matters
    * Standard indent is 4 space
    * No curly braces for code blocks
    * No semicolons at the end of statements

        * Still used sometimes for one-liners

    * Indent to start a code block
    * Dedent to end a code block
    * Indents must match!

White Space
===========

* Notice the second set of dots? The interpreter is waiting for a dedent.

    .. code-block:: pycon

        >>> for n in [1, 2, 3]:
        ...     print n
        ... 
        1
        2
        3

Comments and Docstrings
=======================

* Comments are preceded by a pound sign ``#``
* Comments can occur on separate lines or at the end of a line

    .. code-block:: python

        # This is a comment
        print('something')  # This is an inline comment

* Docstrings appear at the beginning of a file or object definition
    * Generally in triple-double quotes

    .. code-block:: python

        #!/usr/bin/env python
        """
        This is where you would describe the script
        It is also a good place to include contact and copyright information
        """

Line Continuation
=================

* Appending a backslash ``\`` to the end of a line will cause it to continue to the next line
* Strings are automatically concatenated

    .. code-block:: pycon

        >>> myString = "This is the string the never ends. " \
        ...     "It just goes on and on, my friend."
        >>> myString
        "This is the string the never ends. It just goes on and on, my friend."

* Open parentheses, braces and brackets imply a line continuation

    .. code-block:: pycon

        >>> print(
        ...       'something')
        something


Imports
=======

* Additional functions, classes, and objects can be imported from modules
* Modules are simply a Python file
* Packages are collections of modules or subpackages
    * Example: :py:mod:`urllib.request` is a module in the :py:mod:`urllib` package
* A lot of very useful modules and packages are shipped with Python
    * This is called :ref:`library-index`
* Many other modules and packages can be found online
    * The biggest repository is `The Python Package Index <https://pypi.python.org>`_
    * Many of the most popular packages are available from Red Hat or `EPEL <https://fedoraproject.org/wiki/EPEL>`_
* Imports are managed with the :keyword:`import` statement

Imports
=======

* Import a module

    .. code-block:: pycon

        >>> import sys
        >>> sys.version_info
        sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)

* Import module with a different name

    .. code-block:: pycon

        >>> import sys as system
        >>> system.version_info
        sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)

* Import objects from a module
    * Notice the module name is not given when calling :py:data:`~sys.version_info`

    .. code-block:: pycon

        >>> from sys import version, version_info
        >>> version_info
        sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)

Imports
=======

* Sometime you will see a star in the import line
    .. code-block:: pycon

        >>> from sys import *

    * **Don't do this!**
    * This means import "everything" from a module
        * What "everything" includes is configurable with a module
    * Wildcard imports can lead to unexpected behavior


Imports - Module Search Path
============================

* The module search path is installation dependent
* The current path can be displayed with :py:data:`sys.path`

    .. code-block:: pycon

        >>> sys.path
        ['', '/usr/lib64/python35.zip', '/usr/lib64/python3.5',
        '/usr/lib64/python3.5/plat-linux', '/usr/lib64/python3.5/lib-dynload',
        '/usr/lib64/python3.5/site-packages', '/usr/lib/python3.5/site-packages']

* When running a script, the directory the script is in is the first in the search path
    * This is not the same as the current working directory

* The path can be prepended with the :envvar:`PYTHONPATH` environment variable

    .. code-block:: console

        $ PYTHONPATH=/usr/share/superpython:/usr/share/superduperpython python


Standard Library
================

* A collection of packages and modules shipped with Python
* Provides standard solutions for common problems
* Provides standard interfaces for low level or OS-specific operations
* Refer to the `documentation <https://docs.python.org/library>`_ for a complete list
* Highlights
    * `sys <https://docs.python.org/library/sys.html>`_ — System-specific parameters and functions
    * `os <https://docs.python.org/library/os.html>`_ — Miscellaneous operating system interfaces
    * `glob <https://docs.python.org/library/glob.html>`_ — Unix style pathname pattern expansion
    * `shutil <https://docs.python.org/library/shutil.html>`_ — High-level file operations
    * `re <https://docs.python.org/library/re.html>`_ — Regular expression operations
    * `random <https://docs.python.org/library/random.html>`_ — Generate pseudo-random numbers
    * `time <https://docs.python.org/library/time.html>`_ — Time access and conversions (lower level)
    * `datetime <https://docs.python.org/library/datetime.html>`_ — Basic date and time types (higher level)


Online Help
===========

* The :py:func:`help` function, allows help access directly from the Python console
    * If the argument is a string, the topic will be searched for
    * Any other object will bring up help for that object type or class
        .. code-block:: pycon

            >>> help('tuple')
            >>> help(tuple)
            >>> help(myTuple)

* Help is also available from the command line with the ``pydoc`` command
    .. code-block:: console

        $ pydoc tuple

* Objects can also be inspected, using the :py:func:`dir` function
    * Implementation can vary by object type
    * Generally lists attributes and methods associated with an object

