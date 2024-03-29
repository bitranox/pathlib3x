pathlib3x
=========


Version v2.0.3 as of 2023-07-20 see `Changelog`_

|build_badge| |codeql| |license| |pypi|
|pypi-downloads| |black| |codecov| |cc_maintain| |cc_issues| |cc_coverage| |snyk|



.. |build_badge| image:: https://github.com/bitranox/pathlib3x/actions/workflows/python-package.yml/badge.svg
   :target: https://github.com/bitranox/pathlib3x/actions/workflows/python-package.yml


.. |codeql| image:: https://github.com/bitranox/pathlib3x/actions/workflows/codeql-analysis.yml/badge.svg?event=push
   :target: https://github.com//bitranox/pathlib3x/actions/workflows/codeql-analysis.yml

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License

.. |jupyter| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/bitranox/pathlib3x/master?filepath=pathlib3x.ipynb

.. for the pypi status link note the dashes, not the underscore !
.. |pypi| image:: https://img.shields.io/pypi/status/pathlib3x?label=PyPI%20Package
   :target: https://badge.fury.io/py/pathlib3x

.. |codecov| image:: https://img.shields.io/codecov/c/github/bitranox/pathlib3x
   :target: https://codecov.io/gh/bitranox/pathlib3x

.. |cc_maintain| image:: https://img.shields.io/codeclimate/maintainability-percentage/bitranox/pathlib3x?label=CC%20maintainability
   :target: https://codeclimate.com/github/bitranox/pathlib3x/maintainability
   :alt: Maintainability

.. |cc_issues| image:: https://img.shields.io/codeclimate/issues/bitranox/pathlib3x?label=CC%20issues
   :target: https://codeclimate.com/github/bitranox/pathlib3x/maintainability
   :alt: Maintainability

.. |cc_coverage| image:: https://img.shields.io/codeclimate/coverage/bitranox/pathlib3x?label=CC%20coverage
   :target: https://codeclimate.com/github/bitranox/pathlib3x/test_coverage
   :alt: Code Coverage

.. |snyk| image:: https://snyk.io/test/github/bitranox/pathlib3x/badge.svg
   :target: https://snyk.io/test/github/bitranox/pathlib3x

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/pathlib3x
   :target: https://pypi.org/project/pathlib3x/
   :alt: PyPI - Downloads

Backport of Python 3.11.0a0 pathlib for Python 3.6, 3.7, 3.8, 3.9, 3.10 with a few tweaks to make it compatible.

added wrappers to shutil copy, copy2, rmtree, copytree and other useful functions.

fully typed PEP561 package

this will be updated periodically to have the latest version of pathlib available on 3.6, 3.7, 3.8, 3.9, 3.10 and probably others.

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

automated tests, Github Actions, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

Python version required: 3.8.0 or newer

tested on recent linux with python 3.8, 3.9, 3.10, 3.11, 3.12-dev, pypy-3.9, pypy-3.10 - architectures: amd64

`100% (for my added functions) code coverage <https://codeclimate.com/github/bitranox/pathlib3x/test_coverage>`_, flake8 style checking ,mypy static type checking ,tested under `Linux, macOS, Windows <https://github.com/bitranox/pathlib3x/actions/workflows/python-package.yml>`_, automatic daily builds and monitoring

----

- `Usage`_
- `Usage from Commandline`_
- `Installation and Upgrade`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/pathlib3x/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/pathlib3x/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/pathlib3x/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----



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

.. code-block::

   Usage: pathlib3x [OPTIONS] COMMAND [ARGS]...

     backport of pathlib 3.10 to python 3.6, 3.7, 3.8, 3.9 with a few extensions

   Options:
     --version                     Show the version and exit.
     --traceback / --no-traceback  return traceback information on cli
     -h, --help                    Show this message and exit.

   Commands:
     info  get program informations

Installation and Upgrade
------------------------

- Before You start, its highly recommended to update pip and setup tools:


.. code-block::

    python -m pip --upgrade pip
    python -m pip --upgrade setuptools

- to install the latest release from PyPi via pip (recommended):

.. code-block::

    python -m pip install --upgrade pathlib3x


- to install the latest release from PyPi via pip, including test dependencies:

.. code-block::

    python -m pip install --upgrade pathlib3x[test]

- to install the latest version from github via pip:


.. code-block::

    python -m pip install --upgrade git+https://github.com/bitranox/pathlib3x.git


- include it into Your requirements.txt:

.. code-block::

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi:
    pathlib3x

    # for the latest development version :
    pathlib3x @ git+https://github.com/bitranox/pathlib3x.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python -m pip install --upgrade -r /<path>/requirements.txt


- to install the latest development version, including test dependencies from source code:

.. code-block::

    # cd ~
    $ git clone https://github.com/bitranox/pathlib3x.git
    $ cd pathlib3x
    python -m pip install -e .[test]

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

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    click
    cli_exit_tools

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

v2.0.3
---------
2023-07-13:
    - require minimum python 3.8
    - remove python 3.7 tests
    - introduce PEP517 packaging standard
    - introduce pyproject.toml build-system
    - remove mypy.ini
    - remove pytest.ini
    - remove setup.cfg
    - remove setup.py
    - remove .bettercodehub.yml
    - remove .travis.yml
    - update black config
    - clean ./tests/test_cli.py
    - add codeql badge
    - move 3rd_party_stubs outside the src directory to ``./.3rd_party_stubs``
    - add pypy 3.10 tests
    - add python 3.12-dev tests


v2.0.2.1
--------
2022-06-03: use io.encoding only on 3.10 upwards

v2.0.2
--------
2022-06-03: define __fspath__ only on python >= 3.10

v2.0.1
--------
2022-06-03: use io.encoding only on 3.10 upwards

v2.0.0
--------
2022-06-03:
    - upgrade to pathlib python 3.11a0 version
    - upgrade to github actions @v3

v1.3.9
--------
2020-10-09: service release
    - update travis build matrix for linux 3.9-dev
    - update travis build matrix (paths) for windows 3.9 / 3.10

v1.3.8
--------
2020-08-08: service release
    - fix documentation
    - fix travis
    - deprecate pycodestyle
    - implement flake8

v1.3.7
---------
2020-08-01: fix pypi deploy

v1.3.6
--------
2020-07-31: fix travis build

v0.3.5
--------
2020-07-29: feature release
    - use the new pizzacutter template
    - use cli_exit_tools

v0.3.4
--------
2020-07-15 : patch release
    - fix cli test
    - enable traceback option on cli errors

v0.3.3
--------
2020-07-15 : patch release
    - fix minor typos

v0.3.2
--------
2020-07-05 : patch release
    - fix typo in setup.py setup parameter zip_safe

v0.3.1
--------
2020-07-05 : patch release
    - fix version issues in the stub files

v0.3.0
--------
2020-07-05 : added functions, include stub files for typing, setup python_requires
    - added python_requires in setup.py
    - include type stub files, its fully type hinted package now (PEP 561)
    - pep8 fix the standard library code
    - added PurePath.replace_parts
    - added PurePath.is_path_instance
    - added Path.copy
    - added Path.copy2
    - added Path.copyfile
    - added Path.copymode
    - added Path.copystat
    - added Path.copytree
    - added Path.rmtree

v0.2.0
--------
2020-07-02 : added function: PurePath.append_suffix(suffix)
    - added function: PurePath.append_suffix(suffix)

v0.1.1
--------
2020-07-01: patch release
    - guarded the sys.audit calls with try-except clauses, because sys.event is only avail in python 3.8


v0.1.0
--------
2020-06-29: initial release
    - initial release

