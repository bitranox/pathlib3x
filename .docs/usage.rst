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


PurePath.replace_parts(old, new, count=-1)
    Return a new Path with parts replaced. If the Original Part or old has no parts, the Original Path will be returned.
    On Windows the replacement is not case sensitive because of case folding on drives, directory and filenames.
    You can also replace absolute paths with relative paths what is quite handy - just be aware that the results might
    look unexpected, especially on Windows.

    if the Original Path is resolved, You should probably also resolve the old and new paths - because if symlinks are involved,
    the results might be unexpected.

.. code-block:: python

    >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    >>> p.replace_parts(PureWindowsPath('C:/downloads'), PureWindowsPath('D:/uploads'))
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
    >>> p.replace_parts(PureWindowsPath('.'), PureWindowsPath('test'))
    PureWindowsPath()

    # looks unexpected but is correct, since PureWindowsPath('/uploads') is a relative path in Windows
    >>> p = PureWindowsPath('c:/Downloads/pathlib.tar.gz')
    >>> p.replace_parts(PureWindowsPath('C:/downloads'), PureWindowsPath('/uploads'))
    PureWindowsPath('uploads/pathlib.tar.gz')


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

    >>> some_path = pathlib3x.Path('some_file')  # this might happen in another module !
    >>> isinstance(some_path, pathlib.Path)
    False

    # in such cases were You need to mix pathlib and pathlib3x in different modules, use something like:
    >>> 'Path' in str(type(some_path)).rsplit('.', 1)[-1]
    True


So dont mix pathlib with pathlib3x and expect that objects are an instance of Pathlib and vice versa.
This can happen easily if You have many Modules. Just keep it in mind !

