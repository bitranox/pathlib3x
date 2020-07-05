import os
import pathlib3x as pathlib
import pathlib as pathlib_original
import pytest               # type: ignore
from typing import Any
import unittest


class TestPathlibFunctions(unittest.TestCase):

    def test_unlink_missing_ok(self):
        pathlib.Path('__not_existing__').unlink(missing_ok=True)

    def test_glob(self):
        pathlib.Path('.').glob('**/*')


class TestAppendSuffix(unittest.TestCase):

    def test_append_suffix_ok(self):
        # setup
        path_without_suffix = pathlib.Path('path_without_suffix')
        path_with_suffix = pathlib.Path('path_with.suffix')
        path_without_suffix_appended = path_without_suffix.append_suffix('.test')
        path_with_suffix_appended = path_with_suffix.append_suffix('.test')
        # tests
        self.assertEqual(path_without_suffix_appended.suffix, '.test')
        self.assertEqual(path_without_suffix_appended.suffixes, ['.test'])
        self.assertEqual(path_with_suffix_appended.suffix, '.test')
        self.assertEqual(path_with_suffix_appended.suffixes, ['.suffix', '.test'])
        # test empty suffix
        self.assertEqual(pathlib.Path('some_path').append_suffix(''), pathlib.Path('some_path'))

    def test_append_suffix_empty_name_raises(self):
        path_with_empty_name = pathlib.Path('')
        self.assertRaises(ValueError, path_with_empty_name.append_suffix, '.test')

    def test_append_suffix_invalid_suffix_raises(self):
        path_test = pathlib.Path('some_path')
        # test suffix not starting with '.'
        self.assertRaises(ValueError, path_test.append_suffix, 'test')
        # test suffix is only '.'
        self.assertRaises(ValueError, path_test.append_suffix, '.')

    def test_append_suffix_sep_or_altsep_in_suffix_raises(self):
        # Setup
        path_test = pathlib.Path('path_test')
        suffix_with_sep = '.test' + os.path.sep + 'test'

        # Test
        self.assertRaises(ValueError, path_test.append_suffix, suffix_with_sep)
        if os.path.altsep:  # altsep is '/' on Windows
            suffix_with_altsep = '.test' + os.path.altsep + 'test'
            self.assertRaises(ValueError, path_test.append_suffix, suffix_with_altsep)


@pytest.fixture(params=[pathlib.PurePath(''), pathlib.PurePath('./test/Test1/test2/test3'), pathlib.PurePosixPath('/test/Test1/test2/test3'),
                        pathlib.PureWindowsPath('C:\\test\\Test1/test2/test3')],
                ids=['Empty', 'Relative', 'PosixAbsolute', 'WindowsAbsolute'])
def source_path(request: Any) -> pathlib.PurePath:
    return request.param


@pytest.fixture(params=[pathlib.PurePath(''), pathlib.PurePath('Test1/test2'), pathlib.PurePath('test1/test2'), pathlib.PurePath('test/test'),
                pathlib.PurePosixPath('/test/Test1'), pathlib.PurePosixPath('/test/test1'),
                pathlib.PureWindowsPath('C:\\test\\Test1'), pathlib.PureWindowsPath('c:\\test\\test1'), pathlib.PureWindowsPath('c:\\test\\test')],
                ids=['Empty', 'RelativeMatch', 'RelativeWinMatch', 'RelativeNoMatch',
                     'PosixAbsoluteMatch', 'PosixAbsoluteNoMatch',
                     'WinAbsoluteMatch', 'WinAbsoluteMatchLower', 'WinAbsoluteNoMatch'])
def old(request: Any) -> pathlib.PurePath:
    return request.param


def test_replace_parts(source_path, old):
    new = pathlib.PurePath('new1/new2/new3/new4')
    source_path.replace_parts(old, new)
    if source_path == pathlib.PurePath('') or old == pathlib.PurePath(''):
        assert source_path.replace_parts(old, new) == source_path


