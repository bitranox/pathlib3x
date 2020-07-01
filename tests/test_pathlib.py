import pathlib3x as pathlib


def test_pathlib():
    """
    >>> test_pathlib()
    """
    pathlib.Path('__not_existing__').unlink(missing_ok=True)
    pathlib.Path('.').glob('**/*')
    pathlib.Path('.').rglob('**/*')
