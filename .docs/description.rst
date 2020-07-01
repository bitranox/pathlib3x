Backport (actually a blunt copy) of python 3.8 pathlib for python 3.6, 3.7 with a few tweaks to make it compatible.

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