def test_replace_parts_doctest():
    """

    # check Path like
    >>> pathlib.PurePath('test/test/test').replace_parts('test','testnew/testnew', 1)
    Pure...Path('testnew/testnew/test/test')

    >>> new = pathlib.PurePath('new1/new2/new3/new4')

    >>> # Test Source Path = relative PurePath
    >>> source_path = pathlib.PurePath('./test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePath('Test1/test2'), new)
    Pure...Path('test/new1/new2/new3/new4/test3')

    >>> source_path.replace_parts(pathlib.PurePath('test/test'), new)
    Pure...Path('test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePosixPath('/test/Test1'), new)
    Pure...Path('test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePosixPath('/test/test1'), new)
    Pure...Path('test/Test1/test2/test3')

    >>> # Test Source Path = absolute PosixPath
    >>> source_path = pathlib.PurePosixPath('/test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePath('Test1/test2'), new)
    Pure...Path('/test/new1/new2/new3/new4/test3')

    >>> source_path.replace_parts(pathlib.PurePath('test1/test2'), new)
    Pure...Path('/test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePath('test/test'), new)
    Pure...Path('/test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePosixPath('/test/Test1'), new)
    Pure...Path('new1/new2/new3/new4/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePosixPath('/test/test1'), new)
    Pure...Path('/test/Test1/test2/test3')

    >>> # Test Source Path = absolute WindowsPath
    >>> source_path = pathlib.PureWindowsPath(r'C:\\test\\Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePath('Test1/test2'), new)
    PureWindowsPath('C:/test/new1/new2/new3/new4/test3')

    >>> # this will be replaced because of windows case folding, it is correct !
    >>> source_path.replace_parts(pathlib.PurePath('test1/test2'), new)
    PureWindowsPath('C:/test/new1/new2/new3/new4/test3')

    >>> source_path.replace_parts(pathlib.PurePath('test/test'), new)
    PureWindowsPath('C:/test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePosixPath('/test/Test1'), new)
    PureWindowsPath('C:/test/Test1/test2/test3')

    >>> source_path.replace_parts(pathlib.PurePosixPath('/test/test1'), new)
    PureWindowsPath('C:/test/Test1/test2/test3')

    # this might be unexpected but correct - we make a relative path out of an absolute path
    >>> source_path.replace_parts(pathlib.PureWindowsPath(r'C:\\test\\Test1'), new)
    PureWindowsPath('new1/new2/new3/new4/test2/test3')

    >>> source_path.replace_parts(pathlib.PureWindowsPath(r'C:\\test\\Test1'), pathlib.PureWindowsPath(r'd:\\new'))
    PureWindowsPath('d:/new/test2/test3')

    >>> source_path.replace_parts(pathlib.PureWindowsPath(r'c:\\test\\test1'), pathlib.PureWindowsPath(r'D:\\new'))
    PureWindowsPath('D:/new/test2/test3')

    >>> source_path.replace_parts(pathlib.PureWindowsPath(r'c:\\test\\test'), pathlib.PureWindowsPath(r'D:\\new'))
    PureWindowsPath('C:/test/Test1/test2/test3')

    >>> # check count
    >>> pathlib.PurePath('test/test/test').replace_parts(pathlib.PurePath('test/test'), pathlib.PurePath('testnew/testnew'), 3)
    Pure...Path('testnew/testnew/test')
    >>> pathlib.PurePath('test/test/test').replace_parts(pathlib.PurePath('test/test'), pathlib.PurePath('testnew/testnew'), 1)
    Pure...Path('testnew/testnew/test')
    >>> pathlib.PurePath('test/test/test').replace_parts(pathlib.PurePath('test/test'), pathlib.PurePath('testnew/testnew'), 0)
    Pure...Path('test/test/test')
    >>> pathlib.PurePath('test/test/test').replace_parts(pathlib.PurePath('test'), pathlib.PurePath('testnew/testnew'), 1)
    Pure...Path('testnew/testnew/test/test')
    >>> pathlib.PurePath('test').replace_parts(pathlib.PurePath('test'), pathlib.PurePath('testnew/testnew'), 1)
    Pure...Path('testnew/testnew')

    """
    pass


def test_shutil_wrappers():
    """ test the shutil wrappers """
    path_test_dir = pathlib.Path(__file__).parent.resolve()
    path_test_file = path_test_dir / 'test.txt'
    path_target_file = path_test_dir / 'test_target.txt'
    path_test_tree = path_test_dir / 'test_treecopy'
    path_test_tree_target = path_test_dir / 'test_treecopy_target'
    path_test_file.copy(path_target_file)
    path_test_file.copy2(path_target_file)
    path_test_file.copyfile(path_target_file)
    path_test_file.copymode(path_target_file)
    path_test_file.copystat(path_target_file)
    path_test_tree.copytree(path_test_tree_target)
    path_test_tree_target.rmtree()
    path_target_file.unlink()


def test_interaction_with_original_pathlib():
    pathlib_original_file = pathlib_original.Path('some_path/some_path/some_path.txt')
    pathlib3x_file = pathlib.Path('some_path3x/some_path3x/some_path3x.txt')
    assert pathlib.Path.is_path_instance(pathlib_original_file)
    assert pathlib.Path.is_path_instance(pathlib3x_file)
    test_conversion = pathlib.Path(pathlib_original_file)
    isinstance(test_conversion, pathlib.Path)
