Changelog
=========

- new MAJOR version for incompatible API changes,
- new MINOR version for added functionality in a backwards compatible manner
- new PATCH version for backwards compatible bug fixes

0.3.5
-----
2020-07-15 : development
    -

0.3.4
-----
2020-07-15 : patch release
    - fix cli test
    - enable traceback option on cli

0.3.3
-----
2020-07-15 : patch release
    - fix minor typos

0.3.2
-----
2020-07-05 : patch release
    - fix typo in setup.py setup parameter zip_safe

0.3.1
-----
2020-07-05 : patch release
    - fix version issues in the stub files

0.3.0
-----
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
