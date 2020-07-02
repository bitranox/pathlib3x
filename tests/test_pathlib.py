import os
import pathlib3x as pathlib
import unittest


def test_pathlib():
    """
    >>> test_pathlib()
    """
    pathlib.Path('__not_existing__').unlink(missing_ok=True)
    pathlib.Path('.').glob('**/*')
    pathlib.Path('.').rglob('**/*')


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


def test_append_suffix():
    """ test non-standard bitranox method append_suffix

    >>> test_append_suffix()
    """

    # setup
    path_without_suffix = pathlib.Path('path_without_suffix')
    path_with_suffix = pathlib.Path('path_with.suffix')

    # test OK
    path_without_suffix_appended = path_without_suffix.append_suffix('.test')
    path_with_suffix_appended = path_with_suffix.append_suffix('.test')
    assert path_without_suffix_appended.suffix == '.test'
    assert path_without_suffix_appended.suffixes == ['.test']
    assert path_with_suffix_appended.suffix == '.test'
    assert path_with_suffix_appended.suffixes == ['.suffix', '.test']
