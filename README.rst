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

Backport (actually a blunt copy) of python 3.8 pathlib for python 3.6, 3.7

this will be updated periodically to have the latest version of pathlib available on 3.6, 3.7 and probably others.

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

A very few of own extensions to that pathlib will be added probably over time.

If You have some nice features for pathlib, let me know - I will consider to integrate them.

----

automated tests, Travis Matrix, Documentation, Badges, etc. are managed with `PizzaCutter <https://github
.com/bitranox/PizzaCutter>`_ (cookiecutter on steroids)

tested on linux "bionic" with python 3.6, 3.7, 3.8, 3.8-dev, pypy3

`100% (for my added functions) code coverage <https://codecov.io/gh/bitranox/pathlib3x>`_, tested under `Linux, macOS, Windows <https://travis-ci.org/bitranox/pathlib3x>`_, automatic daily builds and monitoring

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

Usage from Commandline
------------------------

.. code-block:: bash

   Usage: pathlib3x [OPTIONS] COMMAND [ARGS]...

     backport of latest pathlib to python 3.6, 3.7 with a few extensions

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

0.1.1
-----
2020-07-01: maintainance release
    - guarded the sys.audit calls with try-except clauses, because sys.event is only avail in python 3.8


0.1.0
-----
2020-06-29: initial release
    - initial release

