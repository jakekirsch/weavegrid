import pytest

from app.controller.controller import list_contents_of_dir, get_contents_of_file
from app.models.models import DirectoryEntry

@pytest.fixture(scope='function')
def valid_dirpath():
    return 'tests/sample_dir'

@pytest.fixture(scope='function')
def valid_filepath():
    return 'tests/sample_dir/test.txt'

@pytest.fixture(scope='function')
def invalid_dirpath():
    return 'tests/sample_dir_invalid'

@pytest.fixture(scope='function')
def invalid_filepath():
    return 'tests/sample_dir/invalidtest.txt'


def test_list_contents_of_dir_valid_dirpath(valid_dirpath):
    contents = list_contents_of_dir(valid_dirpath)
    assert len(contents) != 0
    for dir in contents:
        assert isinstance(dir, DirectoryEntry)
        assert dir.name is not None
        assert dir.owner is not None
        assert dir.size is not None
        assert dir.permissions is not None

def test_list_contents_of_dir_invalid_dirpath(invalid_dirpath):
    with pytest.raises(FileNotFoundError):
        contents = list_contents_of_dir(invalid_dirpath)

def test_list_contents_of_file_valid_filepath(valid_filepath):
    contents = get_contents_of_file(valid_filepath)
    assert isinstance(contents, str)
    assert contents == "this is a test file\nwith two lines of text\n"

def test_list_contents_of_file_invalid_filepath(invalid_filepath):
    with pytest.raises(FileNotFoundError):
        contents = get_contents_of_file(invalid_filepath)
