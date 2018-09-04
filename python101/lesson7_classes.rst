.. _lesson7-classes:

==================
Lesson 7 - Classes
==================


Classes - Overview
==================

* Classes are fundamental to object-oriented programming
* Classes are template containers for attributes (variables) and methods (functions)


Classes - Empty
===============

* A basic class definition includes a name and parent(s)
    * :py:class:`object` is the standard base class
    * Class names should be written in CapWords format

    .. code-block:: python

        class EmptyClass(object):
            """
            This is an empty class called EmptyClass
            """

            pass


Class Instances
===============

* Instances are created from classes
* Instances are also called objects

    .. code-block:: python

        class Dog(object):
            """
            This is an empty class called dog
            Think of it as the definition of a dog
            """

            pass

        # My dog spot is the actual dog
        my_dog_spot = Dog()

* Use :py:func:`isinstance` to check if an object is an instance of specific classes

    .. code-block:: pycon

        >>> isinstance(my_dog_spot, Dog)
        True



Class Attributes
================

* Class attributes are variables assigned statically with a class

    .. code-block:: python

        class Car(object):
            """
            This is a simple class called Car
            It has one class attribute, wheels
            """

            wheels = 4

* Attributes can be accessed in the class or in a class instance

    .. code-block:: pycon

        >>> Car.wheels
        4
        >>> myCar.wheels
        4


Class Attributes
================

* If a class attribute is changed, it affects all instances and children

    .. code-block:: pycon

        >>> Car.wheels = 5
        >>> myCar.wheels
        5

* If a class attribute is redefined for an instance, it becomes an instance attribute
    * Instance attributes are only specific to the instance they are defined in

    .. code-block:: pycon

        >>> myCar.wheels = 3
        >>> myCar.wheels
        3
        >>> Car.wheels
        5


Methods
=======

* Methods are functions defined within a class

    .. code-block:: python

        class Car(object):
            """
            This is a simple class called Car
            It has one class attribute, wheels
            """

            wheels = 4

            def wheel_count(self):
                return self.wheels

    .. code-block:: pycon

        >>> myCar = Car()
        >>> myCar.wheel_count()
        4

Self
====

* ``self`` is the first argument to a standard method
* ``self`` is a reference to the current instance
* ``self`` is a convention and can technically be called anything
* The instance is automatically passed as the first argument to a method call

    .. code-block:: python

        class SampleClass(object):
            """
            A simple class to show self
            """

            def know_thyself(self):
                print("I am %s" % self)

    .. code-block:: pycon

        >>> myInstance = SampleClass()
        >>> myInstance.know_thyself()
        I am <__main__.SampleClass object at 0x7fc70f98d990>


Class Initialization
====================

* A special method :py:meth:`__init__() <object.init>` is used to customize a class
* Generally used for validation and to set instance attributes
* Takes arguments, but should not return anything

    .. code-block:: python

        class Car(object):

            wheels = 4

            def __init__(self, fuel='gas', doors=4):
                self.fuel_type = fuel
                self.door_count = doors

    .. code-block:: pycon

        >>> myTeslaModel3 = Car('electric')
        >>> myTeslaModel3.fuel_type
        'electric'
        >>> myTeslaModel3.door_count
        4


Attributes - Methods
====================

* In standard methods, ``self`` can be used to access attributes

    .. code-block:: python

        class Car(object):

            wheels = 4

            def __init__(self, fuel='gas', doors=4):
                self.fuel_type = fuel
                self.door_count = doors

            def get_groceries(self):
                if self.door_count > 2:
                    return True
                else:
                    return False

    .. code-block:: pycon

        >>> myTeslaModel3 = Car('electric')
        >>> myTeslaModel3.get_groceries()
        True


Attributes - Access Functions
=============================

