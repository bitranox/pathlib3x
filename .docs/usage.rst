just check out the latest python documentation :  https://docs.python.org/3/library/pathlib.html

Additional Features are documented here :

.. code-block::

    # no additional features so far

Caveats
=======

.. code-block::

    >>> import pathlib3x
    >>> import pathlib

    >>> some_path = pathlib3x.Path('some_file')  # this might happen in another module !
    >>> isinstance(some_path, pathlib.Path)
    False

    # in such cases were You need to mix pathlib and pathlib3x probably in different modules, use that:
    >>> str(type(some_path)) == str(type(pathlib.Path()))
    True


So dont mix pathlib with pathlib3x and expect that objects are an instance of Pathlib and vice versa.
This can happen easily if You have many Modules. Just keep it in mind !

