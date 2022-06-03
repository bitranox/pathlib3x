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
