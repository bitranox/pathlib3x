pathlib3x
=========

|travis_build| |license| |pypi|

|codecov| |better_code| |cc_maintain| |cc_issues| |cc_coverage| |snyk|


.. |travis_build| image:: https://img.shields.io/travis/bitranox/pathlib3x/master.svg
   :target: https://travis-ci.org/bitranox/pathlib3x

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge.svg
   :target: https://mybinder.org/v2/gh/bitranox/pathlib3x/master?filepath=jupyter_test_pathlib3x.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/pathlib3x?label=PyPI%20Package
   :target: https://badge.fury.io/py/pathlib3x


.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/pathlib3x
   :target: https://codecov.io/gh/bitranox/pathlib3x

.. |better_code| image:: https://bettercodehub.com/edge/badge/bitranox/pathlib3x?branch=master
   :target: https://bettercodehub.com/results/bitranox/pathlib3x

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/pathlib3x?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/pathlib3x/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/pathlib3x?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/pathlib3x/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/pathlib3x?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/pathlib3x/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://img.shields.io/snyk/vulnerabilities/github/bitranox/pathlib3x
   :target: https://snyk.io/test/github/bitranox/pathlib3x

Backport of python 3.10.0a0 (beta) pathlib for python 3.6, 3.7, 3.8, 3.9 with a few tweaks to make it compatible.

added wrappers to shutil copy, copy2, rmtree, copytree and other useful functions.

fully typed PEP561 package

this will be updated periodically to have the latest version of pathlib available on 3.6, 3.7, 3.8, 3.9 and probably others.

WHY pathlib3x ?
===============

There are a number of small, but very handy features added in pathlib over the last python versions,
so I want to be able to use those also on older python versions.


if You are used to :

.. code-block::

    import pathlib

    pathlib.Path('some_file').unlink(missing_ok=True)

You will have no luck on python 3.7 - because the "missing_ok" parameter was added in python3.8

Of course You can do :

.. code-block::

    import pathlib

    try:
        pathlib.Path('some_file').unlink()
    except FileNotFoundError:
        pass



but that clutters the code unnecessarily. So just use :

.. code-block::

    import pathlib3x as pathlib


and You can enjoy the latest pathlib features even on older python versions.

Some own extensions to that pathlib will be added probably over time. At the moment we added some wrappers to shutil like "copy", "rmtree", "copytree", so
You can do :

.. code-block::

    import pathlib3x as pathlib
    my_file = pathlib.Path('/etc/hosts')
    to_file = pathlib.Path('/tmp/foo')
    my_file.copy(to_file)


If You have some nice features for pathlib, let me know - I will consider to integrate them.

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.6.0 or newer

tested on linux "bionic" with python 3.6, 3.7, 3.8, 3.8-dev, pypy3

`100% (for my added functions) code coverage <https://codecov.io/gh/bitranox/pathlib3x>`_, mypy static type checking ,tested under `Linux, macOS, Windows <https://travis-ci.org/bitranox/pathlib3x>`_, automatic daily builds and monitoring

----

- `Installation and Upgrade`_
- `Usage`_
- `Usage from Commandline`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/pathlib3x/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/pathlib3x/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/pathlib3x/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----



Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools
    python -m pip --upgrade wheel

- to install the latest release from PyPi via pip (recommended):

.. code-block:: bash

    # install latest release from PyPi
    python -m pip install --upgrade pathlib3x

    # test latest release from PyPi without installing (can be skipped)
    python -m pip install pathlib3x --install-option test

- to install the latest development version from github via pip:


.. code-block:: bash

    # normal install
    python -m pip install --upgrade git+https://github.com/bitranox/pathlib3x.git

    # to test without installing (can be skipped)
    python -m pip install git+https://github.com/bitranox/pathlib3x.git --install-option test

    # to install and upgrade all dependencies regardless of version number
    python -m pip install --upgrade git+https://github.com/bitranox/pathlib3x.git --upgrade-strategy eager