* :py:func:`getattr` provides another way to get attributes
    * Syntax: ``getattr(object, name[, default])``
    * ``getattr(object, name)`` is equivalent to ``object.name``

    .. code-block:: pycon

        >>> getattr(myTeslaModel3, 'fuel_type')
        'electric'

        >>> getattr(myTeslaModel3, 'flux_cap_type')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        AttributeError: 'Car' object has no attribute 'flux_cap_type'

        >>> getattr(myTeslaModel3, 'flux_cap_type', 'Mr. Fusion')
        'Mr. Fusion'


Attributes - Access Functions
=============================

* :py:func:`hasattr` provides a way to to check if an attribute exists
    * Syntax: ``hasattr(object, name)``

    .. code-block:: pycon

        >>> hasattr(myTeslaModel3, 'fuel_type')
        True
        >>> hasattr(myTeslaModel3, 'flux_cap_type')
        False


Attributes - Access Functions
=============================

* :py:func:`setattr` provides a way to set attributes
    * Syntax: ``setattr(object, name, value)``
    * Equivalent to ``object.name = value``

    .. code-block:: pycon

        >>> setattr(myTeslaModel3, 'flux_cap_type', 'Mr. Fusion')
        >>> myTeslaModel3.flux_cap_type
        'Mr. Fusion'

* :py:func:`delattr` provides a way to delete attributes
    * Syntax: ``delattr(object, name)``
    * Equivalent to ``del object.name``

    .. code-block:: pycon

        >>> delattr(myTeslaModel3, 'flux_cap_type')
        >>> hasattr(myTeslaModel3, 'flux_cap_type')
        False

Class Methods
=============

* Class methods operate on a class rather than an instance
* The first argument is ``cls`` by convention
* Create a class method with the :py:func:`classmethod` decorator

    .. code-block:: python

        class Car(object):

            def __init__(self, fuel='gas', doors=4):
                self.fuel_type = fuel
                self.door_count = doors

            @classmethod
            def station_wagon(cls, fuel='gas'):
                return cls(fuel, 5)

    .. code-block:: pycon

        >>> myWagon = Car.station_wagon()
        >>> myWagon.door_count
        5

Static Methods
==============

* Static methods do not operate on instances or classes
* Regular functions included in a class
* Useful for related utility functions
* Create a static method with the :py:func:`staticmethod` decorator

    .. code-block:: python

        class Car(object):

            @staticmethod
            def honk_horn():
                print("Beep!\a")

    .. code-block:: pycon

        >>> myTeslaModel3 = Car()
        >>> myTeslaModel3.honk_horn()
        Beep!
        >>> Car.honk_horn()
        Beep!


Properties
==========

* Properties allow attributes to be backed by methods
* Create a property with the :py:func:`property` decorator

    .. code-block:: python

        import time

        class Product(object):

            @property
            def serial(self):
                if not hasattr(self, '_serial'):
                    self._serial = time.time()
                return self._serial

    .. code-block:: pycon

        >>> widget = Product()
        >>> widget.serial
        1474583633.99423
        >>> widget.serial
        1474583633.99423


Properties
==========

* Properties also provide a way to call a method for assignment

    .. code-block:: python

        import time

        class Product(object):

            @property
            def serial(self):
                if not hasattr(self, '_serial'):
                    self._serial = time.time()
                return self._serial

            @serial.setter
            def serial(self, value):
                if not isinstance(value, float):
                    raise TypeError('serial must be a float')
                self._serial = value

Properties
==========

* The setter method will be called during assignment
* Uses:
    * Validation
    * When the value is stored in another object (ex: dictionary, class)

    .. code-block:: pycon

        >>> widget = Product()
        >>> widget.serial = "ABC"
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "<stdin>", line 10, in serial
        TypeError: serial must be a float
        >>> widget.serial = 1.0
        >>> widget.serial
        1.0

Inheritance
===========

* A subclass can be created from any class
    * Allows specialization

    .. code-block:: python

        class Fruit(object):
            """
            Fruit base class
            """

            def eat(self):
                print("Yum!")

        class Banana(Fruit):
            """
            Banana subclass
            """

            def peel(self):
                print("Banana's are aPEELing!")


Inheritance
===========

