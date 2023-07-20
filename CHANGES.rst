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
