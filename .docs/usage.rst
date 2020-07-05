just check out the latest python documentation :  https://docs.python.org/3/library/pathlib.html and select 3.10 Branch

Additional Features are documented here :

PurePath.append_suffix(suffix)
    Return a new path with the *suffix* appended. If the original path doesn’t have a suffix, the new suffix is appended.
    If the original path have a suffix, the new suffix will be appended at the end.
    If *suffix* is an empty string the original Path will be returned.

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


PurePath.is_path_instance(__obj)
    Return True if *__obj* is instance of the original pathlib.Path or pathlib3x.Path.
    Useful if You need to check for Path type, in an environment were You mix pathlib and pathlib3x

.. code-block:: python

    >>> import pathlib3x
    >>> import pathlib

    >>> pathlib3x_path = pathlib3x.Path('some_path')  # this might happen in another module !
    >>> pathlib_path = pathlib.Path('some_path')
    >>> isinstance(pathlib3x_path, pathlib.Path)
    False
    >>> isinstance(pathlib_path, pathlib3x.Path)
    False

    # in such cases were You need to mix pathlib and pathlib3x in different modules, use:
    >>> pathlib3x_path.Path.is_path_instance(pathlib3x_path)
    True
    >>> pathlib3x_path.Path.is_path_instance(pathlib_path)
    True


PurePath.replace_parts(old, new, count=-1)
    Return a new Path with parts replaced. If the Original Path or *old* has no parts, the Original Path will be returned.
    On Windows, the replacement operation is not case sensitive, because of case folding on drives, directory and filenames.
    You can also replace absolute paths with relative paths what is quite handy - just be aware that the results might
    look unexpected, especially on Windows.

    *old, new* can be pathlib.Path or Path-like objects

    if the Original Path is resolved, You should probably also resolve *old* and *new* - because if symlinks are involved,
    the results might be unexpected.

    be aware of case folding in windows, the file "c:/Test/test.txt" is the same as "c:/test/Test.TXT"

.. code-block:: python

    >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    >>> p.replace_parts(PureWindowsPath('C:/downloads'), PureWindowsPath('D:/uploads'))
    PureWindowsPath('D:/uploads/pathlib.tar.gz')

    >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    >>> p.replace_parts('C:/downloads','D:/uploads')
    PureWindowsPath('D:/uploads/pathlib.tar.gz')

    # handy to replace source directories with target directories on copy or move operations :
    >>> source_dir = pathlib.Path('c:/source_dir')
    >>> target_dir = pathlib.Path('c:/target_dir')
    >>> source_files = source_dir.glob('**/*.txt')
    >>> for source in source_files:
            target = source.replace_parts(source_dir, target_dir)
    ...     source.copy(target)

    # this will always return PureWindowsPath(), because PureWindowsPath('.') has no parts to replace
    >>> p = PureWindowsPath('.')
    >>> p.replace_parts('.', 'test')
    PureWindowsPath()

    # looks unexpected but is correct, since PureWindowsPath('/uploads') is a relative path in Windows
    >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    >>> p.replace_parts('C:/downloads', '/uploads')
    PureWindowsPath('uploads/pathlib.tar.gz')

    # take care when replace, it might match on parts You are not aware of
    >>> p = PureWindowsPath('c:/downloads/Downloads.tar.gz')
    >>> p.replace_parts('downloads', 'uploads')
    PureWindowsPath('c:/uploads/uploads.tar.gz')    # that was not intended !

    # better
    >>> p = PureWindowsPath('c:/downloads/Downloads.tar.gz')
    >>> p.replace_parts('downloads', 'uploads', 1)
    PureWindowsPath('c:/uploads/Downloads.tar.gz')

    # much better
    >>> p = PureWindowsPath('c:/downloads/Downloads.tar.gz')
    >>> p.replace_parts('c:/downloads', 'c:/uploads')
    PureWindowsPath('c:/uploads/Downloads.tar.gz')


shutil wrappers
===============

Path.copy(target, follow_symlinks)
    wraps shutil.copy, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> s = Path('c:/Downloads/pathlib.tar.gz')
    >>> t = PureWindowsPath('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copy(t)

Path.copy2(target, follow_symlinks=True)
    wraps shutil.copy2, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> s = Path('c:/Downloads/pathlib.tar.gz')
    >>> t = PureWindowsPath('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copy2(t)

Path.copyfile(target, follow_symlinks)
    wraps shutil.copyfile, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> s = Path('c:/Downloads/pathlib.tar.gz')
    >>> t = PureWindowsPath('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copyfile(t)

Path.copymode(target, follow_symlinks=True)
    wraps shutil.copymode, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> s = Path('c:/Downloads/pathlib.tar.gz')
    >>> t = PureWindowsPath('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copymode(t)

Path.copystat(target, follow_symlinks=True)
    wraps shutil.copystat, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> s = Path('c:/Downloads/pathlib.tar.gz')
    >>> t = PureWindowsPath('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copystat(t)

Path.copytree(target, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=True, dirs_exists_ok=False)
    wraps shutil.copytree, see: https://docs.python.org/3/library/shutil.html

    dirs_exists_ok=True will raise a TypeError on Python Versions < 3.8

.. code-block:: python

    >>> s = Path('c:/Downloads')
    >>> t = PureWindowsPath('c:/temp/Backups')
    >>> s.copytree(t)

Path.rmtree(ignore_errors=False, onerror=None)
    wraps shutil.rmtree, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> p = Path('c:/Downloads/old')
    >>> p.rmtree()


Caveats of pathlib3x
====================

.. code-block::

    >>> import pathlib3x
    >>> import pathlib

    >>> pathlib3x_path = pathlib3x.Path('some_path')  # this might happen in another module !
    >>> pathlib_path = pathlib.Path('some_path')
    >>> isinstance(pathlib3x_path, pathlib.Path)
    False
    >>> isinstance(pathlib_path, pathlib3x.Path)
    False

    # in such cases were You need to mix pathlib and pathlib3x in different modules, use:
    >>> pathlib3x_path.Path.is_path_instance(pathlib3x_path)
    True
    >>> pathlib3x_path.Path.is_path_instance(pathlib_path)
    True


So dont mix pathlib with pathlib3x and expect that objects are an instance of Pathlib and vice versa.
This can happen easily if You have many Modules. Just keep it in mind !
