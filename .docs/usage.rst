just check out the latest python documentation :  https://docs.python.org/3/library/pathlib.html and select 3.10 Branch

Additional Features are documented here :

PurePath.append_suffix(suffix)
    Return a new path with the suffix appended. If the original path doesn’t have a suffix, the new suffix is appended.
    If the original path have a suffix, the new suffix will be appended at the end.
    If the suffix is an empty string the returned Path does not change.

.. code-block:: python

    >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    >>> p.append_suffix('.bz2')
    PureWindowsPath('c:/Downloads/pathlib.tar.gz.bz2')
    >>> p = PureWindowsPath('README')
    >>> p.append_suffix('.txt')
    PureWindowsPath('README.txt')
    >>> p = PureWindowsPath('README.txt')
    >>> p.append_suffix('')
    PureWindowsPath('README.txt')


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