* Subclasses inherit methods and attributes from base classes

    .. code-block:: pycon

        >>> myBanana = Banana()
        >>> myBanana.eat()  # Provided in Fruit base class
        Yum!
        >>> myBanana.peel()  # Provided in Banana subclass class
        Banana's are aPEELing!

        >>> isinstance(myBanana, Banana)
        True

        >>> isinstance(myBanana, Fruit)
        True

* Use :py:func:`issubclass` to check inheritance

        >>> issubclass(Banana, Fruit)
        True


Inheritance - Overwriting
==========================

* Methods and attributes can also be overwritten
    * Parent methods and attributes can still be utilized

    .. code-block:: python

        class Car(object):

            wheels = 4

            def __init__(self, fuel='gas', doors=4):
                self.fuel_type = fuel
                self.door_count = doors

        class TeslaModel3(Car):

            def __init__(self, battery=65):
                Car.__init__(self, 'electric', 4)
                self.battery_size = battery


Inheritance - super
===================

* :py:func:`super` is used to access ancestor methods and attributes
* Syntax: super(type[, object-or-type])
    * type is optional in Python 3
* Provides a more flexible way to access parent

    .. code-block:: python

        class TeslaModel3(Car):

            def __init__(self, battery=65):
                super(TeslaModel3, self).__init__(self, 'electric', 4)
                self.battery_size = battery


Abstract Methods
================

* An abstract method declared, but not implemented
    * Intended to be defined in a subclass

    .. code-block:: python

        class Car(object):
            def contact_dealer(self):
                raise NotImplementedError

        class TeslaModel3(Car):
            def contact_dealer(self):
                print("Call 1-888-51-TESLA")

    .. code-block:: pycon

        >>> Car().contact_dealer()
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "<stdin>", line 3, in contact_dealer
        NotImplementedError
        >>> TeslaModel3().contact_dealer()
        Call 1-888-51-TESLA

Multiple Inheritance
====================

* Classes can have multiple parents
* Can get complicated, use rarely and sparingly

    .. code-block:: python

        class Car(object):
            wheels = 4

        class Tesla(object):
            def contact_dealer(self):
                print("Call 1-888-51-TESLA")

        class TeslaModel3(Car, Tesla):
            pass

    .. code-block:: pycon

        >>> TeslaModel3.wheels
        4
        >>> TeslaModel3().contact_dealer()
        Call 1-888-51-TESLA


Iterators
=========

* An iterator is a specialized type of generator
    * Iterators have an extra method :py:meth:`~iterator.__iter__` that returns itself
* Iterators are generally not accessed directly
    * Provided by other objects to support iteration
* Many functions that previously returned lists return objects with iterators in Python 3
    * Makes the code more efficient (lazy processing)
    * Example: :py:meth:`dict.keys` behaves like ``dict.iterkeys()`` did in Python 2
    * To convert to a list, use :py:class:`list`

    .. code-block:: pycon

        >>> myDict = {'a' : 1, 'b' : 2, 'c' : 3}
        >>> myDict.keys()
        dict_keys(['a', 'b', 'c'])
        >>> list(myDict.keys())
        ['a', 'b', 'c']


Iterators
=========

* To create an iterable object, create a generator method called ``__iter__()``
    * ``__iter__()`` will automatically return an iterator

    .. code-block:: python

        class range2(object):

            def __init__(self, start, end):
                self.start = start
                self.end = end

            def __iter__(self):
                current = self.start
                while current < self.end:
                    yield current
                    current += 1


Iterators
=========

    .. code-block:: pycon

        >>> numbers = range2(1, 10)
        >>> numbers
        <__main__.range2 object at 0x7fc389a77cc0>
        >>> list(numbers)
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> list(numbers)
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

        >>> numbers.__iter__()
        <generator object range2.__iter__ at 0x7fc38b0b6410>
        >>> numbers.__iter__()
        <generator object range2.__iter__ at 0x7fc38b0b6620>

        >>> numbersIterator = numbers.__iter__()
        >>> numbersIterator.__iter__() is numbersIterator
        True