- include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    pathlib3x

    # for the latest development version :
    pathlib3x @ git+https://github.com/bitranox/pathlib3x.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt



- to install the latest development version from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/pathlib3x.git
    $ cd pathlib3x

    # to test without installing (can be skipped)
    python setup.py test

    # normal install
    python setup.py install

- via makefile:
  makefiles are a very convenient way to install. Here we can do much more,
  like installing virtual environments, clean caches and so on.

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/pathlib3x.git
    $ cd pathlib3x

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Usage
-----------

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

    >>> import pathlib3x as pathlib
    >>> s = pathlib.Path('c:/Downloads/pathlib.tar.gz')
    >>> t = pathlib.Path('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copy(t)

Path.copy2(target, follow_symlinks=True)
    wraps shutil.copy2, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> import pathlib3x as pathlib
    >>> s = pathlib.Path('c:/Downloads/pathlib.tar.gz')
    >>> t = pathlib.Path('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copy2(t)

Path.copyfile(target, follow_symlinks)
    wraps shutil.copyfile, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> import pathlib3x as pathlib
    >>> s = pathlib.Path('c:/Downloads/pathlib.tar.gz')
    >>> t = pathlib.Path('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copyfile(t)

Path.copymode(target, follow_symlinks=True)
    wraps shutil.copymode, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> import pathlib3x as pathlib
    >>> s = pathlib.Path('c:/Downloads/pathlib.tar.gz')
    >>> t = pathlib.Path('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copymode(t)

Path.copystat(target, follow_symlinks=True)
    wraps shutil.copystat, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> import pathlib3x as pathlib
    >>> s = pathlib.Path('c:/Downloads/pathlib.tar.gz')
    >>> t = pathlib.Path('c:/Downloads/pathlib.tar.gz.backup')
    >>> s.copystat(t)

Path.copytree(target, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=True, dirs_exists_ok=False)
    wraps shutil.copytree, see: https://docs.python.org/3/library/shutil.html

    dirs_exists_ok=True will raise a TypeError on Python Versions < 3.8

.. code-block:: python

    >>> import pathlib3x as pathlib
    >>> s = pathlib.Path('c:/Downloads')
    >>> t = pathlib.Path('c:/temp/Backups')
    >>> s.copytree(t)

Path.rmtree(ignore_errors=False, onerror=None)
    wraps shutil.rmtree, see: https://docs.python.org/3/library/shutil.html

.. code-block:: python

    >>> import pathlib3x as pathlib
    >>> p = pathlib.Path('c:/Downloads/old')
    >>> p.rmtree()


Caveats of pathlib3x
====================

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


So dont mix pathlib with pathlib3x and expect that objects are an instance of Pathlib and vice versa.
This can happen easily if You have many Modules. Just keep it in mind !

Usage from Commandline
------------------------

.. code-block:: bash

   Usage: pathlib3x [OPTIONS] COMMAND [ARGS]...

     backport of pathlib 3.10 to python 3.6, 3.7, 3.8, 3.9 with a few
     extensions

   Options:
     --version   Show the version and exit.
     -h, --help  Show this message and exit.

   Commands:
     info  get program informations

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/pathlib3x/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

0.3.0
-----
2020-07-04 : added functions, include stub files for typing, setup python_requires
    - added python_requires in setup.py
    - include type stub files, its fully type hinted package now (PEP 561)
    - get rid of zip_save warning when running setup on windows
    - pep8 fix the standard library code
    - added PurePath.replace_parts
    - added Path.copy
    - added Path.copy2
    - added Path.copyfile
    - added Path.copymode
    - added Path.copystat
    - added Path.copytree
    - added Path.rmtree

0.2.0
-----
2020-07-02 : added function: PurePath.append_suffix(suffix)
    - added function: PurePath.append_suffix(suffix)

0.1.1
-----
2020-07-01: patch release
    - guarded the sys.audit calls with try-except clauses, because sys.event is only avail in python 3.8


0.1.0
-----
2020-06-29: initial release
    - initial release

